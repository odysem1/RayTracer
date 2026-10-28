import re
import subprocess
from pathlib import Path
from statistics import mean


PROJECT_ROOT = Path(__file__).resolve().parent.parent
EXECUTABLE = PROJECT_ROOT / "build" / "raytracer.exe"

THREAD_COUNTS = [1, 2, 4, 8]
RUNS_PER_CASE = 3

TIME_PATTERN = re.compile(
    r"RENDER_TIME_SECONDS:\s*"
    r"([0-9]+(?:\.[0-9]*)?(?:[eE][+-]?[0-9]+)?)"
)


def run_once(thread_count: int) -> float:
    # Scene and camera settings come from the compiled C++ code.
    # Only the worker count is passed as a command-line argument.
    result = subprocess.run(
        [str(EXECUTABLE), str(thread_count)],
        cwd=PROJECT_ROOT,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8",
        errors="replace",
    )

    if result.returncode != 0:
        raise RuntimeError(
            f"Renderer failed with {thread_count} workers "
            f"(exit code: {result.returncode}).\n"
            f"{result.stderr}"
        )

    match = TIME_PATTERN.search(result.stderr)
    if match is None:
        raise RuntimeError(
            "RENDER_TIME_SECONDS was not found.\n"
            f"{result.stderr}"
        )

    seconds = float(match.group(1))
    if not 0.0 < seconds < float("inf"):
        raise RuntimeError(f"Invalid render time: {seconds}")

    return seconds


def main() -> None:
    if not EXECUTABLE.is_file():
        raise FileNotFoundError(f"Executable not found: {EXECUTABLE}")

    results = {}

    print("Using scene and camera settings from the compiled executable.")
    print("Only worker count changes: 1 / 2 / 4 / 8.")
    print("PPM output is discarded.\n")

    for thread_count in THREAD_COUNTS:
        print(f"[{thread_count} workers] Warm-up...", flush=True)
        run_once(thread_count)

        times = []
        for run in range(RUNS_PER_CASE):
            seconds = run_once(thread_count)
            times.append(seconds)
            print(
                f"[{thread_count} workers] "
                f"Run {run + 1}: {seconds:.6f}s",
                flush=True,
            )

        results[thread_count] = times
        print()

    baseline = mean(results[1])

    columns = (
        ["Workers"]
        + [f"Run {i + 1} (s)" for i in range(RUNS_PER_CASE)]
        + ["Avg (s)", "Speedup"]
    )
    print("| " + " | ".join(columns) + " |")
    print("| " + " | ".join(["---:"] * len(columns)) + " |")

    for thread_count, times in results.items():
        average = mean(times)
        row = (
            [str(thread_count)]
            + [f"{seconds:.6f}" for seconds in times]
            + [f"{average:.6f}", f"{baseline / average:.2f}x"]
        )
        print("| " + " | ".join(row) + " |")


if __name__ == "__main__":
    try:
        main()
    except (OSError, RuntimeError) as error:
        raise SystemExit(f"Benchmark failed:\n{error}")
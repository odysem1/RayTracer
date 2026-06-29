import subprocess
import re
from statistics import mean

SPHERE_COUNTS = [100, 200, 500, 1000]
RUNS_PER_CASE = 3
EXECUTABLE = "./raytracer"

TIME_PATTERN = re.compile(r"RENDER_TIME_SECONDS:\s*([0-9.]+)")


def run_once(sphere_count: int) -> float:
    output_file = f"benchmark_{sphere_count}.ppm"

    with open(output_file, "wb") as out:
        result = subprocess.run(
            [EXECUTABLE, str(sphere_count)],
            stdout=out,
            stderr=subprocess.PIPE,
            text=True,
            check=True,
        )

    match = TIME_PATTERN.search(result.stderr)

    if not match:
        print("stderr output:")
        print(result.stderr)
        raise RuntimeError("Could not find render time in stderr output.")

    return float(match.group(1))


def main():
    print("| Small Spheres | Total Objects | Run 1 | Run 2 | Run 3 | Avg |")
    print("|---:|---:|---:|---:|---:|---:|")

    for sphere_count in SPHERE_COUNTS:
        times = []

        for run in range(RUNS_PER_CASE):
            elapsed = run_once(sphere_count)
            times.append(elapsed)
            print(f"[{sphere_count}] Run {run + 1}: {elapsed:.3f}s")

        avg = mean(times)
        total_objects = sphere_count + 1

        print(
            f"| {sphere_count} | {total_objects} | "
            f"{times[0]:.3f}s | {times[1]:.3f}s | {times[2]:.3f}s | "
            f"{avg:.3f}s |"
        )


if __name__ == "__main__":
    main()
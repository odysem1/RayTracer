#include <chrono>
#include <cstdlib>
#include <iostream>

#include "camera.h"
#include "scenes.h"
#include "BVH.h"

int main(int argc, char** argv) {
    int sphere_count = 100;

    if (argc >= 2) {
        sphere_count = std::atoi(argv[1]);
    }

    // World
    auto world = diffuse_benchmark_scene(sphere_count);

    // BVH acceleration
    world = hittable_list(make_shared<bvh_node>(world));

    // Camera
    camera cam;

    cam.aspect_ratio = 16.0 / 9.0;
    cam.image_width = 400;
    cam.samples_per_pixel = 10;
    cam.max_depth = 10;

    cam.vfov = 20;
    cam.lookfrom = point3(13, 2, 3);
    cam.lookat = point3(0, 0, 0);
    cam.vup = vec3(0, 1, 0);

    cam.defocus_angle = 0.0;
    cam.focus_dist = 10.0;

    auto start = std::chrono::high_resolution_clock::now();

    cam.render(world);

    auto end = std::chrono::high_resolution_clock::now();

    auto elapsed = std::chrono::duration_cast<std::chrono::milliseconds>(
        end - start
    );

    std::cerr << "SPHERES: " << sphere_count << "\n";
    std::cerr << "RENDER_TIME_SECONDS: "
              << elapsed.count() / 1000.0
              << "\n";

    return 0;
}
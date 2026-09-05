#include <iostream>

#include "camera.h"
#include "scenes.h"
#include "BVH.h"

int main() {

    // World list:
    // 1. bouncing_spheres()
    // 2. checkered_spheres()
    // 3. earth()
    // 4. perlin_spheres()

    auto world = perlin_spheres();

    // BVH acceleration
    world = hittable_list(make_shared<bvh_node>(world));

    // Camera
    camera cam;

    cam.aspect_ratio = 16.0 / 9.0;
    cam.image_width = 400;
    cam.samples_per_pixel = 100;
    cam.max_depth = 50;

    cam.vfov = 20;
    cam.lookfrom = point3(13, 2, 3);
    cam.lookat = point3(0, 0, 0);
    cam.vup = vec3(0, 1, 0);

    cam.defocus_angle = 0.0;
    cam.focus_dist = 10.0;

    cam.render(world);

    return 0;
}
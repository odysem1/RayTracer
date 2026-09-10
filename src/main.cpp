#include <iostream>

#include "rtweekend.h"
#include "scenes.h"
#include "scene_cameras.h"
#include "BVH.h"


int main() {

    // World list:
    // 1. bouncing_spheres()
    // 2. checkered_spheres()
    // 3. earth()
    // 4. perlin_spheres()
    // 5. quads()
    // 6. simple_light()
    // 7. cornell_box()

    auto world = cornell_box();

    // BVH acceleration
    world = hittable_list(make_shared<bvh_node>(world));

    // Camera list:
    // 1. main_camera()
    // 2. quad_camera()
    // 3. light_camera()
    // 4. cornell_camera()

    camera cam = cornell_camera();

    cam.render(world);

    return 0;
}
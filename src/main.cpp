#include <iostream>

#include "rtweekend.h"
#include "scenes.h"
#include "scene_cameras.h"


int main() {

    // World list:
    // 1. bouncing_spheres()
    // 2. checkered_spheres()
    // 3. earth()
    // 4. perlin_spheres()
    // 5. quads()
    // 6. simple_light()
    // 7. cornell_box()
    // 8. cornell_smoke()
    // 9. final_scene_TNW()

    auto world = final_scene_TNW();

    // Camera list:
    // 1. main_camera()
    // 2. quad_camera()
    // 3. light_camera()
    // 4. cornell_camera()
    // 5. final_camera_TNW(int image_width, int samples_per_pixel, int max_depth)

    camera cam = final_camera_TNW(800, 10000, 40);

    cam.render(world);

    return 0;
}
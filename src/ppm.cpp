#include <iostream>
#include <format>

int main(){
    int image_width = 256;
    int image_height = 256;

    std::cout << std::format("P3\n{} {}\n255\n", image_width, image_height);

    for (int j = 0; j < image_height; j++){
        std::clog << "\rScanlines remaining: " << (image_height - j)<< " " << std::flush;
        for (int i = 0; i < image_width; i++){
            auto r = double(i) / (image_width - 1);
            auto g = double(j) / (image_height - 1);
            auto b = 0.0;

            int ir = int(255.999 * r);
            int ig = int(255.999 * g);
            int ib = int(255.999 * b);
            std::cout << std::format("{} {} {}\n", ir, ig, ib);
        }
    }
    std::clog << "\rDone.             \n";

}
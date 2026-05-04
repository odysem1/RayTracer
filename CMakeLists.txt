cmake_minimum_required(VERSION 3.20)

project(RayTracer LANGUAGES CXX)

add_executable(raytracer
    src/ppm.cpp
)

target_compile_features(raytracer PRIVATE cxx_std_20)

target_include_directories(raytracer PRIVATE
    ${PROJECT_SOURCE_DIR}/include
)
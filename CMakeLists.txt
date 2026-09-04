cmake_minimum_required(VERSION 3.20)

project(RayTracer LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

add_executable(raytracer
    src/main.cpp
)

target_compile_features(raytracer PRIVATE cxx_std_20)

target_include_directories(raytracer PRIVATE
    ${PROJECT_SOURCE_DIR}/include
)
# RayTracer

C++로 직접 구현하는 CPU 기반 Ray tracing 학습 프로젝트입니다.

## Project info

Ray tracing의 핵심 구성 요소를 직접 구현하며 렌더링의 기본 원리를 이해하기 위해 노력했습니다.

Language: C++

개발 기간: 2026.05.04 ~

## Status

- Ray tracing 개념 학습 중

## Goals

### Phase 1: RTIOW
- [x] PPM image output
- [x] Vec3 class
- [x] Ray class
- [x] Background gradient rendering
- [x] Sphere-ray intersection
- [x] Surface normal visualization
- [X] Camera
- [X] Anti-aliasing
- [X] Diffuse material
- [X] Metal material
- [X] Dielectric material
- [X] Defocus blur
- [X] Final scene Rendering

### Phase 2: The next week

- [x] Defocus Blur
- [x] Bounding Volume Hierarchies
- [x] Texture mapping
- [x] Perlin noise
- [x] Quadrilaterals
- [x] Lights
- [x] Instances 
- [x] Volumes
- [x] Final scene

### Phase 2: The rest of your life

- [x] Stratified Samplig(Jittering)
- [ ] One Dimensional Monte Carlo Integration

## BVH efficiency measurement

### Before BVH

| Small Spheres | Total Objects | Run 1 | Run 2 | Run 3 | Avg |
| --: | --: | --: | --: | --: | --: |
| 100 | 101 | 17.175s | 14.576s | 14.366s | 15.372s |
| 200 | 201 | 26.454s | 26.543s | 26.740s | 26.579s |
| 500 | 501 | 62.637s | 60.111s | 60.007s | 60.918s |
| 1000 | 1001 | 117.167s | 117.447s | 118.706s | 117.773s |

### After BVH

| Small Spheres | Total Objects | Run 1 | Run 2 | Run 3 | Avg |
| --: | --: | --: | --: | --: | --: |
| 100 | 101 | 6.242s | 5.238s | 5.478s | 5.653s |
| 200 | 201 | 6.272s | 6.146s | 6.286s | 6.235s |
| 500 | 501 | 9.228s | 9.085s | 9.224s | 9.179s |
| 1000 | 1001 | 11.589s | 11.242s | 11.269s | 11.367s |

### Overall

| Small Spheres | Total Objects | Before BVH | With BVH | Speedup x |
| --: | --: | --: | --: | --: |
| 100 | 101 | 15.372s | 5.653s | 2.719x |
| 200 | 201 | 26.579s | 6.235s | 4.263x |
| 500 | 501 | 60.918s | 9.179s | 6.637x |
| 1000 | 1001 | 117.773s | 11.367s | 10.361x |

## Reference

- Ray Tracing in One Weekend: https://raytracing.github.io

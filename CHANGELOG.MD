# Changelog

## [0.1] - Initializing

ppm output 테스트 파일 및 기초적인 벡터 헤더파일 추가

### Added

`ppm.cpp`: ppm 이미지 output 테스트를 위한 파일

`CMakeLists.txt`: Make파일 및 executable 파일 생성을 위한 파일(현재는 ppm test 이미지만 생성하면 되므로 raytracer executable을 ppm.cpp 파일을 빌드해서 만듬)

`vec3.h`: 기초적인 3차원 벡터 클래스 및 벡터 연산 함수를 구현함

---

## [0.1.1] - Initializing_ray

color 헤더파일의 write_color 함수 및 ray class 추가

### Added

`color.h`: write_color 함수로 RGB 값을 PPM 이미지 파일 형식에 맞게 출력해줌

`ray.h`: 기초적인 ray 클래스 추가(원점 + 3차원 벡터)

---

## [0.1.2] - Camera and viewport setup

카메라를 기준으로 viewport 평면을 3D 공간에 배치 후, 각 픽셀 좌표에 대응되는 3D 위치를 계산하는 코드를 구현함

### Added
`main.cpp - ray_color`: 픽셀의 위치에 따라 RGB 값이 달라지는 gradient 이미지 색을 생성함

### Changed

`main.cpp - main`: camera와 viewport, pixel 좌표에 해당하는 변수 추가, 카메라에서 각 픽셀을 향하는 ray 구현

---

## [0.1.3] - Sphere test: color rendering based on normal vector

화면에 구를 렌더링하는 코드 구현

### Added

`main.cpp - hit_sphere`: ray-sphere intersection을 이차방정식의 판별식을 이용해 계산함

### Changed

`main.cpp - ray_color`: Sphere에 닿는 경우, Normal vector의 방향에 따라 픽셀을 색칠함

---

## [0.1.4] - Hittable objects, utility functions

여러 ray hittable objects를 화면에 렌더링할 수 있도록 scene 구조를 분리함

`hittable`, `sphere`, `hittable_list` 를 추라하고 공통 유틸리티 헤더를 정리함

### Added

`hittable.h, sphere.h`: ray와 교차 가능한 object의 공통 인터페이스를 정의함, hittable을 상속하는 sphere class를 구현함

`hittable_list.h`: 여러 hittable object를 저장하고 가장 가까운 hit를 찾도록 구현함

`rtweekend.h, interval.h`: 범용 상수와 함수, ray parameter 범위를 정의함

### Changed

`main.cpp - main`: hittable_list를 이용해 구 2개를 렌더링하도록 변경하고, hit 정보를 sphere class를 사용하도록 구현함

---

## [0.1.5] - camera class

기존 main.cpp의 main 함수와 write_color 함수에 구현되어 있던 카메라 기능을 별도의 헤더파일에 클래스로 작성함

### Added

`camera.h`: 카메라 initialize와 화면 픽셀 색칠 기능 이동

### Changed

`main.cpp`: write_color 함수 삭제 및 main 단순화

---

## [0.1.6] - Antialising

random double을 만드는 함수를 이용해 Antialising 기능을 구현함

### Added

`rtweekend.h - random_double`: 0과 1 사이 또는 min과 max 사이의 랜덤한 double을 리턴하는 함수

`camera.get_ray, sample_square`: 픽셀 사각형 내부의 점 하나에 쏜 랜덤한 ray를 생성함

### Changed

`camera.render`: get_ray에서 리턴한 ray samples_per_pixel개(기본 10개, main.cpp에서 100개로 정의함)의 색 평균으로 픽셀을 색칠함

---

## [0.1.7] - Reflection and gamma correction

Lambert distribution에 따라 빛의 reflection을 구현함

### Added

`vec3.h - random_unit_vector`: 랜덤한 unit vector를 생성하는 함수

`color.h - linear_to_gamma`: 물체의 밝기 차이가 빛 흡수도에 따라 너무 크게 변하지 않도록 자연스럽게 보정해주는 함수

### Changed

`camera.ray_color`: hit 지점에서 새로운 scattered ray를 Lambertian distribution에 따른 랜덤 방향으로 쏘고, 그 결과를 재귀적으로 계산하도록 변경함

`interval(0.001, infinity)` 를 사용해 새 ray가 방금 맞은 표면에 다시 hit하는 self-intersection 문제를 줄임

---

## [0.1.8] - Materials: metal

Material class를 크게 정의하고 그 안에 lambertian 물체와 metal 재질 물체가 그 class를 상속하도록 해서 코드를 리팩터링함

### Added

`material.h`: 물체의 재질을 표현하는 class들의 헤더파일

`vec3.h - reflect`: 반사된 ray의 방향 리턴하는 함수

### Changed

`sphere.h, hittable.h`: hittable object(sphere)와 hit_record가 material 변수를 포함하도록 변경

`camera.h - ray_color`: ray_color에서 scatterd ray를 구하는 부분을 달라진 구조에 맞춰서 변경

---

## [0.1.9] - Materials: dielectrics

### Added

`material.h - dielectric`: dielectric 물체를 class로 구현

`vec3.h - refract`: 빛의 굴절을 계산하는 함수

---

## [0.1.10] - Movable camera

기존 원점 고정 카메라를 일반화해, 카메라 위치와 바라보는 지점에 따라 scene을 렌더링할 수 있도록 구현함

### Added

`camera.h - lookfrom, lookat, vup`: 카메라 위치, 바라보는 지점, 화면 위쪽 방향 설정 변수 추가

`camera.h - vfov`: 세로 시야각을 이용한 viewport 크기 계산 기능 추가

### Changed

`camera.h`: 기존 world 좌표축 기준 viewport 배치를 camera basis vector(`u`, `v`, `w`) 기반으로 계산하도록 변경

`main.cpp`: movable camera 설정값을 사용해 렌더링하도록 변경

---

## [0.1.11] - Defocus blur & final render

Pinhole camera 대신 lens 기반 카메라 원리를 적용해 focus 밖의 물체에 blur 효과가 나타나도록 변경

### Added

`vec3.h - random_in_unit_disk`: 원 안의 랜덤한 점을 하나 고르는 함수

`camera.h - focus_dist, defocus_angle`: 렌즈의 초점거리와 렌즈 반지름을 결정하는 각도를 추가함

`camera.h - defocus_disk_sample`: 렌즈 위의 랜덤한 점을 return하는 함수

### Changed

`camera.h`: focal_length를 전부 focus_dist로 바꾸고 가상의 렌즈 원반 위의 랜덤한 점에서 빛을 쏘도록 알고리즘을 변경함

`main.c`: 렌더링할 scene을 변경함 - 많은 구형 물체와 3개의 중심 구

---

## [0.2.1] - Motion blur

움직이는 구를 구현하기 위해 object에 time 및 속도 정보를 추가, ray에도 추가

### Changed

`ray.h`: ray class에 time 정보 추가

`material.h, sphere.h`: 시간에 따라 움직이는 구의 경우, 중심이 이동되는 것을 고려함

`camera.h - get_ray`: 렌더링할 장면의 시간을 고려하기 위해 return하는 ray에 time 정보 추가

## [0.2.2] - AABB and BVH, Scene test

AABB를 통한 Bounded volume hierachies 구현을 위해 AABB.h, BVH.h 추가 및 BVH 성능 테스트를 위해 Scene 구현 분리

### Added

`AABB.h, BVH.h`: 축에 평행한 box와 bounded volume tree class를 구현함

`scenes.h`: BVH 성능 비교를 위해 world 구현 부분을 분리함

`interval.h` : 패딩을 더한 expand 함수와 두 interval 중 교차하는 부분을 구하는 생성자 구현

`sphere.h, hittable.h, hittable_list.h`: 각각의 object를 둘러싸는 aabb 정보 추가

`rtweekend.h`: random_int 함수 추가

## [0.2.2a] - BVH benchmark

### Added

`build/benchmark.py`: BVH가 얼마나 렌더링 성능을 향상시키는지 측정하기 위한 python 파일

### Changed

`AABB.h`: hit 함수에서 ray_t.max를 줄여야 하는 곳에 ray_t.min을 대입하고 있는 오타 수정

## [0.2.3] - Texture mapping

Texture interface를 추가하고, object 표면 좌표를 이용해 procedural texture와 image texture를 적용할 수 있도록 구현함

### Added

`texture.h`: texture의 공통 인터페이스와 `solid_color`, `checker_texture`, `image_texture` 클래스 추가

`sphere.h`: sphere 표면의 hit point를 UV 좌표로 변환하는 기능 추가

`rtw_stb_image.h, stb_image.h`: 이미지 파일을 불러와 texture로 사용할 수 있도록 image loading helper 추가

`scenes.h`: checker texture scene과 earth image texture scene 추가

### Changed

`material.h`: lambertian material이 단일 color 값 대신 texture의 `value(u, v, p)` 결과를 albedo로 사용하도록 변경






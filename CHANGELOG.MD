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
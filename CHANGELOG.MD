# Changelog

## v[0.1] - Initializing

ppm output 테스트 파일 및 기초적인 벡터 헤더파일 추가

### Added

`ppm.cpp`: ppm 이미지 output 테스트를 위한 파일

`CMakeLists.txt`: Make파일 및 executable 파일 생성을 위한 파일(현재는 ppm test 이미지만 생성하면 되므로 raytracer executable을 ppm.cpp 파일을 빌드해서 만듬)

`vec3.h`: 기초적인 3차원 벡터 클래스 및 벡터 연산 함수를 구현함

## v[0.1.1] - Initializing_ray

color 헤더파일의 write_color 함수 및 ray class 추가

### Added

`color.h`: write_color 함수로 RGB 값을 PPM 이미지 파일 형식에 맞게 출력해줌

`ray.h`: 기초적인 ray 클래스 추가(원점 + 3차원 벡터)

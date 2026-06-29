CXX := g++
CXXFLAGS := -std=c++20 -O3 -Wall -Wextra -Iinclude

SRC_DIR := src
BUILD_DIR := build
TARGET := $(BUILD_DIR)/raytracer

SRCS := $(wildcard $(SRC_DIR)/*.cpp)
OBJS := $(patsubst $(SRC_DIR)/%.cpp,$(BUILD_DIR)/%.o,$(SRCS))

.PHONY: all run benchmark clean rebuild

all: $(TARGET)

$(TARGET): $(OBJS)
	@mkdir -p $(BUILD_DIR)
	$(CXX) $(CXXFLAGS) $^ -o $@

$(BUILD_DIR)/%.o: $(SRC_DIR)/%.cpp
	@mkdir -p $(BUILD_DIR)
	$(CXX) $(CXXFLAGS) -I$(SRC_DIR) -c $< -o $@

run: $(TARGET)
	$(TARGET) > output.ppm

benchmark: $(TARGET)
	python3 tools/benchmark.py

clean:
	rm -rf $(BUILD_DIR) output.ppm benchmark_*.ppm

rebuild: clean all
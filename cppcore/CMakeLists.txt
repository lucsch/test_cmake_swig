cmake_minimum_required(VERSION 3.10)

# set the project name
project(ctestapp)

# add the library
add_subdirectory(modfact)

# add the executable
add_executable(${PROJECT_NAME} app/main.cpp)

target_link_libraries(${PROJECT_NAME} PUBLIC modfact)
target_include_directories(${PROJECT_NAME} PUBLIC "${PROJECT_SOURCE_DIR}/modfact/src")

# add the swig directory
add_subdirectory(swig)

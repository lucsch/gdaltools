cmake_minimum_required(VERSION 3.10)
project(gdal_translate)

# cmake magical command for conan
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(KEEP_RPATHS)
message(STATUS "CMAKE_SKIP_RPATH: ${CMAKE_SKIP_RPATH}")

if (APPLE)
	set(CMAKE_INSTALL_RPATH "@executable_path")
else()
	set(CMAKE_INSTALL_RPATH "$ORIGIN")
endif()

# using git version
set(${PROJECT_NAME}_MAJOR_VERSION "3")
set(${PROJECT_NAME}_MINOR_VERSION "5")

if (UNIX)
    add_definitions(-std=c++17)
endif (UNIX)

include_directories("src")
add_executable(${PROJECT_NAME}
		"src/gdal_translate_bin.cpp"
		"src/commonutils.cpp")
target_link_libraries(${PROJECT_NAME} ${CONAN_LIBS})

set(CMAKE_INSTALL_PREFIX "${CMAKE_BINARY_DIR}")
message(STATUS "CMAKE_INSTALL_PREFIX: ${CMAKE_INSTALL_PREFIX}")
install(TARGETS ${PROJECT_NAME})




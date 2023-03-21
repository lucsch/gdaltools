cmake_minimum_required(VERSION 3.0)
project(gdal_translate)

# cmake magical command for conan
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

# using git version
set(${PROJECT_NAME}_MAJOR_VERSION "3")
set(${PROJECT_NAME}_MINOR_VERSION "5")

if (UNIX)
    add_definitions(-std=c++11)
endif (UNIX)

include_directories("src")
add_executable(${PROJECT_NAME} 
		"src/gdal_translate_bin.cpp"
		"src/commonutils.cpp")
target_link_libraries(${PROJECT_NAME} ${CONAN_LIBS})

install(TARGETS ${PROJECT_NAME}
		RUNTIME DESTINATION bin
		LIBRARY DESTINATION bin
		BUNDLE DESTINATION .)

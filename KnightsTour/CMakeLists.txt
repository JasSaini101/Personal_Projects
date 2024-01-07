cmake_minimum_required(VERSION 3.26)
project(KnightsTour2)

set(CMAKE_CXX_STANDARD 17)

add_executable(KnightsTour2 main.cpp
        Board.h
        algorithms.h
)

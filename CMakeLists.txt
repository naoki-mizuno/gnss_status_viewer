cmake_minimum_required(VERSION 2.8.3)
project(gnss_status_viewer)

find_package(catkin REQUIRED)

catkin_package()

catkin_install_python(PROGRAMS
    nodes/gnss_status_viewer.py
    DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

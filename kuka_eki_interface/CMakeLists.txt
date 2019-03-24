cmake_minimum_required(VERSION 2.8.3)
project(kuka_eki_interface)

find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
  sensor_msgs
  geometry_msgs
)

catkin_python_setup()

catkin_package(
)

install(PROGRAMS
   scripts/eki_sim
   nodes/eki_node
   DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
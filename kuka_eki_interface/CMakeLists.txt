cmake_minimum_required(VERSION 2.8.3)
project(kuka_eki_interface)

find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
  sensor_msgs
  geometry_msgs
)

catkin_python_setup()

catkin_package()

catkin_install_python(PROGRAMS
   nodes/kuka_eki_interface_node
   nodes/kuka_eki_state_publisher
   DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
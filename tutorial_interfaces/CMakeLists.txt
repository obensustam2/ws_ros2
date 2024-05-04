cmake_minimum_required(VERSION 3.8)
project(tutorial_interfaces)

find_package(geometry_msgs REQUIRED)
find_package(rosidl_default_generators REQUIRED)

rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/Num.msg"
  "msg/Sphere.msg"
  "srv/AddThreeInts.srv"
  "srv/GoHome.srv"
  "srv/Stop.srv"
  "srv/Start.srv"
  "srv/StartNew.srv"
  DEPENDENCIES geometry_msgs 
  )

ament_package()

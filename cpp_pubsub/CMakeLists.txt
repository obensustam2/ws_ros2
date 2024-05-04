cmake_minimum_required(VERSION 3.8)
project(cpp_pubsub)

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)
find_package(tutorial_interfaces REQUIRED) # Added for custom msg 

add_executable(talker src/publisher_member_function.cpp)
ament_target_dependencies(talker rclcpp std_msgs)

add_executable(listener src/subscriber_member_function.cpp)
ament_target_dependencies(listener rclcpp std_msgs)

add_executable(custom_msg_pub src/custom_msg_pub.cpp)
ament_target_dependencies(custom_msg_pub rclcpp tutorial_interfaces)

add_executable(custom_msg_sub src/custom_msg_sub.cpp)
ament_target_dependencies(custom_msg_sub rclcpp tutorial_interfaces)

install(TARGETS
  talker
  listener
  custom_msg_pub
  custom_msg_sub
  DESTINATION lib/${PROJECT_NAME})

  # Needed for launch file
install(
  DIRECTORY launch
  DESTINATION share/${PROJECT_NAME}
)
ament_package()

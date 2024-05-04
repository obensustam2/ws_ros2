cmake_minimum_required(VERSION 3.8)
project(cpp_srvcli)

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(example_interfaces REQUIRED)
find_package(tutorial_interfaces REQUIRED) # Added for custom srv 

add_executable(server src/add_two_ints_server.cpp)
ament_target_dependencies(server rclcpp example_interfaces)

add_executable(client src/add_two_ints_client.cpp)
ament_target_dependencies(client rclcpp example_interfaces)

add_executable(custom_server src/custom_srv_server.cpp)
ament_target_dependencies(custom_server rclcpp tutorial_interfaces)

add_executable(custom_client src/custom_srv_client.cpp)
ament_target_dependencies(custom_client rclcpp tutorial_interfaces)

install(TARGETS
    server
    client
    custom_server
    custom_client
    DESTINATION lib/${PROJECT_NAME})

ament_package()

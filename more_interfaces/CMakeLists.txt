cmake_minimum_required(VERSION 3.8)
project(more_interfaces)

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)
find_package(rosidl_default_generators REQUIRED)

add_executable(pub_book src/publish_address_book.cpp)
ament_target_dependencies(pub_book rclcpp std_msgs rosidl_default_generators)

install(TARGETS
  pub_book
  DESTINATION lib/${PROJECT_NAME})


# Custom message and service setup
set(msg_files
  "msg/AddressBook.msg")

set(srv_files)

rosidl_generate_interfaces(${PROJECT_NAME}
  ${msg_files}
  ${srv_files})


# In order to use the messages generated in the same package we need to use the following CMake code
rosidl_get_typesupport_target(cpp_typesupport_target
  ${PROJECT_NAME} rosidl_typesupport_cpp)

target_link_libraries(pub_book "${cpp_typesupport_target}")


ament_export_dependencies(rosidl_default_runtime)

ament_package()

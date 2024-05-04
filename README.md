# Packages

## action_tutorials_cpp 
package contains cpp action server and client nodes by using **Fibonacci.action** (from **action_tutorials_interfaces** package).

## action_tutorials_interfaces
package contains **Fibonacci.action**. **rosidl_interface_packages**  was added as dependecy

## action_tutorials_py
package contains python action server and client nodes by using **Fibonacci.action** (from **action_tutorials_interfaces** package).

## cpp_parameter_event_handler
package that checks parameter value updates.

## cpp_parameters
package contains a cpp node which sends **Log** messages with parameter value.

## cpp_pubsub
package contains nodes communicate via topics by using String and custom message(msg from **tutorial_interface** package).

## cpp_srvcli
package contains cpp nodes which use service. 2 integer summation (srv from **example_interfaces** package) and 3 integer summation (srv from **tutorial_interfaces** package). 

## launch_tutorial
package contains launch files. 

## more_interfaces
package includes custom message. For this purpose **rosidl_interface_packages**  was added as dependecy. A node in this package uses this message. Therefore, adjustments are done at CMakeLists.txt file about **rosidl**

## polygon_base
Plugin packages

## polygon_plugins
Plugin packages

## py_parameters
package contains a python node which sends **Log** messages with parameter value.

## py_pubsub
package contains python nodes communicate via topics by using String and custom message(msg from **tutorial_interfaces** package).

- ros2 run py_parameters minimal_param_node --ros-args -p param_planet_name:=Yuy

## py_srvcli
package contains python nodes which use service. 2 integer summation (srv from **example_interfaces** package) and 3 integer summation (srv from **tutorial_interfaces** package). 

## tutorial_interfaces
package includes custom message and service. For this purpose **rosidl_interface_packages**  was added as dependecy. However, there is no node here. 








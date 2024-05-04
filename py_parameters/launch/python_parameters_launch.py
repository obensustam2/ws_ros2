from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration

def generate_launch_description():

    declare_planet_name_arg = DeclareLaunchArgument(
    name='planet_name', 
    default_value='Merkür', 
    description='Name of the planet')

    planet_name_launch_config = LaunchConfiguration('planet_name')
    
    param_node = Node(
        package='py_parameters',
        executable='minimal_param_node',
        name='minimal_param_node',
        output='screen',
        emulate_tty=True,
        parameters=[
            {'param_planet_name': planet_name_launch_config}
        ]
    )
    return LaunchDescription([
        declare_planet_name_arg,
        param_node
    ])
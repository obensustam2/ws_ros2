import launch
import launch_ros.actions

def generate_launch_description():
    return launch.LaunchDescription([
        launch_ros.actions.Node(
            package='py_pubsub',
            executable='custom_msg_pub_py',
            name='custom_msg_pub')
    ])
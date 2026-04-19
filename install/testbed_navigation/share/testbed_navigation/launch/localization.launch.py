from launch import LaunchDescription
from launch_ros.actions import Node
import os

def generate_launch_description():

    amcl_config = os.path.join(
        os.getenv('HOME'),
        'assignment_ws/src/testbed_navigation/config/amcl_params.yaml'
    )

    return LaunchDescription([

        Node(
            package='nav2_amcl',
            executable='amcl',
            name='amcl',
            output='screen',
            parameters=[amcl_config]
        ),

        Node(
            package='nav2_lifecycle_manager',
            executable='lifecycle_manager',
            name='lifecycle_manager_localization',
            output='screen',
            parameters=[{
                'use_sim_time': True,
                'autostart': True,
                'node_names': ['amcl']
            }]
        )

    ])
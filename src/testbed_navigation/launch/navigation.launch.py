from launch import LaunchDescription
from launch_ros.actions import Node
import os

def generate_launch_description():

    nav2_config = os.path.join(
        os.getenv('HOME'),
        'assignment_ws/src/testbed_navigation/config/nav2_params.yaml'
    )

    common_params = [nav2_config, {'use_sim_time': True}]

    return LaunchDescription([

        Node(
            package='nav2_planner',
            executable='planner_server',
            name='planner_server',
            output='screen',
            parameters=common_params
        ),

        Node(
            package='nav2_controller',
            executable='controller_server',
            name='controller_server',
            output='screen',
            parameters=common_params
        ),

        Node(
            package='nav2_bt_navigator',
            executable='bt_navigator',
            name='bt_navigator',
            output='screen',
            parameters=common_params
        ),

        Node(
            package='nav2_behaviors',
            executable='behavior_server',
            name='behavior_server',
            output='screen',
            parameters=common_params
        ),

        Node(
            package='nav2_lifecycle_manager',
            executable='lifecycle_manager',
            name='lifecycle_manager_navigation',
            output='screen',
            parameters=[{
                'use_sim_time': True,
                'autostart': True,
                'node_names': [
                    'planner_server',
                    'controller_server',
                    'bt_navigator',
                    'behavior_server'
                ]
            }]
        )

    ])
import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration, Command
from launch_ros.actions import Node
from launch_ros.descriptions import ParameterValue

def generate_launch_description():

    use_sim_time = LaunchConfiguration('use_sim_time', default='false')
    urdf_file_name = 'PSM1.urdf.xacro'
    urdf = os.path.join(
        get_package_share_directory('dvrk_model'),
        urdf_file_name)

    return LaunchDescription([
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='false'),
            #description='Use simulation (Gazebo) clock if true'),
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            remappings=[
                ("/joint_states", "/PSM1/measured_js"),
                ("/joint_states", "/PSM1/jaw/measured_js")],
            parameters=[{'use_sim_time': use_sim_time,
                         'robot_description': ParameterValue(
                             Command(['xacro ', str(urdf)]), value_type=str)}],
            arguments=[urdf])
        # ,
        # Node(
        #     package='dvrk_model',
        #     executable='joint_state_publisher',
        #     name='joint_state_publisher',
        #     output='screen'),
    ])

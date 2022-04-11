import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess
from launch.substitutions import LaunchConfiguration, Command
from launch_ros.actions import Node
from launch_ros.descriptions import ParameterValue

def generate_launch_description():

    use_sim_time = LaunchConfiguration('use_sim_time', default='false')
    arm = LaunchConfiguration('arm')

    # urdf_file_name = LaunchConfiguration('arm') + '.urdf.xacro'
    urdf_file_name = 'PSM1' + '.urdf.xacro'
    urdf = os.path.join(get_package_share_directory('dvrk_model'),
                        'model',
                        urdf_file_name)

    return LaunchDescription([
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='false',
            description='Use simulation (Gazebo) clock if true'),
        DeclareLaunchArgument(
            'arm',
             description='arm name (i.e. PSM1, PSM2...)'),
        ExecuteProcess(
            cmd=['arm_name=',arm]),
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            remappings=[
                ('/joint_states', '/' + arm_name + '/measured_js')],
#                 ('/joint_states', '/' + ParameterValue(arm, value_type=str) + '/jaw/measured_js')], # this is not working, used to be source_list in ROS1
            parameters=[{'use_sim_time': use_sim_time,
                         'robot_description': ParameterValue(
                             Command(['xacro ', str(urdf)]), value_type=str)}],
            arguments=[urdf])
    ])

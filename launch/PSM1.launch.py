import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess
from launch.substitutions import LaunchConfiguration, Command
from launch_ros.actions import Node
from launch_ros.descriptions import ParameterValue

def generate_launch_description():

    use_sim_time = LaunchConfiguration('use_sim_time', default='false')
    rate = LaunchConfiguration('rate', default=50.0)  # Hz, default is 10 so we're increasing that a bit.  Funny enough joint and robot state publishers don't have the same name for that parameter :-(

    # we really need to add a parameter for the arm name
    urdf_file_name = 'PSM1.urdf.xacro'
    urdf = os.path.join(get_package_share_directory('dvrk_model'),
                        'model',
                        urdf_file_name)

    joint_state_publisher_node = Node(
        package='joint_state_publisher',
        executable='joint_state_publisher',
        name='joint_state_publisher',
        namespace='PSM1',
        output='screen',
        parameters=[{'use_sim_time': use_sim_time,
                     'source_list': ['measured_js', 'jaw/measured_js'],
                     'rate': rate
        }]
    )

    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        namespace='PSM1',
        output='screen',
        parameters=[{'use_sim_time': use_sim_time,
                     'robot_description': ParameterValue(
                         Command(['xacro ', str(urdf)]), value_type=str),
                     'publish_frequency': rate
        }],
        arguments=[urdf]
    )

    return LaunchDescription([
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='false',
            description='Use simulation (Gazebo) clock if true'),
        robot_state_publisher_node,
        joint_state_publisher_node,
    ])

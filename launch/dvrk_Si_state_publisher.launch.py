from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from launch_ros.parameter_descriptions import ParameterValue

from launch import LaunchContext, LaunchDescription, Substitution
from typing import Text


from launch.substitutions import (
    Command,
    FindExecutable,
    LaunchConfiguration,
    PathJoinSubstitution,
)

# Create a list of ROS topics that will provide all the joint states
# from the dVRK main node to the joint_state_publisher
class ArmSourceListSubstitution(Substitution):
    """Generate source list for a given arm"""

    def __init__(self, arm_name: LaunchConfiguration):
        super().__init__()
        self.__arm_name = arm_name

    def describe(self) -> Text:
        return 'ArmSourceList({})'.format(self.__arm_name.describe())

    def perform(self, context: LaunchContext) -> Text:
        arm_name = self.__arm_name.perform(context)
        source_list = ['measured_js']
        if arm_name.startswith('PSM'):
            source_list.append('jaw/measured_js')
        elif arm_name.startswith('MTM'):
            source_list.append('gripper/measured_js')

        # launch_ros parses values from yaml, so source list needs to be yaml
        sources = ','.join(source for source in source_list)
        yaml =  '[{}]'.format(sources)
        return yaml


def generate_launch_description():
    arm_name = LaunchConfiguration('arm')
    use_sim_time = LaunchConfiguration('use_sim_time', default = 'false')
    rate = LaunchConfiguration('rate', default = 50.0)  # Hz, default is 10 so we're increasing that a bit.  Funny enough joint and robot state publishers don't have the same name for that parameter :-(
    #start_joint_state_publisher=LaunchConfiguration('start_joint_state_publisher',default='true')

    robot_model_default = [
        PathJoinSubstitution([FindPackageShare('dvrk_model'), 'model', 'Si','']),
        'dvrk_si',
        '.urdf.xacro',
    ]

    rviz_config_file = PathJoinSubstitution(
        [FindPackageShare('dvrk_model'), "rviz", "Si.rviz"]
    )

    # Use xacro to process robot model at substitution time
    # Can't happen until substitution time when we know robot_model
    robot_description = ParameterValue(
        Command(
            [FindExecutable(name = 'xacro'), ' ', *robot_model_default]
        ),
        value_type = str,
    )

    # Declare nodes
    joint_state_publisher_node = Node(
        package = 'joint_state_publisher',
        executable = 'joint_state_publisher',
        name = 'joint_state_publisher',
        parameters = [{'use_sim_time': use_sim_time,
                       'rate': rate}],
    )

    robot_state_publisher_node = Node(
        package = 'robot_state_publisher',
        executable = 'robot_state_publisher',
        name = 'robot_state_publisher',
        parameters = [{'use_sim_time': use_sim_time,
                       'robot_description': robot_description,
                       'publish_frequency': rate}],
        output="both",
    )
    
    rviz_node = Node(
        package = 'rviz2',
        executable = 'rviz2',
        name = 'rviz2',
	arguments=["-d", rviz_config_file],
        output="both",
    )

    ld = LaunchDescription([
                joint_state_publisher_node,
                robot_state_publisher_node,
                rviz_node,
            ])

    return ld

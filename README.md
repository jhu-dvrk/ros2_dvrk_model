# dVRK Description

This code is written to launch a ros node with the urdf robot
description as a parameter. It is based on this tutorial:
https://docs.ros.org/en/galactic/Tutorials/URDF/Using-URDF-with-Robot-State-Publisher.html

It provides launch files to bringup with the robot with a controller using the ros_control package.

# dVRK models

This code is written to launch a ros node with the urdf robot
description as a parameter.

See also: https://github.com/jhu-dvrk/sawIntuitiveResearchKit/wiki/BuildROS2

It provides launch files to bringup with the robot with a controller using the ros_control package.
# Compilation

1. Create a ros2 workspace with the src code inside
2. Run the following in the workspace:
```sh
colcon build --packages-select dvrk_model
```

#  Requirements

xacro is not installed by default on ROS 2 (at least with Galactic):
```sh
# don't forget to source after first compilation
source install/setup.bash
# launch script with robot state publisher and our python script to animate the Omni
ros2 launch dvrk_mode dvrk_state_publisher.launch.py
# to visualize the Omni in rviz...
rviz2 -d ~/<workspace_name>/install/dvrk_model/share/dvrk_model/dvrk.rviz # to launch rviz with the omni frames
=======
sudo apt install ros-galactic-xacro
```

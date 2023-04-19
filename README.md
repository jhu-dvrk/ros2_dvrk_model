# dVRK models

This code is written to launch a ros node with the urdf robot
description as a parameter.

See also: https://github.com/jhu-dvrk/sawIntuitiveResearchKit/wiki/BuildROS2

# Compilation

1. Create a ros2 workspace with the src code inside
2. Run the following in the workspace:
```sh
colcon build
```

#  Requirements

xacro is not installed by default on ROS 2 (at least with Galactic):
```sh
sudo apt install ros-galactic-xacro
```

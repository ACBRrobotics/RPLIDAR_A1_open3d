# RPLIDAR_A1_open3d
A simple Python script integrating the RPLIDAR A1 LiDAR with the open3d point cloud library.  The live LiDAR data is read and visualized in an open3d window.  The point cloud data is then analyzed to find the point in the point cloud nearest to the lidar, and its angle and distance from the LiDAR are measured.

This script has been tested in both Linux and Windows environments.  

To install the dependencies open a terminal and type: 

`$ pip install rplidar-roboticia`

`$ pip install open3d`

To make sure your LiDAR cane be accessed via serial, type:

`$ sudo usermod -a -G dialout <insert your username>`

Reboot your computer, and start playing around with your LiDAR point cloud data! Remember to change your COM port if you have more than one serial devices plugged into your computer, or are working in a windows environment

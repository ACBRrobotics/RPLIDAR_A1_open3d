# RPLIDAR_A1_open3d
A simple Python script integrating the RPLIDAR A1 LiDAR with the popular open3d point cloud library.  The live LiDAR data is read and visualized in an open3d window.  The point cloud data is then analyzed to find the point in the point cloud nearest to the lidar, and its angle and distance from the LiDAR are measured.

The RPLIDAR A1:

<img src="https://github.com/ACBRrobotics/RPLIDAR_A1_open3d/assets/60329456/6de532bc-83a3-4d76-8176-c9b38991d570" width="400" height="200">

Sample Program Output:

<img src="https://github.com/ACBRrobotics/RPLIDAR_A1_open3d/assets/60329456/60b4d4fa-b202-4bb1-a0ed-eef5b0f8ba59" width="200" height="200">
<img src="https://github.com/ACBRrobotics/RPLIDAR_A1_open3d/assets/60329456/bb58f3c7-d0fb-4e83-bea1-2c9476cb2493"  width="200" height="200">

This script has been tested in both Linux and Windows environments.  

To install the dependencies open a terminal and type: 

`$ pip install rplidar-roboticia`

`$ pip install open3d`

To make sure your LiDAR can be accessed via serial, be sure to type:

`$ sudo usermod -a -G dialout <insert your username>`

Reboot your computer, and start playing around with your LiDAR point cloud data! Remember to change your COM port if you have more than one serial device plugged into your computer, or are working in a Windows environment.

Additionally:  A robot chassis was designed for this project to facilitate further exploration of LiDAR data for more advanced robotics projects, the .DXF files necessary to edit or fabricate the robot chassis are located in this repository. 

<img src="https://github.com/ACBRrobotics/RPLIDAR_A1_open3d/assets/60329456/918dd350-42b0-45ef-9bd3-1d6bac734509" width="200" height="200">

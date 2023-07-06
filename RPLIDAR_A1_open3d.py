import open3d as o3d
from rplidar import RPLidar
import numpy as np
import time

# Callback function to process the lidar data as it comes in
def process_lidar_measurement(measurement):
    # Extract the angle and distance from the measurement
    angle = measurement[1]
    distance = measurement[2]

    # Convert polar coordinates to Cartesian coordinates 
    # we are assuming z=0 for our 2D RPLIDAR A1
    x = distance * np.cos(np.radians(angle))
    y = distance * np.sin(np.radians(angle))

    # Append the Cartesian coordinates to the lidar_data list
    lidar_data.append([x, y, 0])  # Assuming z=0 for a 2D lidar

# Create an instance of the RPLidar class
# Replace '/dev/ttyUSB0' with the serial port of your Rplidar A1
# On a Windows device it may look something like 'COM6'
lidar = RPLidar('COM6')  

# Initialize an empty list to store the lidar measurements
lidar_data = []

# Set the distance threshold for the warning system
warning_distance = 0.5  # This value can be adjusted as needed

# Start scanning with the RPLIDAR A1
lidar.start_motor()
lidar.connect()

# Add delay to allow the device to initialize safely
time.sleep(2)

# Create an Open3D visualizer
visualizer = o3d.visualization.Visualizer()
visualizer.create_window()

# Main loop for real-time visualization and distance measurement
for scan in lidar.iter_scans():
    for measurement in scan:
        process_lidar_measurement(measurement)

    # Update the Open3D point cloud
    point_cloud = o3d.geometry.PointCloud()
    point_cloud.points = o3d.utility.Vector3dVector(lidar_data)

    # Measure the distance between the lidar module and the points in the point cloud
    distances = np.linalg.norm(point_cloud.points, axis=1)

    # Check if there are points in the point cloud
    if len(distances) > 0:
        # Get the index of the closest point
        closest_index = np.argmin(distances)

        # Get the distance to the closest point
        closest_distance = distances[closest_index]

        # Get the angle of the closest point
        closest_angle = np.degrees(np.arctan2(point_cloud.points[closest_index][1], point_cloud.points[closest_index][0]))

        # Determine the direction of the closest point
        direction = None
        if closest_angle < -90:
            direction = "Left"
        elif closest_angle > 90:
            direction = "Right"
        elif closest_angle >= -90 and closest_angle <= 90:
            if closest_distance > warning_distance:
                direction = "Front"
            else:
                direction = "Back"

        # Print the distance and direction of the closest point
        print("Nearest object distance: {:.2f} millimeters".format(closest_distance))
        print("At angle: {:.2f} degrees from origin".format(closest_distance))
        print("Direction: {}".format(direction))
        print()

    # Clear the lidar data for the next iteration
    lidar_data.clear()

    # Clear previous visualized plots and add the updated point cloud
    visualizer.clear_geometries()
    visualizer.add_geometry(point_cloud)

    # Update the visualization
    visualizer.update_geometry(point_cloud)
    visualizer.poll_events()
    visualizer.update_renderer()

# Stop lidar scanning
lidar.stop_motor()
lidar.disconnect()

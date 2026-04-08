import os

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess
from launch.substitutions import LaunchConfiguration


ROS_WS = os.path.expanduser(os.environ.get("ROS_WS", "/home/r/silver_ws"))
INSTALL_PREFIX = os.path.join(ROS_WS, "install", "silverhand_ws_gateway")
GATEWAY_EXECUTABLE = os.path.join(INSTALL_PREFIX, "lib", "silverhand_ws_gateway", "gateway")
PYTHON_SITE_PACKAGES = os.path.join(INSTALL_PREFIX, "lib", "python3.12", "site-packages")


def generate_launch_description() -> LaunchDescription:
    return LaunchDescription(
        [
            DeclareLaunchArgument("host", default_value="0.0.0.0"),
            DeclareLaunchArgument("port", default_value="8766"),
            DeclareLaunchArgument("rover_cmd_vel_topic", default_value="/rover_base_controller/cmd_vel_unstamped"),
            DeclareLaunchArgument("rover_odom_topic", default_value="/rover_base_controller/odom"),
            DeclareLaunchArgument("rover_imu_topic", default_value="/imu_sensor_broadcaster/imu"),
            DeclareLaunchArgument("rover_battery_topic", default_value="/battery_state"),
            DeclareLaunchArgument("rover_headlights_service", default_value="/power_board/set_headlights"),
            ExecuteProcess(
                cmd=[
                    GATEWAY_EXECUTABLE,
                    "--domain",
                    "rover",
                    "--mode",
                    "ros",
                    "--host",
                    LaunchConfiguration("host"),
                    "--port",
                    LaunchConfiguration("port"),
                    "--rover-cmd-vel-topic",
                    LaunchConfiguration("rover_cmd_vel_topic"),
                    "--rover-odom-topic",
                    LaunchConfiguration("rover_odom_topic"),
                    "--rover-imu-topic",
                    LaunchConfiguration("rover_imu_topic"),
                    "--rover-battery-topic",
                    LaunchConfiguration("rover_battery_topic"),
                    "--rover-headlights-service",
                    LaunchConfiguration("rover_headlights_service"),
                ],
                additional_env={
                    "AMENT_PREFIX_PATH": f"{INSTALL_PREFIX}:{os.environ.get('AMENT_PREFIX_PATH', '')}",
                    "PYTHONPATH": f"{PYTHON_SITE_PACKAGES}:{os.environ.get('PYTHONPATH', '')}",
                },
                output="screen",
            ),
        ]
    )

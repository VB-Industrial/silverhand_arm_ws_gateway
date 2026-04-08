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
            ExecuteProcess(
                cmd=[
                    GATEWAY_EXECUTABLE,
                    "--domain",
                    "rover",
                    "--mode",
                    "mock",
                    "--host",
                    LaunchConfiguration("host"),
                    "--port",
                    LaunchConfiguration("port"),
                ],
                additional_env={
                    "AMENT_PREFIX_PATH": f"{INSTALL_PREFIX}:{os.environ.get('AMENT_PREFIX_PATH', '')}",
                    "PYTHONPATH": f"{PYTHON_SITE_PACKAGES}:{os.environ.get('PYTHONPATH', '')}",
                },
                output="screen",
            ),
        ]
    )

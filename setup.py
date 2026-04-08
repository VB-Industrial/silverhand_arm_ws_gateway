from setuptools import find_packages, setup


package_name = "silverhand_ws_gateway"


setup(
    name=package_name,
    version="0.1.0",
    packages=find_packages(exclude=["test"]),
    data_files=[
        ("share/ament_index/resource_index/packages", [f"resource/{package_name}"]),
        (f"share/{package_name}", ["package.xml", "README.md", "package.dsv"]),
        (
            f"share/{package_name}/launch",
            [
                "launch/arm_mock.launch.py",
                "launch/arm_ros.launch.py",
                "launch/arm_moveit.launch.py",
                "launch/rover_mock.launch.py",
                "launch/rover_ros.launch.py",
            ],
        ),
        (
            f"share/{package_name}/hook",
            [
                "hook/ament_prefix_path.dsv",
                "hook/ament_prefix_path.ps1",
                "hook/ament_prefix_path.sh",
            ],
        ),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="r",
    maintainer_email="r@localhost",
    description="WebSocket gateway for SilverHand robot domains.",
    license="Apache-2.0",
    entry_points={
        "console_scripts": [
            "gateway = silverhand_ws_gateway.main:main",
        ],
    },
)

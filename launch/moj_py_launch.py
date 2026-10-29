from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import LaunchConfiguration

def generate_launch_description():
    ime_teme_arg = LaunchConfiguration('ime_teme', default_value='neka_druga_tema')
    frekvencija_arg = LaunchConfiguration('frekvencija', default_value='5.0')
    pokreni_turtlesim_arg = LaunchConfiguration('pokreni_turtlesim', default_value='False')

    return LaunchDescription([
        Node(
            package="moj_prvi_paket",
            executable="moj_prvi_cvor",
            name="prvi_cvor_iz_launcha",
            namespace="prvi_namespace",
            parameters=[{"ime_teme": ime_teme_arg, "frekvencija": frekvencija_arg, "prag_temperature": 30.0}]
        ),
    ])
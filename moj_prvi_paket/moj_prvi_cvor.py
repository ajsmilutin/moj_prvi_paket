import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from rclpy.clock import Clock
from rclpy.duration import Duration
from math import sin
from moje_poruke.msg import MojaPrvaPoruka
from threading import Thread

def main() -> None:
    rclpy.init()
    node = Node('prvi_cvor')
    node.declare_parameter('prag_temperature', rclpy.Parameter.Type.DOUBLE)
    node.declare_parameter('ime_teme',"moja_prva_tema")
    node.declare_parameter('frekvencija', 8.0)
    thread = Thread(target = rclpy.spin, args=(node,), daemon=True)
    thread.start()

    ime_teme = node.get_parameter('ime_teme')
    publisher = node.create_publisher(MojaPrvaPoruka, 
        ime_teme.get_parameter_value().string_value, 10)

    clock = Clock()

    i = 0
    msg = MojaPrvaPoruka()



    while rclpy.ok():
        i += 1
        msg.temperatura = 25.0 + 10*sin(i/100.0)
        prag_temperature = node.get_parameter('prag_temperature')
        prag = prag_temperature.get_parameter_value().double_value
        print(f"Saljem poruku {i} sa temperaturom {msg.temperatura} i pragom {prag}")
        msg.poruka = "Vruće je" if msg.temperatura > prag else "Hladno je"
        msg.niz_brojeva = [ (i + x) % 128 for x in range(10)]
        msg.boja.r = 1.0
        msg.boja.g = 0.0
        msg.boja.b = 0.0
        msg.boja.a = 1.0
        publisher.publish(msg)
        frekvencija = node.get_parameter('frekvencija').get_parameter_value().double_value
        clock.sleep_for(Duration(seconds=1.0/frekvencija))
        

if __name__ == '__main__':
    main()

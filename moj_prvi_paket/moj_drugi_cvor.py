import rclpy
from rclpy.node import Node
from moje_poruke.msg import MojaPrvaPoruka
from statistics import mean
from rclpy.clock import Clock
from rclpy.duration import Duration

def funkcija_koja_se_izvrsi(msg: MojaPrvaPoruka) -> None:
    print(f"Temperatura: {msg.temperatura}")
    print(msg.poruka)
    print(f"Srednja vrijednost niza brojeva: {mean(msg.niz_brojeva)}")
    print(f"Boja: {msg.boja}")



def main() -> None:
    rclpy.init()

    node = Node('drugi_cvor')
    node.declare_parameter('ime_teme', "moja_prva_tema")

    ime_teme = node.get_parameter('ime_teme')
    subscriber = node.create_subscription(MojaPrvaPoruka, ime_teme.get_parameter_value().string_value, 
        funkcija_koja_se_izvrsi, 10)

    rclpy.spin(node)


if __name__ == '__main__':
    main()
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

    subscriber = node.create_subscription(MojaPrvaPoruka, '/moja_prva_tema', 
        funkcija_koja_se_izvrsi, 10)

    rclpy.spin(node)


if __name__ == '__main__':
    main()
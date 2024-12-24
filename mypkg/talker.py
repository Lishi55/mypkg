import datetime
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16


class Talker(Node):
    def __init__(self):
        super().__init__("talker")
        self.pub = self.create_publisher(Int16, "countup", 10)
        self.create_timer(1, self.cb)
        self.n = 0
        self.m = 0

    def cb(self):
        msg = Int16()
        msg.data = self.n
        self.pub.publish(msg)
        now = datetime.datetime.now()
        self.n = now.minute * 100
        self.n += now.second


def main():
    rclpy.init()
    node = Talker()
    rclpy.spin(node)


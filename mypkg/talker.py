import datetime
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32


class Talker(Node):
    def __init__(self):
        super().__init__("talker")
        self.pub = self.create_publisher(Int32, "countup", 10)
        self.create_timer(1, self.cb)
        self.n = 0

    def cb(self):
        msg = Int32()
        msg.data = self.n
        self.pub.publish(msg)
        now = datetime.datetime.now()
        self.n = now.hour * 10000
        self.n += now.minute * 100
        self.n += now.second


def main():
    rclpy.init()
    node = Talker()
    rclpy.spin(node)


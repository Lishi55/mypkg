import datetime
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

rclpy.init()
node = Node("talker")
pub = node.create_publisher(Int16, "countup", 10)
n = 0


def cb():
    global n
    msg = Int16()
    msg.data = n
    pub.publish(msg)
    now = datetime.datetime.now()
    n = now.second


def main():
    node.create_timer(1, cb)
    rclpy.spin(node)

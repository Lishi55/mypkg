import datetime
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

rclpy.init()
node = Node("talker")
pub = node.create_publisher(Int32, "countup", 10)
n = 0


def cb():
    global n
    msg = Int32()
    msg.data = n
    pub.publish(msg)
    now = datetime.datetime.now()
    n = now.hour * 10000
    n += now.minute * 100
    n += now.second


def main():
    node.create_timer(1, cb)
    rclpy.spin(node)

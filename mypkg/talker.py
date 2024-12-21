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
    dt_now = datetime.datetime.now()
    time = dt_now.hour * 10000
    time += dt_now.minute * 100
    time += dt_now.second
    n = time


def main():
    node.create_timer(1, cb)
    rclpy.spin(node)

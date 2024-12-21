import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32


rclpy.init()
node = Node("listener")


def cb(msg):
    global node
    node.get_logger().info("%d" % msg.data)


def main():
    pub = node.create_subscription(Int32, "countup", cb, 10)
    rclpy.spin(node)

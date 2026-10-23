#!/usr/bin/env python3
import rclpy
import time
import datetime
from rclpy.node import Node

class TimerNode(Node):
    def __init__(self):
        super().__init__('Timer')
        self.counter = 0
        period = 1
        self.timer = self.create_timer(period, self.timer_callback)
    def timer_callback(self):
        self.counter += 1
        current_time = datetime.datetime.now().strftime('%H:%M:%S')
        self.get_logger().info(f'{self.counter} Current time:{current_time}')
        if self.counter >= 5:
            self.timer.cancel()
    

def main(args=None):
    rclpy.init(args=args)                   # инициализация ROS 2
    node = TimerNode()
    rclpy.spin(node)                        # запускаем цикл обработки
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
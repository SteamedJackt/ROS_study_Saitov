import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/jackt/ros2_ws/src/base_pkg/install/base_pkg'

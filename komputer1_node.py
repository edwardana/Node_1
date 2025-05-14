#!/usr/bin/env python3
import rospy
import time
from std_msgs.msg import String

def komputer1():
    rospy.init_node('komputer1_node')
    pub_komputer1 = rospy.Publisher('jaringan_topic', String, queue_size=1)
    while not rospy.is_shutdown():
        data_msg = "Hello ROS"
        pub_komputer1.publish(data_msg)
        rospy.loginfo(data_msg)
        time.sleep(1)

if __name__ == '__main__':
    komputer1()

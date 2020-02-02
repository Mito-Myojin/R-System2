#!/usr/bin/env python

# SPDX-License-Identifier: GPL-3.0

import rospy
from std_msgs.msg import Int32
import wiringpi

wiringpi.wiringPiSetupGpio()
wiringpi.pinMode(25, 1)

n = 0

def three(message):
    global n
    n = message.data % 9

if __name__ == '__main__':
    rospy.init_node('LED')
    sub = rospy.Subscriber('count_up', Int32, three)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        if n == 0:
            wiringpi.digitalWrite(25, 1)
            rate.sleep()
        else:
            wiringpi.digitalWrite(25, 0)
            rate.sleep()

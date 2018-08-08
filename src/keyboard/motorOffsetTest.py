#!/usr/bin/env python
import getch
import rospy
from RDRONE.msg import Throttle

def setThrottle(char, throttle): 
    if (throttle <= 1780) and (char == 'a'):
        return throttle + 20
    elif (throttle >= 1220) and (char == 'd'):
        return throttle - 20
    else: 
        return throttle

def key_node():
    pub = rospy.Publisher('throttle_cmd', Throttle)
    rospy.init_node('key_node')
    throttle = 1200
    print('RDRONE constant motor offset test node. ')
    print('Use A to increment trottle by 20, use D to decrement throttle by 20 (range is 1200-1800)')
    print('Use F to exit')
    while not rospy.is_shutdown():
        msg = Throttle()
        msg.FL = throttle
        msg.FR = throttle
        msg.RR = throttle
        msg.RL = throttle
        pub.publish(msg)
        char = getch.getch()
        throttle = setThrottle(char,throttle)
        if char == 'f':
            exit(0)

if __name__=="__main__":
    try:
        key_node()
    except rospy.ROSInterruptException:
        pass

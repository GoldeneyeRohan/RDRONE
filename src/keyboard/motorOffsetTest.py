#!/usr/bin/env python
import getch
import rospy
from RDRONE.msg import Throttle

def setThrottle(char, throttle): 
    if (throttle <= 1780) and (char == 'a'):
        print('a')
        return throttle + 20
    elif (throttle >= 1220) and (char == 'd'):
        return throttle - 20
    else: 
        return throttle

def key_node():
    rospy.init_node('key_node')
    pub = rospy.Publisher('throttle_cmd', Throttle)
    throttle = 1200
    print('Use A to increment trottle by 20, use D to decrement throttle by 20 (range is 1200-1800)')
    while not rospy.is_shutdown():
        msg = Throttle()
        msg.FL = throttle
        msg.FR = throttle
        msg.RR = throttle
        msg.RL = throttle
        print('publishing msg')
        pub.publish(msg)
        print('published msg')
        char = getch.getch()
        throttle = setThrottle(char,throttle)
        if char == 'f':
            exit(0
)
if __name__=="__main__":
    try:
        key_node()
    except rospy.ROSInterruptException:
        pass

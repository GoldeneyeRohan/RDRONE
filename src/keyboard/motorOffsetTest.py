#!/usr/bin/env python
import getch
import rospy
from RDRONE.msg import Throttle

def setThrottle(char, throttleFront, throttleRear): 
    if (throttleFront <= 1780) and (char == 'a'):
        return throttleFront + 20, throttleRear
    elif (throttleFront >= 1220) and (char == 'd'):
        return throttleFront - 20, throttleRear
    elif (throttleRear <= 1780) and (char == 'j'):
        return throttleFront, throttleRear + 20
    elif (throttleRear >= 1220) and (char == 'l'):
        return throttleFront, throttleRear - 20

    else: 
        return throttleFront, throttleRear

def key_node():
    pub = rospy.Publisher('throttle_cmd', Throttle)
    rospy.init_node('key_node')
    throttleFront = 1200
    throttleRear = 1200
    print('RDRONE constant motor offset test node. ')
    print('Use A to increment trottle by 20, use D to decrement throttle by 20 (range is 1200-1800)')
    print('Use F to exit')
    while not rospy.is_shutdown():
        msg = Throttle()
        print(throttleFront, throttleRear)
        msg.FL = throttleFront
        msg.FR = throttleFront
        msg.RR = throttleRear
        msg.RL = throttleRear
        pub.publish(msg)
        char = getch.getch()
        throttleFront, throttleRear = setThrottle(char,throttleFront, throttleRear)
        if char == 'f':
            exit(0)

if __name__=="__main__":
    try:
        key_node()
    except rospy.ROSInterruptException:
        pass

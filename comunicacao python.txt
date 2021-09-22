#!/usr/bin/env python

import rospy
from std_msgs.msg import String

if __name__ == '__main__':

        rospy.init_node('comunicacao',anonymous=True)

        pub = rospy.Publisher('comunicacao',String,queue_size=10)

        rate = rospy.Rate(0.5)

        while not rospy.is_shutdown():
                msg = String()
                msg.data="Enviando uma mensagem em Python"
                pub.publish(msg)
                rate.sleep()
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                              

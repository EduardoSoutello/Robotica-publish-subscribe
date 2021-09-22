#!/usr/bin/env python

import rospy

if __name__ == '__main__':
        rospy.init_node('teste')

        rate = rospy.Rate(0.5)

        while not rospy.is_shutdown():
                rospy.loginfo('Sou um node teste')
                rate.sleep()

~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
"teste.py" 13L, 203C                                                           


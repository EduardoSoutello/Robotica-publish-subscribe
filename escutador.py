#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def callback_funcao(msg):
        rospy.loginfo("Mensagem: ")
        rospy.loginfo(msg)


if __name__ == '__main__':
        rospy.init_node('escucomunicacao')
        sub = rospy.Subscriber('comunicacao', String, callback_funcao)

        rospy.spin()



~                                                                               
~                                                                               
~                                                                               
~                                                                               
~           

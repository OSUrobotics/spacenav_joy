#!/usr/bin/env python
import roslib
roslib.load_manifest('spacenav_joy')
import rospy
from geometry_msgs.msg import Twist
from geometry_msgs.msg import TwistStamped
from sensor_msgs.msg import LaserScan
from sensor_msgs.msg import Joy
class controller:
	def __init__(self):
		rospy.loginfo('Start Init')
		self.joy_sub = rospy.Subscriber('/spacenav/joy',Joy,self.joy_callback)
		self.twist_command_pub = rospy.Publisher('/cmd_vel_mux/input/teleop', Twist, queue_size=3)
		self.command = Twist()
		rospy.loginfo('End Init')

	def joy_callback(self, joy):
		# print joy
		self.command.linear.x = joy.axes[0]*1.5
		self.command.linear.y = joy.axes[1]*1.5
		self.command.linear.z = joy.axes[2]*1.5
		self.command.angular.x = joy.axes[3]*1.5
		self.command.angular.y = joy.axes[4]*1.5
		self.command.angular.z = joy.axes[5]*1.5
		self.twist_command_pub.publish(self.command)

if __name__ == '__main__':
	rospy.init_node('stopper',log_level=rospy.DEBUG)
	controller = controller()
	rospy.spin()

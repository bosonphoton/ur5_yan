#!/usr/bin/env python

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal, MoveBaseFeedback
from actionlib_msgs.msg import *
from geometry_msgs.msg import Pose, Point, PoseWithCovarianceStamped, Quaternion, PoseStamped
from nav_msgs.srv import GetPlan
from nav_msgs.msg import Odometry
from std_msgs.msg import String
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from sound_play.libsoundplay import SoundClient
import time
from datetime import datetime


speaker = SoundClient()
last_color = ""
last_calltime = datetime.strptime("00:00:00","%H:%M:%S")


def callback(data):
	colors = open("colors.txt", "a")
	global last_calltime, last_color
	cube = data.data
	t = time.localtime()
	tf = time.strftime("%H:%M:%S",t)
	current_time = datetime.strptime(tf, "%H:%M:%S")
	delta_time = current_time - last_calltime

	if abs(delta_time.total_seconds()) >= 3:
		if "Red Cup" in cube:
			if last_color != "redsmall":
				print("Red Small")
				#speaker.say("Did you mean Red?")
				last_color = "redsmall"
				colors.write("\n")
				colors.write("\narears")
				colors.close()

		elif "Red Plate" in cube:
			if last_color != "redlarge":
				print("Red Large")
				#speaker.say("Did you mean Green?")
				last_color = "redlarge"
				colors.write("\n")
				colors.write("\narearl")
				colors.close()
				

		elif "Green Cup" in cube:
			if last_color != "greensmall":
				print("Green Small")
				#speaker.say("Did you mean Blue?")
				last_color = "greensmall"
				colors.write("\n")
				colors.write("\nareags")
				colors.close()

		else:
			if last_color != "greenlarge":
				print("Green Large")
				#speaker.say("Did you mean Blue?")
				last_color = "greenlarge"
				colors.write("\n")
				colors.write("\nareagl")
				colors.close()


		t = time.localtime()
		tf = time.strftime("%H:%M:%S",t)
		last_calltime = datetime.strptime(tf, "%H:%M:%S")


	return last_color


if __name__ == '__main__':

	try:
		rospy.init_node('speak_object')
		rospy.Subscriber ('/gaze_vector',String, callback)
		rospy.spin()

	except rospy.ROSInterruptException:
		print "finished!"


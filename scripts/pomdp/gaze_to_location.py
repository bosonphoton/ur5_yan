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

current_x = 0.0
current_y = 0.0
move = actionlib.SimpleActionClient("move_base", MoveBaseAction)
def callback_pose(data):
	buffer_range = 1
	global current_x,current_y
	previous_x = current_x
	previous_y = current_y
	string_data = data.data
	co_ordinates = string_data.split(",")
	current_x = float(co_ordinates[0])
	current_x = round(current_x,2)
	current_y = float(co_ordinates[1])
	current_y = round(current_y,2)
	trigger_value = int(co_ordinates[2])
	if trigger_value == 1:
		print current_x
		print current_y
		goto(current_x,current_y)


# def goto_location(x,y):
#     goalReached = False
#
#     while(not goalReached):
#
#         goalReached = moveToGoal(x,y)
#         if (goalReached):
#             rospy.loginfo("Reached destination!")
#
# def moveToGoal(x,y):
#     global move
#     move = actionlib.SimpleActionClient("move_base", MoveBaseAction)
#     while(not move.wait_for_server(rospy.Duration.from_sec(5.0))):
#             rospy.loginfo("Waiting for the move_base action server to come up")
#     simplegoal = MoveBaseGoal()
#     simplegoal.target_pose.header.frame_id = "map"
#     simplegoal.target_pose.header.stamp = rospy.Time.now()
#     simplegoal.target_pose.pose.position =  Point(x,y,0)
#     simplegoal.target_pose.pose.orientation.x = 0.0
#     simplegoal.target_pose.pose.orientation.y = 0.0
#     # if(sensitivity != 0):
#     simplegoal.target_pose.pose.orientation.z = 0.0
#     simplegoal.target_pose.pose.orientation.w = 1.0
#     # else:
#     #     simplegoal.target_pose.pose.orientation.z = 0.0
#     #     simplegoal.target_pose.pose.orientation.w = 0.0
#     rospy.loginfo("Sending Next goal location ")
#     move.send_goal(simplegoal)
#     move.wait_for_result(rospy.Duration(60))
#     if(move.get_state() ==  GoalStatus.SUCCEEDED):
#     	rospy.loginfo("This is the end of navigation")
#     	return True
#
#     else:
#     	rospy.loginfo("The robot failed to reach the destination")
#     	return False

def goto(x,y):
	global move
	move = actionlib.SimpleActionClient('move_base',MoveBaseAction)
	move.cancel_all_goals()
	move.wait_for_server()
	goal = MoveBaseGoal()
	goal.target_pose.header.frame_id = "map"
	goal.target_pose.header.stamp = rospy.Time.now()
	goal.target_pose.pose.position.x = x
	goal.target_pose.pose.position.y = y
	goal.target_pose.pose.orientation.z = 0.0
	goal.target_pose.pose.orientation.w = 1.0
	move.send_goal(goal)
	wait = move.wait_for_result()
	if not wait:
	    print "Error!"
	    rospy.signal_shutdown()
	else:
	    return move.get_result()


if __name__ == '__main__':

#	try: 
#		rospy.init_node('gaze_to_location')
#		goto(-0.0, -2.8)

	try:
		rospy.init_node('gaze_to_location')
		rospy.Subscriber ('/gaze_vector',String, callback_pose)
		# goto_location(0.75,1.54)
		rospy.spin()

	except rospy.ROSInterruptException:
		print "finished!"

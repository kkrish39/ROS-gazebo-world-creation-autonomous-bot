#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from project_3a.srv import Velocity
from project_3a.srv import VelocityResponse

#vel msg of type Twist
msg = Twist()
vel_topic = '/cmd_vel'
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

#function to rotate the turtle to a specified angle
def rotate_turtle(speed, angle, clockwise):
    angular_speed = speed*2*3.14/360
    relative_angle = angle*2*3.14/360

    msg.linear.x=0
    msg.linear.y=0
    msg.linear.z=0
    msg.angular.x = 0
    msg.angular.y = 0

    if clockwise:
        msg.angular.z = -abs(angular_speed)
    else:
        msg.angular.z = abs(angular_speed)
    
    t_start = rospy.Time.now().to_sec()
    current_angle = 0

    while(current_angle < relative_angle):
        pub.publish(msg)
        t_now = rospy.Time.now().to_sec()
        current_angle = angular_speed*(t_now-t_start)

    msg.angular.z = 0
    pub.publish(msg)
    
    #Returning an empty response
    return VelocityResponse()

def move_turtle(speed, distance, isForward):
    #check to make the turtle move forward or backward
    if(isForward):
        msg.linear.x = abs(speed)
    else:
        msg.linear.x = -abs(speed)
    
    msg.linear.y = 0
    msg.linear.z = 0
    msg.angular.x = 0
    msg.angular.y = 0
    msg.angular.z = 0

    pub.publish(msg)
    rospy.sleep(int(distance))
    return VelocityResponse()

def draw_initials(req):
    #check to see if the received data is to move or rotate the turtle
    if(req.move_rotate == 'move'):
       return move_turtle(req.speed, req.angle_distance, req.isForward_clockwise)
    if(req.move_rotate == 'rotate'):
       return rotate_turtle(req.speed, req.angle_distance, req.isForward_clockwise)

#server to handle client request to draw the initials
def draw_initials_server():
    rospy.init_node('my_initials')
    rospy.sleep(1)
    s = rospy.Service('my_initials_server',Velocity, draw_initials)
    rospy.spin()
    
if __name__ == '__main__':
    print('Server up and running to receive data...')
    draw_initials_server()
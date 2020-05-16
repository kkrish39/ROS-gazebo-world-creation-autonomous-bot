#!/usr/bin/env python
import rospy
from project_3a.srv import Velocity

#client handler to send data to draw initials
def parse_room_client():
    rospy.wait_for_service('my_initials_server')
    try:
        draw_initals = rospy.ServiceProxy('my_initials_server', Velocity)
        #data to trace the letter K
        pathToTraceTheRoom = [
        [0.2,3,'move',False],
        [0.4,15,'move',True],
        [0.1,1,'move',True],
        [0,2,'move',True],
        [15,90,'rotate',True],
        [0.1,5,'move',True],
        [0,1,'move',True],
        [15,4,'rotate',True],
        [0.13,35,'move',False],
        [0.1,5,'move',False],
        [0,1,'move',False],
        [0.13,12,'move',True],
       [15,90,'rotate',True],
       [0.1,5,'move',True],
       [0.1,10,'move',False]
       ]

        for r in pathToTraceTheRoom:
            draw_initals(r[0], r[1], r[2], r[3])
       
    except rospy.ServiceException, e:
        print("Service call failed: %s"%e)


if __name__ == '__main__':
    rospy.sleep(35)
    print("Cleint sending data to parse the room...")
    parse_room_client()
import rospy
from clever import srv
from std_srvs.srv import Trigger
import time
import math

rospy.init_node('flight')
tolerance = 0.2

get_telemetry = rospy.ServiceProxy('get_telemetry', srv.GetTelemetry)
navigate = rospy.ServiceProxy('navigate', srv.Navigate)
navigate_global = rospy.ServiceProxy('navigate_global', srv.NavigateGlobal)
set_position = rospy.ServiceProxy('set_position', srv.SetPosition)
set_velocity = rospy.ServiceProxy('set_velocity', srv.SetVelocity)
set_attitude = rospy.ServiceProxy('set_attitude', srv.SetAttitude)
set_rates = rospy.ServiceProxy('set_rates', srv.SetRates)
land = rospy.ServiceProxy('land', Trigger)
navigate(x = 0 , y = 0 , z = 1.4 , speed = 1.2, frame_id='body', auto_arm = True)
telem = get_telemetry(frame_id='aruco_map_detected')
while math.isnan(telem.x):
    telem = get_telemetry(frame_id='aruco_map_detected')
    rospy.sleep(0.1)

navigate(x = 0.59 , y = 0.855 , z = 1.4 , speed = 0.7, frame_id='aruco_map')
rospy.sleep(5)

navigate(x = 0.295 , y = 1.18 , z = 1.4 , speed = 0.7, frame_id='aruco_map')
rospy.sleep(5)

navigate(x = 0.59 , y = 0.855 , z = 1.4 , speed = 0.7, frame_id='aruco_map')
rospy.sleep(5)

navigate(x = 0 , y = 0.85 , z = 1.4 , speed = 0.7, frame_id='aruco_map')
rospy.sleep(5)

navigate(x = 0.295 , y = 0.295 , z = 1.4 , speed = 0.7, frame_id='aruco_map')
rospy.sleep(5)

navigate(x = 0.59 , y = 0.59 , z = 1.4 , speed = 0.7, frame_id='aruco_map')
rospy.sleep(5)

navigate(x = 0.59 , y = 1.77 , z = 1.4 , speed = 0.7, frame_id='aruco_map')
rospy.sleep(5)

navigate(x = 0.59 , y = 2.36 , z = 1.4 , speed = 0.7, frame_id='aruco_map')
rospy.sleep(5)

navigate(x = 0 , y = 2.655 , z = 1.4 , speed = 0.7, frame_id='aruco_map')
rospy.sleep(5)

navigate(x = 0 , y = 1.77 , z = 1.4 , speed = 0.7, frame_id='aruco_map')
rospy.sleep(5)

navigate(x = 1.475 , y = 1.77 , z = 1.4 , speed = 0.7, frame_id='aruco_map')
rospy.sleep(5)

navigate(x = 1.475 , y = 2.36 , z = 1.4 , speed = 0.7, frame_id='aruco_map')
rospy.sleep(5)

navigate(x = 0.885 , y = 2.655 , z = 1.4 , speed = 0.7, frame_id='aruco_map')
rospy.sleep(5)

navigate(x = 0.885 , y = 1.77 , z = 1.4 , speed = 0.7, frame_id='aruco_map')
rospy.sleep(5)

navigate(x = 0.885 , y = 0.296 , z = 1.4 , speed = 0.7, frame_id='aruco_map')
rospy.sleep(5)

navigate(x = 1.475 , y = 0.295 , z = 1.4 , speed = 0.7, frame_id='aruco_map')
rospy.sleep(5)

navigate(x = 1.475 , y = 1.18 , z = 1.4 , speed = 0.7, frame_id='aruco_map')
rospy.sleep(5)

navigate(x = 0.885 , y = 1.18 , z = 1.4 , speed = 0.7, frame_id='aruco_map')
rospy.sleep(5)

navigate(x =0.885  , y = 0.295 , z = 1.4 , speed = 0.7, frame_id='aruco_map')
rospy.sleep(5)

navigate(x =0.885  , y = 0.295 , z = 0.88 , speed = 0.7, frame_id='aruco_map')
rospy.sleep(5)

navigate(x =0.885 , y = 1.18 , z = 0.88 , speed = 0.7, frame_id='aruco_map')
rospy.sleep(5)

navigate(x =0.885 , y = 1.18 , z = 0.2 , speed = 0.7, frame_id='aruco_map')
rospy.sleep(5)

navigate(x =0.885 , y = 0.295 , z = 0.2 , speed = 0.7, frame_id='aruco_map')
rospy.sleep(5)

navigate(x =0.885 , y = 0.295 , z = 0.88 , speed = 0.7, frame_id='aruco_map')
rospy.sleep(5)

navigate(x =0.59 , y = 2.36 , z = 0.88 , speed = 0.7, frame_id='aruco_map')
rospy.sleep(5)

navigate(x =0.59 , y = 2.36 , z = 0.2 , speed = 0.7, frame_id='aruco_map')
rospy.sleep(5)

navigate(x =0.59 , y = 1.77 , z = 0.2 , speed = 0.7, frame_id='aruco_map')
rospy.sleep(5)

navigate(x =0.59 , y = 1.77 , z = 0.88 , speed = 0.7, frame_id='aruco_map')
rospy.sleep(5)

navigate(x =0.885 , y =0.295  , z = 0.88 , speed = 0.7, frame_id='aruco_map')
rospy.sleep(5)

navigate(x =0.885 , y =0.295  , z = 0.2 , speed = 0.7, frame_id='aruco_map')
rospy.sleep(5)

navigate(x =0.885 , y =1.18  , z = 0.2 , speed = 0.7, frame_id='aruco_map')
rospy.sleep(5)

navigate(x =1.475 , y =1.18  , z = 0.2 , speed = 0.7, frame_id='aruco_map')
rospy.sleep(5)

navigate(x =1.475 , y =1.18  , z = 0.88 , speed = 0.7, frame_id='aruco_map')
rospy.sleep(5)

navigate(x =0.59 , y =0.295  , z = 0.88 , speed = 0.7, frame_id='aruco_map')
rospy.sleep(5)

land()
print('gg')


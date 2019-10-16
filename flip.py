import rospy
import math
from clever import srv
from std_srvs.srv import Trigger

rospy.init_node('flight')

get_telemetry = rospy.ServiceProxy('get_telemetry', srv.GetTelemetry)
navigate = rospy.ServiceProxy('navigate', srv.Navigate)
navigate_global = rospy.ServiceProxy('navigate_global', srv.NavigateGlobal)
set_position = rospy.ServiceProxy('set_position', srv.SetPosition)
set_velocity = rospy.ServiceProxy('set_velocity', srv.SetVelocity)
set_attitude = rospy.ServiceProxy('set_attitude', srv.SetAttitude)
set_rates = rospy.ServiceProxy('set_rates', srv.SetRates)
land = rospy.ServiceProxy('land', Trigger)



navigate(x = 0 , y = 0 , z = 0.5, speed = 0.5, frame_id='body', auto_arm = True)
rospy.sleep(5)

def flip():
    start = get_telemetry()  # memorize starting position

    set_rates(thrust=1)  # bump up
    rospy.sleep(0.2)

    set_rates(roll_rate=30, thrust=0.2)  # maximum roll rate

    while True:
        telem = get_telemetry()

        if abs(telem.roll) > math.pi/2:
            break

    rospy.loginfo('finish flip')
    set_position(x=start.x, y=start.y, z=start.z, yaw=start.yaw)  # finish flip

print navigate(z=2, speed=1, frame_id='body', auto_arm=True)  # take off
rospy.sleep(10)

rospy.loginfo('flip')
flip()
land()


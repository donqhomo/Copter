import rospy
from clever import srv
from std_srvs.srv import Trigger

import time

from rpi_ws281x import Adafruit_NeoPixel
from rpi_ws281x import Color

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


LED_COUNT      = 60
LED_PIN        = 18
LED_FREQ_HZ    = 800000
LED_DMA        = 10
LED_BRIGHTNESS = 166
LED_INVERT     = False
LED_CHANNEL    = 0

strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT)
strip.begin()

def colorWipe(strip, color, wait_ms=50):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/2000.0)

def light_of_success():
    print('color of success.')
    colorWipe(strip, Color(0, 255, 0), wait_ms=100)
    colorWipe(strip, Color(0, 0, 0), wait_ms=100)

light_of_success()

# взлететь
navigate(x = 0 , y = 0 , z = 1.4 , speed = 0.5, frame_id='body', auto_arm = True)
while True:
    if get_telemetry().z - start.z + z < tolerance:
        break
    rospy.sleep(0.2)
# пролетел  =к столбу 1
navigate(x = 0 , y = 1.2 , z = 0 , speed = 0.5, frame_id='body')
    rospy.sleep(0.2)

#облет столба 1
navigate(x = 0, y = 0.6 , z = 0 , speed = 0.5, frame_id='body')
navigate(x = - 0.6 , y = 0 , z = 0 , speed = 0.5, frame_id='body')
navigate(x = 0, y = - 0.6 , z = 0 , speed = 0.5, frame_id='body')
navigate(x = 0 , y = 0 , z = 0.15 , speed = 0.5, frame_id='body')
navigate(x = 0.6 , y = 0 , z = 0 , speed = 0.5, frame_id='body')

rospy.sleep(0.2)
 #  прилетел к столбу 2
navigate(x = 0.3 , y = 0 , z = -0.15 , speed = 0.5, frame_id='body')
    rospy.sleep(0.2)
#облет столба 2
navigate(x = 0, y = 0.6 , z = 0 , speed = 0.5, frame_id='body')
navigate(x =  0.6 , y = 0 , z = 0 , speed = 0.5, frame_id='body')
navigate(x = 0, y = - 0.6 , z = 0 , speed = 0.5, frame_id='body')
navigate(x = 0 , y = 0 , z = 0.15 , speed = 0.5, frame_id='body')
navigate(x = 0.6 , y = 0 , z = 0 , speed = 0.5, frame_id='body')
    rospy.sleep(0.2)
 # прилетел к столбу 3
navigate(x = 0 , y = -0.8 , z = -0.15 , speed = 0.5, frame_id='body')
    rospy.sleep(0.2)
#облет столба 3
navigate(x = 0, y = -0.6 , z = 0 , speed = 0.5, frame_id='body')
navigate(x =  0.6 , y = 0 , z = 0 , speed = 0.5, frame_id='body')
navigate(x = 0, y =  0.6 , z = 0 , speed = 0.5, frame_id='body')
navigate(x = 0 , y = 0 , z = 0.15 , speed = 0.5, frame_id='body')
navigate(x = -0.6 , y = 0 , z = 0 , speed = 0.5, frame_id='body')
navigate(x = 0, y =- 0.6 , z = 0 , speed = 0.5, frame_id='body')
    rospy.sleep(0.2)
# прилетел к столбу 4
navigate(x = -0.3 , y = 0 , z = -0.15 , speed = 0.5, frame_id='body')
    rospy.sleep(0.2)
#облет столба 4
navigate(x = 0, y = 0.6 , z = 0 , speed = 0.5, frame_id='body')
navigate(x = - 0.6 , y = 0 , z = 0 , speed = 0.5, frame_id='body')
navigate(x = 0, y = - 0.6 , z = 0 , speed = 0.5, frame_id='body')
navigate(x = 0 , y = 0 , z = 0.15 , speed = 0.5, frame_id='body')
navigate(x = 0.6 , y = 0 , z = 0 , speed = 0.5, frame_id='body')
navigate(x = 0, y = 0.6 , z = 0 , speed = 0.5, frame_id='body')
navigate(x = 0 , y = 0 , z = -0.15 , speed = 0.5, frame_id='body')
    rospy.sleep(0.2)
#  прилетел к серединке
navigate(x = 0.15 , y = 0 , z = 0 , speed = 0.5, frame_id='body')
    rospy.sleep(0.2)
# спустился
navigate(x = 0 , y = 0 , z = -0.9 , speed = 0.5, frame_id='body')
    rospy.sleep(0.2)
# облетел к горизотали 1 нижняя
for i in range(3):
    navigate(x = 0, y = 0 , z = -0.5 , speed = 0.5, frame_id='body')
    navigate(x = 0 , y = -0.5 , z = 0 , speed = 0.5, frame_id='body')
    navigate(x = 0.15, y = 0 , z = 0 , speed = 0.5, frame_id='body')
    navigate(x = 0, y =  0 , z = 0.5 , speed = 0.5, frame_id='body')
    navigate(x = 0 , y = 0.5 , z = 0 , speed = 0.5, frame_id='body')
    navigate(x = -0.15, y = 0 , z = 0 , speed = 0.5, frame_id='body')
rospy.sleep(0.2)
 #  прилетел к серединке 2 нижняя
navigate(x = 0 , y = 1.2 , z = 0 , speed = 0.5, frame_id='body')
    rospy.sleep(0.2)

# облетел к горизотали 2 нижняя
for i in range(3):
    navigate(x = 0, y = 0 , z = -0.5 , speed = 0.5, frame_id='body')
    navigate(x = 0 , y = -0.5 , z = 0 , speed = 0.5, frame_id='body')
    navigate(x = 0.15, y = 0 , z = 0 , speed = 0.5, frame_id='body')
    navigate(x = 0, y =  0 , z = 0.5 , speed = 0.5, frame_id='body')
    navigate(x = 0 , y = 0.5 , z = 0 , speed = 0.5, frame_id='body')
    navigate(x = -0.15, y = 0 , z = 0 , speed = 0.5, frame_id='body')
    rospy.sleep(0.2)
# диагональка
navigate(x = -0.4 , y = 0 , z = 0.7 , speed = 0.5, frame_id='body')
    rospy.sleep(0.2)
# сдвиг на первую 8
navigate(x = 0 , y = -0.6 , z = 0 , speed = 0.5, frame_id='body')
    rospy.sleep(0.2)
# 8_1
navigate(x = 0.4, y = 0 , z = 0 , speed = 0.5, frame_id='body')
navigate(x = 0 , y = 0 , z = -0.3 , speed = 0.5, frame_id='body')
navigate(x = -0.4, y = 0 , z = 0 , speed = 0.5, frame_id='body')
navigate(x = 0, y =  0 , z = -0.6 , speed = 0.5, frame_id='body')
navigate(x = 0.7 , y = 0 , z = 0 , speed = 0.5, frame_id='body')
navigate(x = 0, y = 0 , z = 0.6 , speed = 0.5, frame_id='body')
navigate(x = -0.4, y = 0 , z = 0 , speed = 0.5, frame_id='body')
navigate(x = 0 , y = 0 , z = 0.3 , speed = 0.5, frame_id='body')
navigate(x = 0.4, y = 0 , z = 0 , speed = 0.5, frame_id='body')
    rospy.sleep(0.2)
# сдвиг на вторую 8
navigate(x = 0, y = 0.4 , z = 0 , speed = 0.5, frame_id='body')
    rospy.sleep(0.2)
# 8_2
navigate(x = -0.4, y = 0 , z = 0 , speed = 0.5, frame_id='body')
navigate(x = 0 , y = 0 , z = -0.3 , speed = 0.5, frame_id='body')
navigate(x = 0.4, y = 0 , z = 0 , speed = 0.5, frame_id='body')
navigate(x = 0, y =  0 , z = -0.6 , speed = 0.5, frame_id='body')
navigate(x = -0.7 , y = 0 , z = 0 , speed = 0.5, frame_id='body')
navigate(x = 0, y = 0 , z = 0.6 , speed = 0.5, frame_id='body')
navigate(x = 0.4, y = 0 , z = 0 , speed = 0.5, frame_id='body')
navigate(x = 0 , y = 0 , z = 0.3 , speed = 0.5, frame_id='body')
navigate(x = -0.4, y = 0 , z = 0 , speed = 0.5, frame_id='body')

# сдвиг до конца
navigate(x = 0, y = 0.4 , z = 0 , speed = 0.5, frame_id='body')
    rospy.sleep(0.2)
#облет столба 4
navigate(x = 0, y = -0.6 , z = 0 , speed = 0.5, frame_id='body')
navigate(x = 0.6 , y = 0 , z = 0 , speed = 0.5, frame_id='body')
navigate(x = 0, y = 0.6 , z = 0 , speed = 0.5, frame_id='body')
navigate(x = 0 , y = 0 , z = 0.15 , speed = 0.5, frame_id='body')
navigate(x = -0.6 , y = 0 , z = 0 , speed = 0.5, frame_id='body')
navigate(x = 0, y = -0.6 , z = 0 , speed = 0.5, frame_id='body')
navigate(x = 0 , y = 0 , z = -0.15 , speed = 0.5, frame_id='body')
    rospy.sleep(0.2)
land()

print('gg')

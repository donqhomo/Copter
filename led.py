
import time

from rpi_ws281x import Adafruit_NeoPixel
from rpi_ws281x import Color


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

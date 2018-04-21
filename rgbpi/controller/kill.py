import time
import math
from neopixel import *
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

##################################################
# PARAMS
##################################################
pin_window=5
pin_logo=6
pin_button=13
pin_gpu=19

#################################################
GPIO.setup(pin_window, GPIO.OUT)
GPIO.setup(pin_logo, GPIO.OUT)
GPIO.setup(pin_button, GPIO.OUT)
GPIO.setup(pin_gpu, GPIO.OUT)

##################################################
# COLORS
##################################################
red=Color(0,255,0)
green=Color(255,0,0)
blue=Color(0,0,255)
cyan=Color(255,0,255)
yellow=Color(255,255,0)
purple=Color(0,255,255)
white=Color(255,255,255)
off=Color(0,0,0)

##################################################
# NEW CLASS
##################################################
class LedStrip(Adafruit_NeoPixel):
    def __init__(self,LED_COUNT,LED_PIN,LED_FREQ_HZ,LED_DMA,LED_INVERT,LED_BRIGHTNESS,LED_CHANNEL,EN_PIN):
        Adafruit_NeoPixel.__init__(self,LED_COUNT,LED_PIN,LED_FREQ_HZ,LED_DMA,LED_INVERT,LED_BRIGHTNESS,LED_CHANNEL)
        self.enpin=EN_PIN

##################################################
# FUNCTIONS
##################################################
def show(strip):
    GPIO.output(strip.enpin, GPIO.LOW)
    strip.show()
    time.sleep(0.005)
    GPIO.output(strip.enpin, GPIO.HIGH)

def full(strip,color):
    for n in range(strip.numPixels()):
        strip.setPixelColor(n,color)
    show(strip)

##################################################
# MAIN
##################################################
GPIO.output(pin_window, GPIO.HIGH)
GPIO.output(pin_logo, GPIO.HIGH)
GPIO.output(pin_button, GPIO.HIGH)
GPIO.output(pin_gpu, GPIO.HIGH)
window = LedStrip(76,18,800000,10,False,255,0,pin_window)
logo = LedStrip(9,18,800000,10,False,255,0,pin_logo)
button = LedStrip(2,18,800000,10,False,255,0,pin_button)
gpu = LedStrip(4,18,800000,10,False,255,0,pin_gpu)
window.begin()
logo.begin()
button.begin()
gpu.begin()

##################################################
full(window,off)
full(logo,off)
full(button,off)
full(gpu,off)
##################################################
quit

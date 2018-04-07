import time
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
    def enpin(self):
        return self.enpin

##################################################
# FUNCTIONS
##################################################

def full(strip,color):
    for n in range(strip.numPixels()):
        strip.setPixelColor(n,color)
    strip.show()

def breathe(strip,color,speed):
    i=0
    while i<4:
        strip.setBrightness(int(i*i*i*i))
        full(strip,color)
        i=i+0.04
        time.sleep(float(1)/speed)
    strip.setBrightness(255)
    full(strip,color)
    i=0
    while i<4:
        strip.setBrightness(int(255-i*i*i*i))
        full(strip,color)
        i=i+0.04
        time.sleep(float(1)/speed)
    strip.setBrightness(0)
    full(strip,off)
#CIRCLE OLD
def circle_old(strip,turns,speed):
    for t in range(turns):
        for i in range(255):
            for n in range(strip.numPixels()):
                strip.setPixelColor(n,Color(0,255,i))
            strip.show()
            time.sleep(float(1)/speed)
        for i in range(255):
            for n in range(strip.numPixels()):
                strip.setPixelColor(n,Color(0,255-i,255))
            strip.show()
            time.sleep(float(1)/speed)
        for i in range(255):
            for n in range(strip.numPixels()):
                strip.setPixelColor(n,Color(i,0,255))
            strip.show()
            time.sleep(float(1)/speed)
        for i in range(255):
            for n in range(strip.numPixels()):
                strip.setPixelColor(n,Color(255,0,255-i))
            strip.show()
            time.sleep(float(1)/speed)
        for i in range(255):
            for n in range(strip.numPixels()):
                strip.setPixelColor(n,Color(255,i,0))
            strip.show()
            time.sleep(float(1)/speed)
        for i in range(255):
            for n in range(strip.numPixels()):
                strip.setPixelColor(n,Color(255-i,255,0))
            strip.show()
            time.sleep(float(1)/speed)
    full(strip,off)

#CIRCLE
def circle(strip,turns,speed):
    for t in range(1530*turns):
        for n in range(strip.numPixels()):
            speed*setfade(strip,n)
        strip.show()
        time.sleep(0.001)

#SETFADE
def setfade(strip,n):
    g=(strip.getPixelColor(n)>>16)&255
    r=(strip.getPixelColor(n)>>8)&255
    b=strip.getPixelColor(n)&255
    if g==0:
        if r==0:
            g+=1
        elif b==255:
            r-=1
        else:
            b+=1
    elif r==0:
        if b==0:
            r+=1
        elif g==255:
            b-=1
        else:
            g+=1
    elif b==0:
        if r==255:
            g-=1
        else:
            r+=1
    strip.setPixelColor(n,Color(g,r,b))

#RAINBOW
def rainbow(strip):
    for n in range(strip.numPixels()):
        i=int((float(n)/(strip.numPixels()-1))*1529)
        if i>=0 and i<=254:
            strip.setPixelColor(n,Color(0,255,i%255))
        elif i<=509:
            strip.setPixelColor(n,Color(0,255-(i%255),255))
        elif i<=764:
            strip.setPixelColor(n,Color(i%255,0,255))
        elif i<=1019:
            strip.setPixelColor(n,Color(255,0,255-(i%255)))
        elif i<=1274:
            strip.setPixelColor(n,Color(255,i%255,0))
        elif i<=1529:
            strip.setPixelColor(n,Color(255-(i%255),255,0))
    strip.show()

#DOT
def dot(strip,color,length,speed,turns):
    full(strip,off)
    for t in range(turns):
        n=strip.numPixels()
        while n<(2*strip.numPixels()):
            strip.setPixelColor(n%strip.numPixels(),color)
            strip.setPixelColor((n-length)%strip.numPixels(),off)
            strip.show()
            time.sleep(float(1)/speed)
            n+=1
    full(strip,off)        

    
##################################################
# MAIN
##################################################
GPIO.output(pin_window, GPIO.LOW)
#GPIO.output(pin_logo, GPIO.HIGH)
#GPIO.output(pin_button, GPIO.HIGH)
#GPIO.output(pin_gpu, GPIO.HIGH)
window = LedStrip(76,18,800000,10,False,255,0,pin_window)
#logo = LedStrip(9,18,800000,10,False,255,0,pin_logo)
#button = LedStrip(2,18,800000,10,False,255,0,pin_button)
window.begin()
#logo.begin()
#button.begin()

##################################################
rainbow(window)
circle(window,1,1000)
full(window,off)
##################################################
quit

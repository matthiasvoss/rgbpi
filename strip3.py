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

def full_all(color):
    full(window,color)
    full(logo,color)
    full(button,color)
    full(gpu,color)

def full_set(strip,color):
    for n in range(strip.numPixels()):
        strip.setPixelColor(n,color)

def dot(strip,color,turns,speed,length):
    full(strip,off)
    for t in range(turns):
        n=strip.numPixels()
        while n<(2*strip.numPixels()):
            strip.setPixelColor(n%strip.numPixels(),color)
            strip.setPixelColor((n-length)%strip.numPixels(),off)
            show(strip)
            time.sleep(float(1)/speed)
            n+=1
    full(strip,off)

#CIRCLE
def circle(strip,turns,speed):
    for t in range(turns):
        for s in range(int(float(1530)/speed)):
            for n in range(strip.numPixels()):
                for i in range(speed):
                    setfade(strip,n)
            show(strip)
            time.sleep(0.01)

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
    show(strip)

def breatheval(x):
    return 255*(x**4)
    
def breathe(strip,turns,speed,hold,pause):
    for t in range(turns):
        i=float(0)
        while breatheval(i)<255:
            #print i,"-",breatheval(i),"-",int(breatheval(i))
            strip.setBrightness(int(breatheval(i)))
            show(strip)
            i=i+0.001*speed
            time.sleep(0.01)
        strip.setBrightness(255)
        show(strip)
        time.sleep(hold)
        i=i-0.001*speed
        while i>=0:
            #print i,"-",breatheval(i),"-",int(breatheval(i))
            strip.setBrightness(int(breatheval(i)))
            show(strip)
            i=i-0.001*speed
            time.sleep(0.01)
        strip.setBrightness(0)
        show(strip)
        time.sleep(pause)

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
gpu.setBrightness(125)
full_all(white)
time.sleep(3)
full_all(red)
time.sleep(3)
full_all(green)
time.sleep(3)
full_all(blue)
time.sleep(3)
full_all(off)

##################################################
quit

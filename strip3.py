import time
from neopixel import *
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

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
        GPIO.setup(EN_PIN, GPIO.OUT)
        GPIO.output(EN_PIN, GPIO.HIGH)
        super().__init__(LED_COUNT,LED_PIN,LED_FREQ_HZ,LED_DMA,LED_INVERT,LED_BRIGHTNESS,LED_CHANNEL)
        self.enpin=EN_PIN

    ##################################################
    # FUNCTIONS
    ##################################################
    def show(self):
        GPIO.output(self.enpin, GPIO.LOW)
        super().show()
        time.sleep(0.005)
        GPIO.output(self.enpin, GPIO.HIGH)

    def full(self,color):
        for n in range(self.numPixels()):
            self.setPixelColor(n,color)
        self.show()

    def full_set(self,color):
        for n in range(self.numPixels()):
            self.setPixelColor(n,color)

    def dot(self,color,turns,speed,length):
        self.full(off)
        for t in range(turns):
            n=self.numPixels()
            while n<(2*self.numPixels()):
                self.setPixelColor(n%self.numPixels(),color)
                self.setPixelColor((n-length)%self.numPixels(),off)
                self.show()
                time.sleep(float(1)/speed)
                n+=1
        self.full(off)

    #CIRCLE
    def circle(self,turns,speed):
        for t in range(turns):
            for s in range(int(float(1530)/speed)):
                for n in range(self.numPixels()):
                    for i in range(speed):
                        self.setfade(n)
                self.show()
                time.sleep(0.01)

    #SETFADE
    def setfade(self,n):
        g=(self.getPixelColor(n)>>16)&255
        r=(self.getPixelColor(n)>>8)&255
        b=self.getPixelColor(n)&255
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
        self.setPixelColor(n,Color(g,r,b))

    #RAINBOW
    def rainbow(self):
        for n in range(self.numPixels()):
            i=int((float(n)/(self.numPixels()-1))*1529)
            if i>=0 and i<=254:
                self.setPixelColor(n,Color(0,255,i%255))
            elif i<=509:
                self.setPixelColor(n,Color(0,255-(i%255),255))
            elif i<=764:
                self.setPixelColor(n,Color(i%255,0,255))
            elif i<=1019:
                self.setPixelColor(n,Color(255,0,255-(i%255)))
            elif i<=1274:
                self.setPixelColor(n,Color(255,i%255,0))
            elif i<=1529:
                self.setPixelColor(n,Color(255-(i%255),255,0))
        self.show()

    def breatheval(x):
        return 255*(x**4)

    def breathe(self,turns,speed,hold,pause):
        for t in range(turns):
            i=float(0)
            while breatheval(i)<255:
                #print i,"-",breatheval(i),"-",int(breatheval(i))
                self.setBrightness(int(breatheval(i)))
                self.show()
                i=i+0.001*speed
                time.sleep(0.01)
            self.setBrightness(255)
            self.show()
            time.sleep(hold)
            i=i-0.001*speed
            while i>=0:
                #print i,"-",breatheval(i),"-",int(breatheval(i))
                self.setBrightness(int(breatheval(i)))
                self.show()
                i=i-0.001*speed
                time.sleep(0.01)
            self.setBrightness(0)
            self.show()
            time.sleep(pause)

##################################################
# MAIN
##################################################
def main():
    window = LedStrip(76,18,800000,10,False,255,0,5)
    logo = LedStrip(9,18,800000,10,False,255,0,6)
    button = LedStrip(2,18,800000,10,False,255,0,13)
    gpu = LedStrip(4,18,800000,10,False,255,0,19)
    window.begin()
    logo.begin()
    button.begin()
    gpu.begin()

##################################################
    gpu.setBrightness(125)
    gpu.full(red)
    time.sleep(1)
    gpu.full(off)
##################################################
#quit
if __name__=="__main__":
    main()

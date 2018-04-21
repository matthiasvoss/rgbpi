import time
from neopixel import Adafruit_NeoPixel
import colorsys
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


class Color:
    _rgb255 = None

    def __init__(self, rgb255=None, rgb=None, bit24=None, hsv=None):
        # Check that only 1 value is given
        if sum(bool(e) for e in (rgb255, rgb, bit24, hsv)) != 1:
            raise ValueError('Initialize a new Color with only a single color format!')

        # Convert to internal rgb255 representation
        if rgb255:
            self._rgb255 = rgb255
        elif rgb:
            self._rgb255 = self.rgb_to_rgb255(rgb)
        elif bit24:
            self._rgb255 = self.bit24_to_rgb255(bit24)
        elif hsv:
            self._rgb255 = self.hsv_to_rgb255(hsv)

    @classmethod
    def rgb255_to_rgb(cls, rgb255):
        return [c/255 for c in rgb255]

    @classmethod
    def rgb_to_rgb255(cls, rgb):
        return [int(round(c*255)) for c in rgb]

    @classmethod
    def rgb255_to_bit24(cls, rgb255):
        return (rgb255[0] << 16) | (rgb255[1] << 8) | rgb255[2]

    @classmethod
    def bit24_to_rgb255(cls, bit24):
        return (bit24 >> 8) & 255, (bit24 >> 16) & 255, bit24 & 255

    @classmethod
    def rgb255_to_hsv(cls, rgb255):
        return colorsys.rgb_to_hsv(*cls.rgb255_to_rgb(rgb255))

    @classmethod
    def hsv_to_rgb255(cls, hsv):
        return cls.rgb_to_rgb255(colorsys.hsv_to_rgb(*hsv))

    @property
    def rgb255(self):
        return self._rgb255

    @property
    def rgb(self):
        return self.rgb255_to_rgb(self._rgb255)

    @property
    def bit24(self):
        return self.rgb255_to_bit24(self._rgb255)

    @property
    def hsv(self):
        return self.rgb255_to_hsv(self._rgb255)


##################################################
# COLORS
##################################################
red = Color(rgb255=(0, 255, 0))
green = Color(rgb255=(255, 0, 0))
blue = Color(rgb255=(0, 0, 255))
cyan = Color(rgb255=(255, 0, 255))
yellow = Color(rgb255=(255, 255, 0))
purple = Color(rgb255=(0, 255, 255))
white = Color(rgb255=(255, 255, 255))
off = Color(rgb255=(0, 0, 0))


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
        self.full_set(color)
        self.show()

    def full_set(self,color):
        for n in range(self.numPixels()):
            self.setPixelColor(n,color)

    def dot(self,color,turns,speed,length):
        self.full(off)
        for t in range(turns):
            for n in range(self.numPixels()):
                self.setPixelColor(n,color)
                self.setPixelColor(n-length,off)
                self.show()
                time.sleep(1./speed)
            self.full(off)

    #CIRCLE
    def circle(self,turns,speed):
        hsv=[whatever_to_hsv(self.getPixelColor(n)) for n in range(self.numPixels())]
        #print(hsv)
        steps=int(turns*(1/speed))
        for s in range(steps):
            for n,c in enumerate(hsv):
                c[0]+=speed
                self.setPixelColor(n,hsv_to_whatever(c))
            self.show()
            time.sleep(0.01)
                    
                
           

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
            while self.breatheval(i)<255:
                #print i,"-",breatheval(i),"-",int(breatheval(i))
                self.setBrightness(int(self.breatheval(i)))
                self.show()
                i=i+0.001*speed
                time.sleep(0.01)
            self.setBrightness(255)
            self.show()
            time.sleep(hold)
            i=i-0.001*speed
            while i>=0:
                #print i,"-",breatheval(i),"-",int(breatheval(i))
                self.setBrightness(int(self.breatheval(i)))
                self.show()
                i=i-0.001*speed
                time.sleep(0.01)
            self.setBrightness(0)
            self.show()
            time.sleep(pause)

def whatever_to_rgb(whatever):
    rgb=[(whatever>>8)&255,(whatever>>16)&255,whatever&255]
    return rgb

def whatever_to_hsv(whatever):
    rgb=whatever_to_rgb(whatever)
    rgb=[c/255 for c in rgb]
    return list(colorsys.rgb_to_hsv(*rgb))

def hsv_to_whatever(hsv):
    rgb=colorsys.hsv_to_rgb(*hsv)
    rgb=[int(round(c*255)) for c in rgb]
    grb=[rgb[1],rgb[0],rgb[2]]
    whatever=Color(*grb)
    return whatever
    
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
    logo.full(yellow)
    logo.circle(5,0.07)
    #logo.circle1(1,10)
    time.sleep(3)
    logo.full(off)
##################################################
#quit
if __name__=="__main__":
    main()

import time
from flask import Flask
from rgbpi.controller.strip3 import LedStrip, full, red, off, pin_logo

app = Flask(__name__)
logo = LedStrip(9,18,800000,10,False,255,0,pin_logo)


@app.route("/")
def hello():
    for n in range (3):
        logo.begin()
        full(logo,red)
        time.sleep(0.2)
        full(logo,off)
        time.sleep(0.2)
    return "Hello World!"

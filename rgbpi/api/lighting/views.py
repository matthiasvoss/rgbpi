from flask import Blueprint, current_app
import time

from rgbpi.controller.strip3 import LedStrip, full, red, off, pin_logo

blueprint = Blueprint('lighting', __name__, url_prefix='/lighting')

@blueprint.route("/")
def hello():
    strips = current_app.strips
    for n in range(3):
        strips['logo'].begin()
        full(strips['logo'], red)
        time.sleep(0.2)
        full(strips['logo'], off)
        time.sleep(0.2)
    return "Hello World!"

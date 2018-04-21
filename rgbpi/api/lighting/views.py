from flask import Blueprint, current_app
import time

from rgbpi.controller.strip import red, off

blueprint = Blueprint('lighting', __name__, url_prefix='/lighting')

@blueprint.route("/")
def hello():
    strips = current_app.strips
    for n in range(3):
        strips['logo'].begin()
        strips['logo'].full(red)
        time.sleep(0.2)
        strips['logo'].full(off)
        time.sleep(0.2)
    return "Hello World!"

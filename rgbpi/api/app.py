import time
from flask import Flask

from rgbpi.api import lighting
from rgbpi.controller.strip3 import LedStrip, pin_logo


def create_app(config_object=None):
    app = Flask(__name__.split('.')[0])
    app.config.from_object(config_object)

    # Create LED Strips
    strips = dict()
    strips['logo'] = LedStrip(9, 18, 800000, 10, False, 255, 0, pin_logo)

    app.strips = strips

    # Register blueprints
    app.register_blueprint(lighting.views.blueprint)

    return app

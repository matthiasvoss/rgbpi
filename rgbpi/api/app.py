import time
from flask import Flask

from rgbpi.api import lighting
from rgbpi.controller.strip import LedStrip


def create_app(config_object=None):
    app = Flask(__name__.split('.')[0])
    app.config.from_object(config_object)

    # Create LED Strips
    strips = dict()
    strips['window'] = LedStrip(76, 18, 800000, 10, False, 255, 0, 5)
    strips['logo'] = LedStrip(9, 18, 800000, 10, False, 255, 0, 6)
    strips['button'] = LedStrip(2, 18, 800000, 10, False, 255, 0, 13)
    strips['gpu'] = LedStrip(4, 18, 800000, 10, False, 255, 0, 19)

    app.strips = strips

    # Register blueprints
    app.register_blueprint(lighting.views.blueprint)

    return app

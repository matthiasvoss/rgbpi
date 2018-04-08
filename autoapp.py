"""Create an application instance."""
from flask.helpers import get_debug_flag

from rgbpi.api.app import create_app
from rgbpi.api.settings import DevConfig, ProdConfig

CONFIG = DevConfig if get_debug_flag() else ProdConfig

app = create_app(CONFIG)

import unittest

from rgbpi.controller.color import Color


class ColorInitTest(unittest.TestCase):
    target_rgb255 = (255, 0, 0)

    def test_rgb255_init(self):
        rgb255 = (255, 0, 0)
        self.assertTupleEqual(self.target_rgb255, Color(rgb255=rgb255)._rgb255)
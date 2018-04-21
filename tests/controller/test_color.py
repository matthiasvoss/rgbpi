import unittest

from rgbpi.controller.color import Color


class ColorInitTest(unittest.TestCase):
    target_rgb255 = (255, 0, 0)

    def test_rgb255_init(self):
        color = (255, 0, 0)
        self.assertTupleEqual(self.target_rgb255, Color(rgb255=color)._rgb255)

    def test_rgb_init(self):
        color = (1., 0, 0)
        self.assertTupleEqual(self.target_rgb255, Color(rgb=color)._rgb255)

    def test_hsv_init(self):
        color = (0, 1., 1.)
        self.assertTupleEqual(self.target_rgb255, Color(hsv=color)._rgb255)

    def test_bit24_init(self):
        color = 16711680
        self.assertEqual(self.target_rgb255, Color(bit24=color)._rgb255)


class ColorConversionTest(unittest.TestCase):
    init_rgb255 = (255, 0, 0)

    def setUp(self):
        self.color = Color(rgb255=self.init_rgb255)

    def test_rgb255(self):
        self.assertTupleEqual(self.color.rgb255, (255, 0, 0))

    def test_rgb_init(self):
        color = (1., 0, 0)
        self.assertTupleEqual(self.color.rgb, (1, 0, 0))

    def test_hsv_init(self):
        color = (0, 1., 1.)
        self.assertTupleEqual(self.color.hsv, (0, 1., 1.))

    def test_bit24_init(self):
        self.assertEqual(self.color.bit24, 16711680)
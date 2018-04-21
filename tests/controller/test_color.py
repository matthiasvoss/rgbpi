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

    def test_grb_init(self):
        color = (0, 1., 0)
        self.assertEqual(self.target_rgb255, Color(grb=color)._rgb255)

    def test_grb255_init(self):
        color = (0, 255, 0)
        self.assertEqual(self.target_rgb255, Color(grb255=color)._rgb255)

    def test_bit24_grb_init(self):
        color = 65280
        self.assertEqual(self.target_rgb255, Color(bit24_grb=color)._rgb255)

    def test_no_value_init(self):
        with self.assertRaises(ValueError):
            Color()

    def test_two_value_init(self):
        with self.assertRaises(ValueError):
            Color(rgb=1, rgb255=1)


class ColorConversionTest(unittest.TestCase):
    init_rgb255 = (255, 0, 0)

    def setUp(self):
        self.color = Color(rgb255=self.init_rgb255)

    def test_rgb255(self):
        self.assertTupleEqual(self.color.rgb255, (255, 0, 0))

    def test_rgb(self):
        color = (1., 0, 0)
        self.assertTupleEqual(self.color.rgb, (1, 0, 0))

    def test_hsv(self):
        color = (0, 1., 1.)
        self.assertTupleEqual(self.color.hsv, (0, 1., 1.))

    def test_bit24(self):
        self.assertEqual(self.color.bit24, 16711680)

    def test_grb(self):
        self.assertTupleEqual(self.color.grb, (0, 1., 0))

    def test_grb255(self):
        self.assertTupleEqual(self.color.grb255, (0, 255, 0))

    def test_bit24_grb(self):
        self.assertEqual(self.color.bit24_grb, 65280)

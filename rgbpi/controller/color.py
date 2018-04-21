import colorsys


class Color:
    _rgb255 = None

    def __init__(self, rgb255=None, rgb=None, grb255=None, grb=None, bit24=None, bit24_grb=None, hsv=None):
        # Check that only 1 value is given
        if sum(bool(e) for e in (rgb255, rgb, bit24, hsv, grb, grb255, bit24_grb)) != 1:
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
        elif grb:
            self._rgb255 = self.grb_to_rgb255(grb)
        elif grb255:
            self._rgb255 = self.grb255_to_rgb255(grb255)
        elif bit24_grb:
            self._rgb255 = self.bit24_grb_to_rgb255(bit24_grb)

    @classmethod
    def rgb255_to_rgb(cls, rgb255):
        return tuple(c/255 for c in rgb255)

    @classmethod
    def rgb_to_rgb255(cls, rgb):
        return tuple(int(round(c*255)) for c in rgb)

    @classmethod
    def rgb255_to_bit24(cls, rgb255):
        return (rgb255[0] << 16) | (rgb255[1] << 8) | rgb255[2]

    @classmethod
    def bit24_to_rgb255(cls, bit24):
        return (bit24 >> 16) & 255, (bit24 >> 8) & 255, bit24 & 255

    @classmethod
    def rgb255_to_hsv(cls, rgb255):
        return colorsys.rgb_to_hsv(*cls.rgb255_to_rgb(rgb255))

    @classmethod
    def hsv_to_rgb255(cls, hsv):
        return cls.rgb_to_rgb255(colorsys.hsv_to_rgb(*hsv))

    @classmethod
    def rgb255_to_grb255(cls, rgb255):
        return rgb255[1], rgb255[0], rgb255[2]

    @classmethod
    def grb255_to_rgb255(cls, grb255):
        return cls.rgb255_to_grb255(grb255)

    @classmethod
    def rgb255_to_grb(cls, rgb255):
        return cls.rgb255_to_rgb(cls.rgb255_to_grb255(rgb255))

    @classmethod
    def grb_to_rgb255(cls, grb):
        return cls.grb255_to_rgb255(cls.rgb_to_rgb255(grb))

    @classmethod
    def rgb255_to_bit24_grb(cls, rgb255):
        return cls.rgb255_to_bit24(cls.rgb255_to_grb255(rgb255))

    @classmethod
    def bit24_grb_to_rgb255(cls, bit24_grb):
        return cls.rgb255_to_grb255(cls.bit24_to_rgb255(bit24_grb))

    @property
    def rgb255(self):
        return self._rgb255

    @property
    def rgb(self):
        return self.rgb255_to_rgb(self._rgb255)

    @property
    def grb(self):
        return self.rgb255_to_grb(self.rgb255)

    @property
    def grb255(self):
        return self.rgb255_to_grb255(self.rgb255)

    @property
    def bit24(self):
        return self.rgb255_to_bit24(self._rgb255)

    @property
    def bit24_grb(self):
        return self.rgb255_to_bit24_grb(self._rgb255)

    @property
    def hsv(self):
        return self.rgb255_to_hsv(self._rgb255)
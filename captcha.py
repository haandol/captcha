# coding: utf-8

import os
import random
import Image
import ImageDraw
import ImageFont
from tempfile import NamedTemporaryFile

PWD = os.getcwd()
SEP = os.path.sep
FONT_FILE = SEP.join([PWD, "veramono.ttf"])
FONT_SIZE = 35
POOL = 'acbdefghijklmnopqrstuvwxyz1234567890'

LENGTH = 6
WIDTH = 135
HEIGHT = 50

R = 00
G = 39
B = 50


def generate_captcha(PATH=PWD):
    """Author:
        haandol <ldg55d@gmail.com>

    Parameters:
        PATH - path to where captha image will be stored

    Description:
        using PIL, generate captcha image and its value and return them.
        generated captha image is not encrypted,
        this module simply generate a image for the random character value
        if you want to encrypting captcha library,
        you should find other library like python-recaptcha or something.
    """
    with NamedTemporaryFile(suffix='.jpg', dir=PATH, delete=False) as fp:
        im = Image.new("RGB", (WIDTH, HEIGHT), (R, G, B))
        draw = ImageDraw.Draw(im)
        font = ImageFont.truetype(FONT_FILE, FONT_SIZE, encoding='unic')

        value = ''.join(random.sample(POOL, LENGTH))
        draw.text((5, 1), value, font=font)

        im.save(fp.name)
        return im, value

if __name__ == '__main__':
    print generate_captcha()

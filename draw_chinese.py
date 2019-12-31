#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 21:06:18 2019

@author: xzfang
"""
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
# image = "sample-out.png"
# img = Image.open(image)
# draw = ImageDraw.Draw(img)
# font = ImageFont.truetype(<font-file>, <font-size>)
# font = ImageFont.truetype("sans-serif.ttf", 16)
font0 = ImageFont.truetype("/Library/Fonts/Arial Unicode.ttf", 80)
#font0 = ImageFont.truetype("/Library/Fonts/Arial.ttf", 80)
#        font0 = ImageFont.truetype("/Library/Fonts/simsum.ttc", 80)
width1 = 80
width2 = 900
height = 1900

cur_img = Image.open('sample-out.png')
a = '喜欢啊'
draw = ImageDraw.Draw(cur_img)
#            draw.text((width1, height), iRow.agent_in_picture, color0, font=font0)
#            draw.text((width2, height), iRow.patient_in_picture, color0, font=font0)
#            draw.text((width1, height), iRow.agent_in_picture, fill=(0,0,0), font=font0)
draw.text((width1, height), a, fill=(0,0,0,0), font=font0)

#draw.text((width2, height), iRow.patient_in_picture, fill=(0,0,0), font=font0)
cur_img.save('sample-chinese.png')
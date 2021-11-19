# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 14:43:59 2021

@author: ziac
"""

'''
import colorgram

colors = colorgram.extract('hirst.jpg', 30)
colors_list = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    if r <210 and g<210 and b<210:
        colors_list.append(new_color)
    '''

colors_list = [(201, 164, 112), (152, 75, 49), (171, 153, 42), (56, 95, 126), (139, 31, 19), (134, 163, 184), (197, 93, 73), (48, 121, 88), (98, 75, 77), (142, 178, 148), (75, 41, 33), (165, 145, 156), (15, 99, 71), (54, 45, 47), (32, 61, 77), (145, 21, 25), (21, 83, 89), (182, 205, 175), (85, 147, 127), (44, 66, 87), (178, 94, 98), (8, 68, 51), (108, 127, 151)]

import turtle as t
import random

t.colormode(255)
t.speed(0)

y = -200

for i in range(10):
    x = -200
    for j in range(10):
        t.penup()
        t.goto(x, y)
        c = random.randrange(len(colors_list))
        t.color(colors_list[c], colors_list[c])
        t.pendown()
        t.begin_fill()
        t.circle(10)
        t.end_fill()
        x += 40
    y += 40

t.hideturtle()
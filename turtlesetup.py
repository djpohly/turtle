from turtle import *
# XXX These use radians, so it would be confusing to tell anyone about them for now
from math import *
import time
import random as _random
import itertools
import readline
import rlcompleter

# Tab-completion fix found at https://stackoverflow.com/questions/35115208
readline.parse_and_bind("tab: complete")
readline.set_completer(rlcompleter.Completer(locals()).complete)

# Prep for responding to input
listen()

# New functions
def random(n):
    return _random.randint(1, n)

def randomcolor():
    return _random.random(), _random.random(), _random.random()

def wait(tenths):
    time.sleep(tenths/10)

# Fix turtle redrawing on clearscreen()
__oldclearscreen = clearscreen
def clearscreen():
    __oldclearscreen()
    isvisible()

clearscreen()

# Function aliases
cs = clearscreen
pc = pencolor
fc = fillcolor
bg = bgcolor
ps = pensize
arc = circle

# Overrides for "degree mode"
acos_rad = acos
asin_rad = asin
atan_rad = atan
atan2_rad = atan2

def acos(x):
    return degrees(acos_rad(x))
def asin(x):
    return degrees(asin_rad(x))
def atan(x):
    return degrees(atan_rad(x))
def atan2(y, x):
    return degrees(atan2_rad(y, x))

cos_rad = cos
sin_rad = sin
tan_rad = tan

def cos(x):
    return cos_rad(radians(x))
def sin(x):
    return sin_rad(radians(x))
def tan(x):
    return tan_rad(radians(x))

# Handlers for new blocks
class Filled:
    def __init__(self, *args):
        self.color = args

    def __enter__(self, *args):
        if filling():
            raise SyntaxError("cannot have two filled blocks at the same time")
        begin_fill()

    def __exit__(self, t, val, tb):
        oldfill = fillcolor()
        if self.color:
            fillcolor(*self.color)
        end_fill()
        fillcolor(oldfill)

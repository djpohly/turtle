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

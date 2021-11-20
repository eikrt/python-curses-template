import time
from datetime import datetime
import curses
import math
from curses import wrapper
import random
import re
from .settings import settings
from .state import state
from .settings import Color
from .settings import scr
from .utils import utils
class Entity:
    def __init__(self, x: float, y: float, color: Color, symbol: str, id: str, cbox_w: float, cbox_h: float):
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0
        self.color = color
        self.symbol = symbol
        self.id = id
        self.dir = -math.pi/4
        self.speed = 10
        self.dead = False
        self.cbox_w=cbox_w
        self.cbox_h=cbox_h
        self.tickcd = 15
        self.ticktime = 0
        self.buffer_size = 0.2
    def draw(self, stdscr):
        utils.draw(stdscr, self.x, self.y, self.symbol, self.color)
    def move(self, delta):
        self.ticktime -= 1
        self.x += (math.cos(self.dir) * self.speed * delta) / 1000
        self.y += (math.sin(self.dir) * self.speed * delta) / 1000
    def collision(self, other):
        pass
        

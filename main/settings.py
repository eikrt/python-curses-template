from enum import Enum

settings = {'w':70, 'h':25, 'mute':True}
class Color(Enum):
    YELLOW = 1
    RED = 2
    YELLOW_2 = 3
    CYAN = 4
    MAGENTA = 5
    BLUE = 6
    GREEN = 7
    BLACK = 8
    WHITE = 9
class Scr:
    def __init__(self):
        self.margin_x = 0
        self.margin_y = 0
    def update_margins(self,stdscr: object):
        margin_y, margin_x = stdscr.getmaxyx()
        self.margin_x = margin_x / 2 - settings['w'] / 2
        self.margin_y = margin_y / 2 - settings['h'] / 2
scr = Scr()

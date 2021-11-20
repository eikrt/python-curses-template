import os
import curses
from .settings import Color
from .settings import scr 
from .utils import utils
menu_selection = 0

def menu_show(main,stdscr, key):
    global menu_selection
    if key == curses.KEY_UP:
        if menu_selection >= 1:
            menu_selection -= 1
    elif key == curses.KEY_DOWN:
        if menu_selection <= 0:
            menu_selection += 1


import time
from datetime import datetime
import curses
from curses import wrapper
import math
import random
from .world import Entity
from .settings import Color
from .settings import settings
from .menu import menu_show
from .utils import utils
from .state import state
from .utils import scr
class Main:
    def __init__(self):
        self.running = True
        stdscr = curses.initscr()
        curses.curs_set(0)
        curses.noecho()
        curses.cbreak()
        stdscr.nodelay(1)
        curses.endwin()
        curses.start_color()
        stdscr.idcok(False)
        stdscr.idlok(False)
        curses.init_pair(Color.YELLOW.value, curses.COLOR_YELLOW, curses.COLOR_BLACK)
        curses.init_pair(Color.RED.value, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(Color.YELLOW.value, curses.COLOR_YELLOW, curses.COLOR_BLACK)
        curses.init_pair(Color.CYAN.value, curses.COLOR_CYAN, curses.COLOR_BLACK)
        curses.init_pair(Color.MAGENTA.value, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
        curses.init_pair(Color.BLUE.value, curses.COLOR_BLUE, curses.COLOR_BLACK)
        curses.init_pair(Color.GREEN.value, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(Color.BLACK.value, curses.COLOR_BLACK, curses.COLOR_WHITE)
        curses.init_pair(Color.WHITE.value, curses.COLOR_WHITE, curses.COLOR_BLACK)
        stdscr.keypad(1)
        curses.mousemask(1)
        global settings
        self.entities = []
        self.menu_on = True
        self.loop(stdscr)
        wrapper(self.loop)

    def loop(self, stdscr):
        old_time = None
        menu_selection = 0
        delta = 10
        while(self.running):

            key = stdscr.getch() 
            stdscr.erase()
            

            new_time = datetime.now()
            
            if old_time != None:
                delta = (new_time.microsecond - old_time.microsecond) /1000
            if delta < 10:
                delta = 10

            
            if key == ord('q'):
                self.running = False
            if self.menu_on:
                menu_show(self, stdscr, key)
            elif not self.menu_on:


                if key == curses.KEY_LEFT:
                    pass
                elif key == curses.KEY_RIGHT:
                    pass
                elif key == ord(' '):
                    pass
                for e in self.entities:
                    e.draw(stdscr)
            
            utils.draw(stdscr, 3,2,f"Score: {state['score']}", Color.WHITE)
            for x in range(settings['w']):

                utils.draw(stdscr, x,0,'\u2593', Color.WHITE)

            for y in range(settings['h']):

                utils.draw(stdscr, 0,y,'\u2593', Color.WHITE)

            for x in range(settings['w']):

                utils.draw(stdscr, x,settings['h'],'\u2593', Color.WHITE)

            for y in range(settings['h']+1):

                utils.draw(stdscr, settings['w'],y,'\u2593', Color.WHITE)

            scr.update_margins(stdscr)
            stdscr.refresh()

            old_time = datetime.now()
            time.sleep(0.05)
        curses.endwin()


def main():
        main = Main()


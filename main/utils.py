from playsound import playsound
from .settings import settings
import curses
import os
from sys import platform
from .settings import scr
class Utils:
    def psound(self, url: str, block: bool):
        if not settings['mute']:
            try:
                if platform == "linux" or platform == "linux2":
                    os.system("play " + os.path.abspath(url) + " > /dev/null 2>&1 &")
                elif platform == "darwin":
                    os.system("play " + os.path.abspath(url) + " > /dev/null 2>&1 &")
                elif platform == "win32":
                    playsound(os.path.abspath(url), block)
            except:
                pass


    def draw(self, stdscr, x, y, content, color):
        try:
            stdscr.addstr(int(scr.margin_y + y), int(scr.margin_x + x), content, curses.color_pair(color.value))
        except curses.error:
            pass
utils = Utils()

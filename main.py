#!/usr/bin/python3

from graphics import Window
from maze import Maze


def main():
    win = Window(900, 900)
    maze = Maze(50,50,10,10,40,40,win,0)
    win.wait_for_close()

if __name__ == "__main__":
    main()


    
#!/usr/bin/python3

from graphics import Window
from maze import Maze


def main():
    win = Window(900, 900)
    maze = Maze(50,50,20,20,40,40,win)
    print("Solved the maze?" + str(maze.solve()))
    win.wait_for_close()

if __name__ == "__main__":
    main()


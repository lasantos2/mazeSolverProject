#!/usr/bin/python3
from tkinter import Tk, BOTH, Canvas
import time

from maze import Maze

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.geometry("{0}x{1}".format(width, height))
        self.__root.title = "Window"
        self.__canvas = Canvas(self.__root,width=width,height=height)
        self.__canvas.pack()
        self.__is_running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        


    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__is_running = True
        while self.__is_running:
            self.redraw()

    def close(self):
        self.__is_running = False

    def draw_line(self, line_instance, fill_color):
        line_instance.draw(self.__canvas, fill_color)

def main():
    win = Window(900, 900)

    maze = Maze(50,50,3,3,40,40,win)


    win.wait_for_close()

if __name__ == "__main__":
    main()


    
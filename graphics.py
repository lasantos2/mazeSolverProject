
from tkinter import Tk, BOTH, Canvas

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


class Point:
    def __init__(self, x = 0, y = 0):
        self.x_ = x
        self.y_ = y

class Line:
    def __init__(self, point1, point2):
        self.__point1 = point1
        self.__point2 = point2

    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.__point1.x_, 
            self.__point1.y_, 
            self.__point2.x_, 
            self.__point2.y_, 
            fill=fill_color, 
            width=2
        )

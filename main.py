#!/usr/bin/python3
from tkinter import Tk, BOTH, Canvas


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

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title = "Window"
        self.__canvas = Canvas()
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


class Cell:
    def __init__(self, window, point1=Point(), point2=Point()):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

        self._x1 = point1.x_
        self._x2 = point2.x_
        self._y1 = point1.y_
        self._y2 = point2.y_
        self._win = window

    def draw(self):
        top_left = Point(self._x1, self._y2)
        bottom_left = Point(self._x1,self._y1)
        bottom_right = Point(self._x2,self._y1)
        top_right = Point(self._x2, self._y2)

        if self.has_left_wall:
            line = Line(top_left, bottom_left)
            self._win.draw_line(line,"Black")

        if self.has_right_wall:
            line = Line(top_right, bottom_right)
            self._win.draw_line(line,"Black")

        if self.has_top_wall:
            line = Line(top_left, top_right)
            self._win.draw_line(line,"Black")

        if self.has_bottom_wall:
            line = Line(bottom_left, bottom_right)
            self._win.draw_line(line,"Black")

    def draw_move(self, to_cell, undo=False):
        line_color = "Red"
        if undo:
            line_color = "Gray"

        mid_point = Point((self._x2 + self._x1)/2, (self._y1 + self._y2) / 2)

        to_cell_midPoint = Point((to_cell._x2 + to_cell._x1) / 2, (to_cell._y1 + to_cell._y2)/2)

        line_to_cell = Line(mid_point, to_cell_midPoint)
        self._win.draw_line(line_to_cell,line_color)

        

        


def main():
    win = Window(800, 600)

    cell_hor = 3
    

    #draw line
    point1_ = Point(10, 10)
    point2_ = Point(40,40)

    cell1 = Cell(win, point1_, point2_)
    cell1.has_right_wall = False
    cell1.draw()

    point1_ = Point(50, 10)
    point2_ = Point(80, 40)
    cell2 = Cell(win, point1_, point2_)
    cell2.has_left_wall = False
    cell2.has_right_wall = False
    cell2.draw()

    cell1.draw_move(cell2)

    win.wait_for_close()




if __name__ == "__main__":
    main()


    
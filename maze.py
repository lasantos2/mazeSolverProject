import time
from graphics import *

class Cell:
    def __init__(self, window = None, point1=Point(), point2=Point()):
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
            if self._win != None:
                self._win.draw_line(line,"Black")

        if self.has_right_wall:
            line = Line(top_right, bottom_right)
            if self._win != None:
                self._win.draw_line(line,"Black")

        if self.has_top_wall:
            line = Line(top_left, top_right)
            if self._win != None:
                self._win.draw_line(line,"Black")

        if self.has_bottom_wall:
            line = Line(bottom_left, bottom_right)
            if self._win != None:
                self._win.draw_line(line,"Black")

    def draw_move(self, to_cell, undo=False):
        line_color = "Red"
        if undo:
            line_color = "Gray"

        mid_point = Point((self._x2 + self._x1)/2, (self._y1 + self._y2) / 2)

        to_cell_midPoint = Point((to_cell._x2 + to_cell._x1) / 2, (to_cell._y1 + to_cell._y2)/2)

        line_to_cell = Line(mid_point, to_cell_midPoint)
        if self._win != None:
            self._win.draw_line(line_to_cell,line_color)

class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win = None ):
            
            self._x1 = x1         
            self._y1 = y1
            self._num_rows = num_rows
            self._num_cols = num_cols
            self._cell_size_x = cell_size_x
            self._cell_size_y = cell_size_y
            self._win = win

            self._create_cells()

    def _create_cells(self):
        self._cells = []

        for i in range(self._num_cols):
            self._cells.append([])
            for j in range(self._num_rows):
                self._cells[i].append("cell")
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):

        if self._win is None:
            return
        currcel_x = self._x1 + (self._cell_size_x) * i
        curr_cell_y = self._y1 + (self._cell_size_y) * j

        curr_point_top_left = Point(currcel_x, curr_cell_y + self._cell_size_y)
        curr_point_bottom_right = Point(currcel_x + self._cell_size_x, curr_cell_y)

        curr_cell = Cell(self._win, curr_point_top_left, curr_point_bottom_right)

        self._cells[i][j] = curr_cell
        self._cells[i][j].draw()

        # print("columns: " + str(len(self._cells)))
        # print("row: " + str(len(self._cells[i])))

        self._animate()


    def _animate(self):
        if self._win != None:
            self._win.redraw()
            time.sleep(0.05)
    

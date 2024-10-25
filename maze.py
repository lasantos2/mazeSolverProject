import time
from graphics import *

class Cell:
    def __init__(self, window = None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = window
        

    def draw(self,x1,y1,x2,y2):


        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2

        top_left = Point(x1, y1)
        bottom_left = Point(x1,y2)
        bottom_right = Point(x2,y2)
        top_right = Point(x2, y1)

        if self._win == None:
            return

        if self.has_left_wall:
            line = Line(top_left, bottom_left)
            self._win.draw_line(line,"Black")
        else:
            line = Line(top_left, bottom_left)
            self._win.draw_line(line,"#D8D9D8")

        if self.has_right_wall:
            line = Line(top_right, bottom_right)

            self._win.draw_line(line,"Black")
        else:
            line = Line(top_right, bottom_right)
            self._win.draw_line(line,"#D8D9D8")

        if self.has_top_wall:
            line = Line(top_left, top_right)

            self._win.draw_line(line,"Black")
        else:
            line = Line(top_left, top_right)
            self._win.draw_line(line,"#D8D9D8")

        if self.has_bottom_wall:
            line = Line(bottom_left, bottom_right)
            self._win.draw_line(line,"Black")
        else:
            line = Line(bottom_left, bottom_right)
            self._win.draw_line(line,"#D8D9D8")

    def draw_move(self, to_cell, undo=False):
        line_color = "Red"
        if undo:
            line_color = "#D8D9D8"

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
            self._cells = []

            self._create_cells()
            self._break_entrance_and_exit()

    def _create_cells(self):
        for i in range(self._num_cols):
            column_cells = []
            for j in range(self._num_rows):
                column_cells.append(Cell(self._win))
            self._cells.append(column_cells)

        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i,j)
        

    def _draw_cell(self, i, j):

        if self._win is None:
            return

        x1 = self._x1 + (self._cell_size_x) * i
        y1 = self._y1 + (self._cell_size_y) * j
        y2 = y1 + self._cell_size_y
        x2 = x1 + self._cell_size_x

        self._cells[i][j].draw(x1,y1,x2,y2)

        

        self._animate()

    def _break_entrance_and_exit(self):

        self._cells[0][0].has_top_wall = False
        self._draw_cell(0,0)

        self._cells[-1][-1].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1,self._num_rows - 1)


    def _animate(self):
        if self._win != None:
            self._win.redraw()
            time.sleep(0.05)
    

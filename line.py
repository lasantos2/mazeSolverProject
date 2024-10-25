

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

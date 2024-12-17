from tkinter import Canvas, BOTH, Tk


class Point:
    def __init__(self, x, y):
        self.x
        self.y


class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def draw(self, canvas_in, fill_color):
        canvas_in.create_line(self.point1.x, self.point1.y, self.point2.x, self.point2.y, fill_color, width=2)

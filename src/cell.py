from graphics import Point, Line

class Cell():
    def __init__(self):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = 0
        self._x1 = 0
        self._y2 = 0
        self._y2 = 0
        self._window = None

    def set_window(self, window):
        self._window = window
    
    def set_coordinates(self, x1, y1, x2, y2):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
    
    def draw(self):
        if self.has_left_wall:
            line_left = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
            self._window.draw_line(line_left)
        if self.has_right_wall:
            line_right = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
            self._window.draw_line(line_right)
        if self.has_top_wall:
            line_top = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            self._window.draw_line(line_top)
        if self.has_bottom_wall:
            line_bottom = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
            self._window.draw_line(line_bottom)
    
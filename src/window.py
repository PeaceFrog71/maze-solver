from tkinter import Tk, BOTH, Canvas
from drawables import Point, Line

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title = "Maze Solver"
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width,)
        self.__canvas.pack(fill=BOTH, expand=True)

        self._is_running = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        self._is_running = True
        while self._is_running:
            self.redraw()
        print("window closed...")

    def close(self):
        self._is_running = False

    def draw_line(self, line_in, fill_color):
        line_in.draw(self.__canvas, fill_color)
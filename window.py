from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(width, height):
        self.width = width
        self.height = height
        self.root_widget = Tk()
        self.root_widget.title = "root"
        self.canvas_widget = Canvas(self.root_widget)
        self.canvas_widget.pack()
        is_running = False
        
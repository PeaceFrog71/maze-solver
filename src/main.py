from window import Window
from drawables import Point, Line

def main():
    # Create Window
    win = Window(800, 600)
    
    # Create two points and a line
    start_point = Point(50, 50)
    end_point = Point(400, 300)
    new_line = Line(start_point, end_point)

    # Draw the line on the window
    win.draw_line(new_line, "green")

    # Keep the window open until close
    win.wait_for_close()



main()
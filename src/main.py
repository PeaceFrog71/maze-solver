from window import Window
from graphics import Point, Line

def main():
    # Create Window
    win = Window(800, 600)
    
    # Create two points and a line
    UL_outter = Point(50, 50)
    LL_outter = Point(50, 550)
    UL_inner = Point(360, 270)
    LL_inner = Point(360, 330)
    UL_line = Line(UL_outter, UL_inner)
    LL_line = Line(LL_outter, LL_inner)
    UR_outter = Point(750, 50)
    LR_outter = Point(750, 550)
    UR_inner = Point(440,270)
    LR_inner = Point(440, 330)
    UR_line = Line(UR_outter, UR_inner)
    LR_line = Line(LR_outter, LR_inner)
    top_inner = Line(UL_inner, UR_inner)
    bottom_inner = Line(LL_inner, LR_inner)
    left_inner = Line(UL_inner, LL_inner)
    right_inner = Line(UR_inner, LR_inner)

    # Draw the line on the window
    win.draw_line(UL_line, "green")
    win.draw_line(UR_line, "green")
    win.draw_line(LL_line, "green")
    win.draw_line(LR_line, "green")
    win.draw_line(top_inner)
    win.draw_line(bottom_inner)
    win.draw_line(left_inner)
    win.draw_line(right_inner)

    # Keep the window open until close
    win.wait_for_close()



main()
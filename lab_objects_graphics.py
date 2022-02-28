"""CSC 161 Lab: Objects & Graphics

Lihang Liu
Lab Section CSC 161-2 TR 2:00-3:15pm
Spring 2022
"""


from graphics import GraphWin, Text, Rectangle, Point, Line, Circle, Polygon


def main():
    win = GraphWin("Draw a house", 500, 500)
    message = Text(Point(win.getWidth()/2, 20),
                   'Click on lower left corner of the house frame.')
    message.setTextColor('black')
    message.setStyle('italic')
    message.setSize(15)
    message.draw(win)

    p1 = win.getMouse()
    p1.draw(win)

    message.setText('Click upper right corner of the house frame..')
    p2 = win.getMouse()
    p2.draw(win)

    frame = Rectangle(p1, p2)
    frame.draw(win)

    message.setText("Click on the center of the top of the door.")
    left_wid = p1.getX()
    right_wid = p2.getX()
    frame_wid = (right_wid - left_wid)
    door_wid = (frame_wid/5)
    door_rad = float(door_wid/2)

    p3 = win.getMouse()     # the center of the door
    p3_x = p3.getX()        # p3 x cord

    p4_x = (p3_x - door_rad)
    p5_x = (p3.x + door_rad)

    p3_y = (p3.getY())

    p4 = Point(p4_x, p3_y)  # left point of the top
    p5 = Point(p5_x, p3_y)  # right point
    door_top = Line(p4, p5)
    door_top.draw(win)

    # draw vertical line
    # firstly get the door bottom's y cood, so it would stop
    door_bot = p1.getY()

    door_len = (p3_y - door_bot)

    p6 = Point(p4_x, door_bot)  # The left corner of the door
    p7 = Point(p5_x, door_bot)  # The right corner of the door

    door_left = Line(p4, p6)
    door_right = Line(p5, p7)

    door_left.draw(win)
    door_right.draw(win)

    # draw the doorknob
    doorknob_height = (door_len/2) 
    doorknob_point_x = (p5_x - 15) 
    doorknob_point_y = (p3_y - doorknob_height)
    doorknob_point = Point(doorknob_point_x, doorknob_point_y)
    # Doorknob's center
    doorknob = Circle(doorknob_point, 5)
    doorknob.setFill("black")
    doorknob.draw(win)

    # Draw the window
    message.setText("Click on the center of the window.")
    window_wid = door_wid * (3/4) 
    window_rad = window_wid / 2 
    window_center = win.getMouse() 

    window_center_x = window_center.getX()
    window_center_y = window_center.getY()

    window_lower_left_x = window_center_x - window_rad
    window_lower_left_y = window_center_y + window_rad

    window_lower_left = Point(window_lower_left_x, window_lower_left_y)

    window_upper_right_x = window_center_x + window_rad
    window_upper_right_y = window_center_y - window_rad

    window_upper_right = Point(window_upper_right_x, window_upper_right_y)

    window = Rectangle(window_lower_left, window_upper_right)
    window.draw(win)

    # window's muntins
    window_left_mid = Point(window_lower_left_x,
                            window_lower_left_y - window_rad)

    window_right_mid = Point(window_upper_right_x,
                             window_upper_right_y + window_rad)

    window_hori_line = Line(window_left_mid, window_right_mid)
    window_hori_line.draw(win)

    window_upper_mid = Point(window_upper_right_x - window_rad,
                             window_upper_right_y)

    window_lower_mid = Point(window_lower_left_x + window_rad,
                             window_lower_left_y)

    window_verti_line = Line(window_upper_mid, window_lower_mid)
    window_verti_line.draw(win)

    # Draw the roof
    message.setText("Click on the peak of the roof.")
    roof_top = win.getMouse()
    frame_upper_left = Point(p1.getX(), p2.getY())
    roof = Polygon(frame_upper_left, p2, roof_top)
    roof.draw(win)

    message.setText("Click anywhere to quit.")
    win.getMouse()
    win.close()


if __name__ == '__main__':
    main()

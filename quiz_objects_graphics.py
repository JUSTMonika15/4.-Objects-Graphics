"""CSC 161 Quiz: Objects & Graphics

Lihang Liu
Lab Section TR 2:00-3:15pm
Spring 2022
"""

from graphics import Oval, Circle, GraphWin, Point


def main():
    win = GraphWin()
    face = Circle(Point(100, 100), 60)
    face.draw(win)

    left_eye = Circle(Point(75, 85), 15)
    right_eye = Circle(Point(125, 85), 15)
    left_eye.draw(win)
    right_eye.draw(win)

    mouth = Oval(Point(75, 125),
                 Point(125, 140))
    mouth.draw(win)


if __name__ == '__main__':
    main()

# @author yuu
# @date 2020/4/11

import turtle
import time

# macro for drawing
class Color:
    WHITE = '#FFFFFF'
    BLACK = '#000000'
    RED = '#FF0000'
    GREEN = '#00FF00'
    BLUE = '#0000FF'
    YELLOW = '#FFFF00'
    ORANGE = '#FF7F00'
    PURPLE = '#FF00FF'
    CYAN = '#00FFFF'
    GRAY = '#808080'
    LIGHT_GRAY = '#D3D3D3'
    DARK_GRAY = '#A9A9A9'
    PINK = '#FF69B4'
    BROWN = '#A52A2A'
    LIGHT_GREEN = '#90EE90'
    LIGHT_BLUE = '#ADD8E6'
    LIGHT_PINK = '#FFB6C1'
    LIGHT_ORANGE = '#FFA07A'
    LIGHT_PURPLE = '#EE82EE'
    LIGHT_CYAN = '#E0FFFF'
    LIGHT_BROWN = '#F5DEB3'
    DARK_GREEN = '#006400'
    DARK_BLUE = '#00008B'
    DARK_PINK = '#FF1493'
    DARK_ORANGE = '#FF8C00'
    DARK_PURPLE = '#800080'
    DARK_CYAN = '#008B8B'
    DARK_BROWN = '#8B4513'

    def getAll():
        return [Color.WHITE, Color.BLACK, Color.RED, Color.GREEN, Color.BLUE, Color.YELLOW, Color.ORANGE, Color.PURPLE, Color.CYAN, Color.GRAY, Color.LIGHT_GRAY, Color.DARK_GRAY, Color.PINK, Color.BROWN, Color.LIGHT_GREEN, Color.LIGHT_BLUE, Color.LIGHT_PINK, Color.LIGHT_ORANGE, Color.LIGHT_PURPLE, Color.LIGHT_CYAN, Color.LIGHT_BROWN, Color.DARK_GREEN, Color.DARK_BLUE, Color.DARK_PINK, Color.DARK_ORANGE, Color.DARK_PURPLE, Color.DARK_CYAN, Color.DARK_BROWN]

    def getAllWithout(color):
        return [c for c in Color.getAll() if c != color]
    
    def getAllWithouts(colors):
        return [c for c in Color.getAll() if c not in colors]

class Pen:
    def t():
        t = turtle.Turtle()
        return t
    
    def s():
        s = turtle.getscreen()
        return s

    def reset():
        turtle.reset()

    def up():
        turtle.penup()

    def down():
        turtle.pendown()

    def fd(distance):
        turtle.forward(distance)

    def l(angle):
        turtle.left(angle)

    def r(angle):
        turtle.right(angle)

    def fill(color):
        turtle.fillcolor(color)
        turtle.begin_fill()
    
    def color(color):
        turtle.color(color)

    def end_fill():
        turtle.end_fill()
    
    def seth(angle):
        turtle.seth(angle)
    
    def ht():
        turtle.ht()

    def circle(radius, color=None, steps=None):
        if steps is None:
            if color is None:
                turtle.circle(radius)
            else:
                turtle.fillcolor(color)
                turtle.begin_fill()
                turtle.circle(radius)
                turtle.end_fill()
        else:
            if color is None:
                turtle.circle(radius, steps)
            else:
                turtle.fillcolor(color)
                turtle.begin_fill()
                turtle.circle(radius, steps)
                turtle.end_fill()
    
    def triangle(pos: tuple, size: int, color: str):
        turtle.fillcolor(color)
        turtle.begin_fill()
        turtle.setpos(pos[0], pos[1])
        turtle.setpos(pos[0] + size, pos[1])
        turtle.setpos(pos[0] + size / 2, pos[1] + size)
        turtle.end_fill()
    
    def square(pos: tuple, size: int, color: str):
        turtle.fillcolor(color)
        turtle.begin_fill()
        turtle.setpos(pos[0], pos[1])
        turtle.setpos(pos[0] + size, pos[1])
        turtle.setpos(pos[0] + size, pos[1] + size)
        turtle.setpos(pos[0], pos[1] + size)
        turtle.end_fill()

    def sp(x, y):
        turtle.setpos(x, y)

p: Pen = Pen
sc: turtle.Screen = turtle.Screen()
sc.setup(width=600, height=600)
tt: turtle.Turtle = turtle.Turtle()
tt.pensize(2)
tt.speed(100)
n = -1
for angle in range(0, 360, 30):
    n =+ 1
    if n == 5:
        n =- 1
    colors: list = Color.getAllWithout(Color.WHITE)
    p.color(colors[n])
    p.seth(angle)
    p.circle(60)
p.up

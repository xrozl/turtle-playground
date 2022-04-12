# @author yuu
# @date 2020/4/12

import turtle

# macro for drawing
class Pen:
    def t():
        return turtle
    
    def s():
        s = turtle.getscreen()
        return s

# main function

# dot hash data
meta = [
    "0000088000000000",
    "0000812808880000",
    "0088222283128000",
    "0824282255222800",
    "0822222228222800",
    "0822662222222280",
    "8722226666622280",
    "87727222222227780",
    "86777722277277780",
    "08847777777777780",
    "0008867777476880",
    "0000086776888000",
    "0000008888000000",
]


p: Pen = Pen
sc: turtle.Screen = turtle.Screen()
sc.setup(width=600, height=600)
t: turtle = p.t()
t.pensize(2)
t.speed(0)
offset = (-100, 100)
colors = [
    "#ffffff",
    "#C5A4CD",
    "#947ACD",
    "#6A5391",
    "#3A304E",
    "#9C7DD5",
    "#414041",
    "#7A59AB",
    "#000000",
]

for i in range(len(meta)):
    meta_split = [c for c in meta[i]]
    for k in range(len(meta_split)):
        if int(meta_split[k-1]) == 0:
            continue
        t.penup()
        t.setpos(-140+k * 10, 120+i * -10)
        t.pendown()
        t.fillcolor(colors[int(meta_split[k-1])])
        t.pencolor(colors[int(meta_split[k-1])])
        t.begin_fill()
        for _ in range(4):
            t.fd(10)
            t.rt(90)
        t.end_fill()

t.penup()
t.setpos(10000, 10000)

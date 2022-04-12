# @author yuu
# @date 2022/4/12

import turtle
import time

# macro for drawing
class Pen:
    def t():
        return turtle
    
    def s():
        s = turtle.getscreen()
        return s

# main function
meta = [
    # 40 x 40  
    "0000088000000000000",
    "0000811888000000000",
    "0088223333888000000",
    "0845333332335800000",
    "0853333333335380000",
    "8313334533323380000",
    "8533235533334338000",
    "8455333353334438000",
    "8457525541333418880",
    "08775457771331151180",
    "00877547772141151180",
    "0856777776621151180",
    "0865677666521458800",
    "0088886566756880000",
    "0000008887778000000",
    "0000000008880000000",
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
    "#658CCA",
    "#486B9E",
    "#8CADF2",
    "#ECEDEA",
    "#404143",
    "#C9B984",
    "#FFE6AC",
    "#000000",
]
# meta
for i in range(len(meta)):
    # split string
    meta_split = [c for c in meta[i]]
    for k in range(len(meta_split)):
        if int(meta_split[k-1]) == 0:
            continue
        t.penup()
        # print(-140+k*10, 120+i*-10)
        t.setpos(-140+k * 10, 120+i * -10)
        t.pendown()
        # print(int(meta_split[k-1]))
        t.fillcolor(colors[int(meta_split[k-1])])
        t.pencolor(colors[int(meta_split[k-1])])
        t.begin_fill()
        for _ in range(4):
            t.fd(10)
            t.rt(90)
        t.end_fill()

t.penup()
# trash turtle :D
t.setpos(10000, 10000)

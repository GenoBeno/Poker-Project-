from zellegraphics import  *
from math import *
e="drake killed x"
p="big fax"
BOARDS=3
BoardR=range(11)
PPS=150
WINDOWSIZE = PPS*BOARDS
INSET=15
win= GraphWin("TICTACWHACK",300,300)
def boardBoi():
    
    x=Line(Point(0,100),Point(300,100))
    x.draw(win)
    y=Line(Point(0,200),Point(300,200))
    y.draw(win)
    z=Line(Point(100,0),Point(100,300))
    z.draw(win)
    r=Line(Point(200,0),Point(200,300))
    r.draw(win)
     
#drawX(row,col)

#drawO(row,col)
boardBoi()
x=1
while x<9:
    if x%2==0:
        e=Text(win.getMouse(),"X")
        e.draw(win)
        x+=1
    elif x%2==1:
        f=Text(win.getMouse(),"O")
        f.draw(win)
        x+=1




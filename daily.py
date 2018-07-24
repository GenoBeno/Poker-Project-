import zellegraphics as zg 
import math
import pygame
Tolerance=5
win = zg.GraphWin("draw",500,500)
clicks = []
def drawPoint(p):
    x=zg.Circle(p,Tolerance)
    x.draw(win)
    x.setFill('red')

def dist(p1,p2):
    x1=p1.getX()
    x2=p2.getX()
    y1=p1.getY()
    y2=p2.getY()
    dx=x1-x2
    dy=y1-y2
    return math.sqrt((dx ** 2 )+(dy**2))

while True:
    c=win.getMouse()
    drawPoint(c)
    clicks.append(c)
    if len(clicks)>1:
        p= zg.Line(clicks[-1],clicks[-2])
        p.draw(win)
        

    if len(clicks) > 1 and dist(clicks[0],clicks[-1])<Tolerance :
        break

x=zg.Polygon(clicks)
x.setFill('red')
x.draw(win)

win.getMouse()




pygame.draw.line(display, pink, (0,0), (250,100), 3)
import math
from math import *
import zellegraphics
from zellegraphics import *

boardsize = 3
boardrange = range(boardsize)
PPS = 150
windowsize = PPS * boardsize
inset = 15
empty = -1

def rectUpperRight(row,col):
    return Point(PPS*(col+1) - inset, PPS*row+inset)

def rectUpperLeft(row,col):
    return Point(PPS*col+inset,PPS*row+inset)

def rectLowerLeft(row,col):
    return Point(PPS*col+inset,PPS*(row+1)-inset)

def rectLowerRight(row,col):
    return Point(PPS*(col+1)-inset, PPS*(row+1)- inset)

def rectCenter(row,col):
    return Point(PPS*col + 1/2 * PPS, PPS*row + 1/2 * PPS)

def drawGrid():
    for i in range (1, boardsize):
        Line(Point(0, i*PPS), Point(windowsize, i*PPS)).draw(win)
        Line(Point(i*PPS, 0), Point(i*PPS, windowsize)).draw(win)

def drawX(row,col):
    Line(rectUpperLeft(row,col), rectLowerRight(row,col)).draw(win)
    Line(rectLowerLeft(row,col), rectUpperRight(row,col)).draw(win)

def drawO(row,col):
    Circle(rectCenter(row,col), PPS/2-inset).draw(win)

def boardCoord(pixelCoord):
    return pixelCoord // PPS;

global win, boardsize,boardrange, windowsize

userSize = input('enter board size (Press Enter for 3):')
if userSize != '':
    boardsize = int(userSize)
    boardrange = range(boardsize)
    windowsize = PPS * boardsize

win = GraphWin("Tic-Tac-Toe", windowsize, windowsize)
drawGrid()
drawList = [drawX, drawO]

turnCount = 0
board = [[empty for j in boardrange] for i in boardrange]

while turnCount <boardsize*boardsize:
    mouseclick = win.getMouse()
    row,col = boardCoord(mouseclick.getY()),boardCoord(mouseclick.getX())
    if board[row][col] == empty:
        drawList[turnCount%2](row,col)
        board[row][col] = turnCount%2
        turnCount = turnCount + 1


win.getMouse()
win.close()

import zellegraphics as zg
import time

xTurn = True
width = 600
height = 600

win = zg.GraphWin("Tic Tac Toe", width, height)

win.setBackground(('white'))

hLine1 = zg.Line(zg.Point(0, height/3), zg.Point(width, height/3))
hLine2 = zg.Line(zg.Point(0, 2 * height/3), zg.Point(width, 2 * height/3))
vLine1 = zg.Line(zg.Point(width/3, 0), zg.Point(width/3, height))
vLine2 = zg.Line(zg.Point(2 * width/3, 0), zg.Point(2* width/3, height))

hLine1.draw(win)
hLine2.draw(win)
vLine1.draw(win)
vLine2.draw(win)

isEmpty = True
xWin = False
oWin = False
numPlays = 0

def winMessage(whoWon):
    win.setBackground('black')
    if(whoWon == "X"):
        text = zg.Text(zg.Point(width/2, height/2), "X has won")
        text.setSize(36)
        text.draw(win)
    else:
        text = zg.Text(zg.Point(width/2, height/2), "O has won")
        text.setSize(36)
        text.draw(win)
    text.setFill('white')
    time.sleep(8)
    win.close()
    

def checkWin():
    if(isEmpty):
        return True

    # c = clickPt.getX()//200
    # r = clickPt.getY()//200

    horzCountX = 0
    vertCountX = 0
    diagCountX = 0

    horzCountO = 0
    vertCountO = 0
    diagCountO = 0

    #Horizontal Check
    for r in range(0, 3):
        for c in range(0, 3):
            if(gridArray[r][c] == "X"):
                horzCountX += 1
            if(gridArray[r][c] == "O"):
                horzCountO += 1
        if(horzCountX == 3):
            xWin = True
            winMessage("X")
            return False
        if(horzCountO == 3):
            oWin = True
            winMessage("O")
            return False
        horzCountX = 0
        horzCountO = 0

    #Vertical Check
    for c in range(0,3):
        for r in range(0, 3):
            if(gridArray[r][c] == "X"):
                vertCountX += 1
        if(vertCountX == 3):
            xWin = True
            winMessage("X")
            return False
        if(vertCountO == 3):
            oWin = True
            winMessage("O")
            return False
        vertCountX = 0
        vertCountO = 0

    #Diagonal Check from TOP LEFT to BOTTOM RIGHT
    for x in range(0, 3):
        if(gridArray[x][x] == "X"):
            diagCountX += 1
    if(diagCountX == 3):
        xWin = True
        winMessage("X")
        return False
    if(diagCountO == 3):
        oWin = True
        winMessage("O")
        return False
    
    diagCountX = 0
    diagCountO = 0

    #Diagnoal CHeck from TOP RIGHT to BOTTOM LEFT
    for x in range(0, 3):
        if(gridArray[x][2-x] == "X"):
            diagCountX += 1
    if(diagCountX == 3):
        xWin = True
        winMessage("X")
        return False
    if(diagCountO == 3):
        winMessage("O")
        oWin = True
        return False

    if(numPlays == 9):
        return False

    return True

def returnSquare(pt, XorO):
    col = pt.getX()//200
    row = pt.getY()//200

    while(gridArray[row][col] != None):
        point = win.getMouse()
        col = point.getX()//200
        row = point.getY()//200

    if(gridArray[row][col] == None):
        if(XorO == "X"):
            gridArray[row][col] = "X"
        else:
            gridArray[row][col] = "O"

        if(row == 0 and col == 0):
            return zg.Point(width/6, height/6)
        if(row == 0 and col == 1):
            return zg.Point(width/2, height/6)
        if(row == 0 and col == 2):
            return zg.Point(5 * width/6, height/6)
        if(row == 1 and col == 0):
            return zg.Point(width/6, height/2)
        if(row == 1 and col == 1):
            return zg.Point(width/2, height/2)
        if(row == 1 and col == 2):
            return zg.Point(5 * width/6, height/2)
        if(row == 2 and col == 0):
            return zg.Point(width/6, 5 * height/6)
        if(row == 2 and col == 1):
            return zg.Point(width/2, 5 * height/6)
        if(row == 2 and col == 2):
            return zg.Point(5 * width/6, 5 * height/6)
    


def drawX(pt):
    point = returnSquare(pt, "X")
    text = zg.Text(point, "X")
    text.setSize(36)
    text.draw(win)

def drawO(pt):
    point = returnSquare(pt, "O")
    text = zg.Text(point, "O")
    text.setSize(36)
    text.draw(win)


gridArray = [[None, None, None], [None, None, None], [None, None, None]]
clickPt = (0, 0)
while(checkWin()):
    clickPt = win.getMouse()
    if(xTurn):
        drawX(clickPt)
    else:
        drawO(clickPt)
    numPlays += 1
    xTurn = not xTurn
    isEmpty = False

# win.setBackground('white')
# print("xWin = " + str(xWin))
# if(xWin):
#     text = zg.Text(zg.Point(width/2, height/2), "X has won")
# elif(oWin):
#     text = zg.Text(zg.Point(width/2, height/2), "O has won")
# else:

win.setBackground('black')
text = zg.Text(zg.Point(width/2, height/2), "Tie")
text.setSize(36)
text.setFill('white')
text.draw(win)

time.sleep(8)




# win.getMouse()



win.close()



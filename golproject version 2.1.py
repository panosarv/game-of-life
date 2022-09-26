#MODULES
import tkinter as tk
from tkinter import ttk
import random

#CONSTANCES
ROOT_SIZE=520
BOARD_SIZE = int((ROOT_SIZE-20)/10)
CELL_SIZE =10
STARTING_R=5

#CELL_CLASS
class Cell():
    def __init__(self, screen_x, screen_y, row, col):
        self.state = False
        self.nextState = None
        self.screen_pos = (screen_x, screen_y)
        self.matrix_pos = (row, col)

    def changeState(self):
        self.state = not self.state

    def __str__(self):
        return str(self.state)




#CREATE_BOARD
def createGrid():
   
    x = CELL_SIZE
    y = CELL_SIZE
    global cellGrid 
    global rectList 
    rectList = []
    cellGrid = []
    for row in range(BOARD_SIZE):
        cellGrid.append([])
        rectList.append([])
        for col in range(BOARD_SIZE):
            rect = canvas.create_rectangle(x, y, x+CELL_SIZE, y+CELL_SIZE, fill="grey")
            rectList[row].append(rect)
            cellGrid[row].append(Cell(x, y, row, col))
            x += CELL_SIZE
        x = CELL_SIZE
        y += CELL_SIZE

#CHANGE_COLOR_ON_CLICK
def findRectCoordinates(x, y):
   
    return (x- x%CELL_SIZE, y - y%CELL_SIZE)


def changeColour(event):
    x, y = findRectCoordinates(event.x, event.y)
    try:
        iy = int(x / CELL_SIZE - 1)
        ix = int(y / CELL_SIZE - 1)
        if ix == -1 or iy == -1:
            raise IndexError
        if cellGrid[ix][iy].state:
            canvas.itemconfig(rectList[ix][iy], fill="grey")
        else:
            canvas.itemconfig(rectList[ix][iy], fill="yellow")
        cellGrid[ix][iy].changeState()
        
    except IndexError:
        return

#---UPDATE_GRID---
def updateRect():
    for row in cellGrid:
        for cell in row:
            if cell.nextState != cell.state:
                x, y = cell.matrix_pos
                if cell.nextState:canvas.itemconfig(rectList[x][y], fill="yellow")    
                else:canvas.itemconfig(rectList[x][y], fill="grey")
                cell.changeState()
                


#---EVOLVE_CRITERIA---               
def changeCellState(cell):
    
    alive_counter = 0
    x, y = cell.matrix_pos
    for neightbors_x in (x-1, x, x+1):
        for neighbors_y in (y-1, y, y+1):
            if neightbors_x == x and neighbors_y == y:
                continue
            if neightbors_x == -1 or neighbors_y == -1:
                continue
            try:
                if cellGrid[neightbors_x][neighbors_y].state:
                    alive_counter += 1
            except IndexError:
                pass
    if cell.state:
       if not( alive_counter == 2 or alive_counter==3 ):return True
    else:
        if(alive_counter == 3):return True

#---CONTROL_GAME---
def startGame():
    for row in cellGrid:
        for cell in row:
            if changeCellState(cell):
                cell.nextState = not cell.state
            else:
                cell.nextState = cell.state
    updateRect()
    global begin_id
    begin_id = root.after(200,startGame)


def pauseGame():
    try:
        root.after_cancel(begin_id)
    except:
        pass

def exitGame():
    root.destroy()
    
def reset(event):
    pauseGame()
    for row in cellGrid:
        for cell in row:
            cell.nextState=None
            if cell.state:
                cell.state=False
                x,y = cell.matrix_pos
                canvas.itemconfig(rectList[x][y], fill="grey")

#---METHODS---
def resetGrid():
    pauseGame()
    for row in cellGrid:
        for cell in row:
            cell.nextState=None
            if cell.state:
                cell.state=False
                x,y = cell.matrix_pos
                canvas.itemconfig(rectList[x][y], fill="grey")

def createGlider():
    resetGrid()
    for cell in [(STARTING_R-2,STARTING_R+1),(STARTING_R-1,STARTING_R+2),(STARTING_R,STARTING_R),
                 (STARTING_R,STARTING_R+1),(STARTING_R,STARTING_R+2)]:
        glider_x, glider_y =cell
        cellGrid[glider_x][glider_y].state=True
        canvas.itemconfig(rectList[glider_x][glider_y],fill='yellow')
def createSpaceship():
    resetGrid()
    for cell in [(STARTING_R+18,STARTING_R+1),(STARTING_R+18,STARTING_R+2),(STARTING_R+18,STARTING_R+3),
                 (STARTING_R+18,STARTING_R+4),(STARTING_R+19,STARTING_R),(STARTING_R+19,STARTING_R+4),
                 (STARTING_R+20,STARTING_R+4),(STARTING_R+21,STARTING_R),(STARTING_R+21,STARTING_R+3)]:
        spashp_x, spashp_y = cell
        cellGrid[spashp_x][spashp_y].state=True
        canvas.itemconfig(rectList[spashp_x][spashp_y],fill='yellow')
def createTenRow():
    resetGrid()
    for cell_y in range(STARTING_R+15,STARTING_R+25):
        cellGrid[STARTING_R+20][cell_y].state=True
        canvas.itemconfig(rectList[STARTING_R+20][cell_y],fill='yellow')

def createRandom():
    resetGrid()
    for cells in range(ROOT_SIZE-20):
        rand_x=random.randint(0,BOARD_SIZE-1)
        rand_y=random.randint(0,BOARD_SIZE-1)
        cellGrid[rand_x][rand_y].state=True
        canvas.itemconfig(rectList[rand_x][rand_y],fill='yellow')

def createGun():
    resetGrid()
    for cell in [(STARTING_R,STARTING_R),(STARTING_R,STARTING_R+1),(STARTING_R+1,STARTING_R+1),(STARTING_R+1,STARTING_R),(STARTING_R+1,STARTING_R+1),
                 (STARTING_R+1,STARTING_R+8),(STARTING_R+2,STARTING_R+8),(STARTING_R+2,STARTING_R+9),
                 (STARTING_R,STARTING_R+9),(STARTING_R,STARTING_R+10),(STARTING_R+1,STARTING_R+10),
                 (STARTING_R+2,STARTING_R+16),(STARTING_R+2,STARTING_R+17),(STARTING_R+3,STARTING_R+16),
                 (STARTING_R+4,STARTING_R+16),(STARTING_R+3,STARTING_R+18),(STARTING_R,STARTING_R+22),(STARTING_R,STARTING_R+23),
                 (STARTING_R-1,STARTING_R+22),(STARTING_R-2,STARTING_R+23),(STARTING_R-2,STARTING_R+24),
                 (STARTING_R-1,STARTING_R+24),(STARTING_R-1,STARTING_R+34),(STARTING_R-1,STARTING_R+35),
                 (STARTING_R-2,STARTING_R+34),(STARTING_R-2,STARTING_R+35),(STARTING_R+5,STARTING_R+35),(STARTING_R+6,STARTING_R+35),
                 (STARTING_R+7,STARTING_R+35),(STARTING_R+5,STARTING_R+36),(STARTING_R+6,STARTING_R+37),
                  (STARTING_R+10,STARTING_R+26),(STARTING_R+10,STARTING_R+25),(STARTING_R+10,STARTING_R+24),
                  (STARTING_R+11,STARTING_R+24),(STARTING_R+12,STARTING_R+25)]:
        gun_x,gun_y=cell
        cellGrid[gun_x][gun_y].state=True
        canvas.itemconfig(rectList[gun_x][gun_y],fill='yellow')
        
def getMethod(method):
    if method=="Clear":resetGrid()
    elif method=="Glider":createGlider()
    elif method=="Spaceship":createSpaceship()
    elif method=="10-Row":createTenRow()
    elif method=="Gosper Glider gun":createGun()
    elif method=="Random":createRandom()

#---COMBOBOX---
def comboBox():
    global box_value
    box_value=tk.StringVar()
    global box
    box=tk.ttk.Combobox(frame,state="readonly",textvariable=box_value)
    box.bind('<<ComboboxSelected>>',selection)
    method_list=["Clear","Glider","Spaceship","10-Row","Gosper Glider gun","Random"]
    method_tupple=("Choose a starting method",)
    for method in method_list:
        method_tupple = method_tupple+(method,)
    box['values']=method_tupple
    box.current(0)
    box.pack(fill='x',expand=0)
    
def selection(event):
    value_of_combo=box.get()
    chosen_method=value_of_combo
    getMethod(chosen_method)

#MAIN_PROGRAMME
#ROOT-------------------------------------
root = tk.Tk()
root.resizable(width=False, height=False)
root.title("Conway's Game of Life")
root.bind("<KeyPress-r>",reset)
root.bind("<KeyPress-R>",reset)
#FRAME------------------------------------
frame = tk.Frame(root, width=ROOT_SIZE, height=ROOT_SIZE)
frame.pack()
#COMBOBOX--------------------------------
comboBox()
#CANVAS----------------------------------
canvas = tk.Canvas(frame, width=ROOT_SIZE, height=ROOT_SIZE)
canvas.bind("<Button-1>", changeColour)
canvas.config(cursor="hand2")
canvas.pack()
#GRID------------------------------------
createGrid()
#BUTTONS---------------------------------

#START_BUTTON
start = tk.Button(root, text="▶",font="Consolas 15", command=startGame)
start.config(cursor="hand2")
start.pack(side = "left")
#EXIT_BUTTON
exitb= tk.Button(root, text="❌",font="Consolas 15",fg='red',command= exitGame)
exitb.config(cursor="hand2")
exitb.pack(side="right")
#PAUSE_BUTTON
pause = tk.Button(root, text="⏸", font="Consolas 15",command = pauseGame)
pause.config(cursor="hand2")
pause.pack()



root.mainloop()


from tkinter import *
import random
import copy
import time
import policy
import value
from typing import List

# constants
NORMAL_TILE_COLOR = '#50577A'
SELECTED_TILE_COLOR = '#AAAAAA'
BACKGROUND_COLOR = "#404258"
CANVAS_BACKGROUND = "#50577A"
SCALE = 0.7


TILE_SIZE = 50
# setting the window
window:Tk = Tk()
window.geometry(f"{int(SCALE*900)}x{int(SCALE*620)}")
window.title("Suduko agent")
window.config(background=BACKGROUND_COLOR)
window.resizable(False,False)

N = IntVar(window,7)

canvas:Canvas = Canvas(window,height=600*SCALE,width=600*SCALE,background=CANVAS_BACKGROUND)
button:Button = None
solveButton:Button = None
entry:Entry = None
# current_state:list[list[int]] =  []
# maze:list[list[int]]=[]
maze: List[List[int]] = []
currentPosition:int = 0


up1 = PhotoImage(file="Walking sprites/boy_up_1.png")  
up2 = PhotoImage(file="Walking sprites/boy_up_2.png")
up1=up1.zoom(2)
up2=up2.zoom(2)

down1=PhotoImage(file="Walking sprites/boy_down_1.png")
down2=PhotoImage(file="Walking sprites/boy_down_2.png")
down1=down1.zoom(2)
down2=down2.zoom(2)

left1=PhotoImage(file="Walking sprites/boy_left_1.png")
left2=PhotoImage(file="Walking sprites/boy_left_2.png")
left1=left1.zoom(2)
left2=left2.zoom(2)

right1=PhotoImage(file="Walking sprites/boy_right_1.png")
right2=PhotoImage(file="Walking sprites/boy_right_2.png")
right1=right1.zoom(2)
right2=right2.zoom(2)

monster = PhotoImage(file="Walking sprites/monster.png")
monster=monster.zoom(1)

heroId = 0

# create value and policy objects
valueObject = None
selected = StringVar(window,'')
# selected = 'p' or 'v'
policyObject= None

# radio buttons to select v or p
Radiobutton(window, text = "value iteration", variable = selected, 
    value = 'v', font=('arial',11),foreground='#D6E4E5',background="#404258").place(x=SCALE*700,y=SCALE*400,) 
Radiobutton(window, text = "policy iteration", variable = selected, 
    value = 'p', font=('arial',11),foreground='#D6E4E5',background="#404258").place(x=SCALE*700,y=SCALE*450)
  


def terminate(event):
    exit()

def getPosition():
    for i in range(N.get()):
        for j in range(N.get()):
            if maze[i][j]==2:
                return [i,j]

def goRight(event=None):
    global heroId
    x:int=0
    toggle=0
    hero=[right1,right2]
    [i,j] = getPosition()
    while x<TILE_SIZE:

        if heroId > 0:
            canvas.delete(heroId)
        
        heroId=canvas.create_image((TILE_SIZE*(j+1)+x)*SCALE, (TILE_SIZE)*(i+1)*SCALE, image=hero[toggle])
        canvas.update()
        time.sleep(0.04)
        toggle=1 if toggle==0 else 0
        x+=2
    if j+1<N.get():
        maze[i][j]=0
        maze[i][j+1]=2

    for i in range(N.get()):
        print(maze[i])
    print('\n')

    drawMaze()
    drawMazeOutline()


def goLeft(event=None):
    global heroId
    x:int=0
    toggle=0
    hero=[left1,left2]
    [i,j] = getPosition()
    while x<TILE_SIZE:

        if heroId > 0:
            canvas.delete(heroId)
        
        heroId=canvas.create_image((TILE_SIZE*(j+1)-x)*SCALE, (TILE_SIZE)*(i+1)*SCALE, image=hero[toggle])
        canvas.update()
        time.sleep(0.04)
        toggle=1 if toggle==0 else 0
        x+=2
    if j-1>=0:
        maze[i][j]=0
        maze[i][j-1]=2
    
    for i in range(N.get()):
        print(maze[i])
    print('\n')

    drawMaze()
    drawMazeOutline()


def goUp(event=None):
    global heroId
    x:int=0
    toggle=0
    hero=[up1,up2]
    [i,j] = getPosition()
    while x<TILE_SIZE:

        if heroId > 0:
            canvas.delete(heroId)
        
        heroId=canvas.create_image((TILE_SIZE)*(j+1)*SCALE, (TILE_SIZE*(i+1)-x)*SCALE, image=hero[toggle])
        canvas.update()
        time.sleep(0.04)
        toggle=1 if toggle==0 else 0
        x+=2
    if i-1>=0:
        maze[i][j]=0
        maze[i-1][j]=2

    for i in range(N.get()):
        print(maze[i])
    print('\n')

    drawMaze()
    drawMazeOutline()


def goDown(event=None):
    global heroId
    x:int=0
    toggle=0
    hero=[down1,down2]
    [i,j] = getPosition()
    while x<TILE_SIZE:

        if heroId > 0:
            canvas.delete(heroId)
        
        heroId=canvas.create_image((TILE_SIZE)*(j+1)*SCALE, (TILE_SIZE*(i+1)+x)*SCALE, image=hero[toggle])
        canvas.update()
        time.sleep(0.04)
        toggle=1 if toggle==0 else 0
        x+=2

    if i+1<N.get():
        maze[i][j]=0
        maze[i+1][j]=2

    for i in range(N.get()):
        print(maze[i])
    print('\n')

    drawMaze()
    drawMazeOutline()

def genMaze():
    global N,maze,solveButton,valueObject,policyObject

    # maze = [[0 for _ in range(N.get())] for _ in range(N.get())]

    # for i in range(N.get()):
    #     for j in range(N.get()):
    #         if i==j:
    #             if i==0:
    #                 maze[i][j]=2
    #                 continue
    #             if i==N.get()-1:
    #                 maze[i][j]=0
    #                 continue

    #         maze[i][j]=random.randint(0,1)
    #     print(maze[i])
    # print('\n')
    if selected.get()=='v':
        barrier_prob = float(input("Enter the probability of barriers (0.0 to 1.0): "))
        valueObject = value.MazeSolver(N.get(),barrier_prob)
        maze = valueObject.maze
    elif selected.get()=='p':
        barrier_prob = float(input("Enter the probability of barriers (0.0 to 1.0): "))
        policyObject = policy.MazeSolver(N.get(),barrier_prob)
        maze = copy.deepcopy(policyObject.maze)
        for i in range(N.get()):
            for j in range(N.get()):
                if maze[i][j]==-1:
                    maze[i][j]=1
    else:
        print('choose policy iteration or value iteration')
        return
    maze[0][0]=2
    drawMaze()
    drawMazeOutline()
    print(maze,end='\n\n')

    solveButton=Button(window,text='solve',font=('arial',int(17*SCALE)),foreground='#D6E4E5',background="#404258",command=solveMaze)
    solveButton.place(x=SCALE*700,y=SCALE*300)
    

def solveMaze():
    global valueObject

    # value iteration
    if selected.get()=='v':

        solvable = valueObject.is_solvable()
        if solvable:
            tv=time.time()
            commands=valueObject.getCommands()
            tvt=time.time()-tv
            print('path to goal starting from state(0,0):')
            print(commands)
            print(f"cost of path: {len(commands)}")
            print(f"time taken: {tvt}")
        else:
            print("Maze is not solvable")
            return

    
    elif selected.get()=='p':
        solvable = policyObject.is_solvable()
        if solvable:
            t1=time.time()
            policyObject.policy_iteration()
            t=time.time()-t1
            commands=policy.find_optimal_path_with_values(policyObject.policy)

            if commands != -1 :
                print('path to goal starting from state(0,0):')
                print(commands)
                print(f"cost of path: {len(commands)}")
                print(f"time taken: {t}")
            else:
                print("blocked maze")
                return

        else:
            print("Maze is not solvable")
            return

    for action in commands:
        if action.lower()=='u':
            goUp()
        elif action.lower()=='d':
            goDown()
        elif action.lower()=='l':
            goLeft()
        elif action.lower()=='r':
            goRight()

        else:
            print("error in solvemaze")
            exit(-10)
    print('Winner winner chicken dinner!!')


def drawMazeOutline():
    for i in range(N.get()):    
        canvas.create_line(((i+1)*TILE_SIZE+20)*SCALE,0,((i+1)*TILE_SIZE+20)*SCALE,(TILE_SIZE+5)*N.get()*SCALE,width=2*SCALE)
        canvas.create_line(0,((i+1)*TILE_SIZE+20)*SCALE,(TILE_SIZE+5)*N.get()*SCALE,((i+1)*TILE_SIZE+20)*SCALE,width=2*SCALE)


def drawMaze(event=None):
    global canvas,heroId

    canvas.delete('all')
    
    canvas.create_text(TILE_SIZE*SCALE,TILE_SIZE*SCALE,text='S')
    canvas.create_text(TILE_SIZE*N.get()*SCALE,TILE_SIZE*N.get()*SCALE,text='E')
    for i in range(N.get()):
        for j in range(N.get()):
            if maze[i][j]==1:
                canvas.create_image((TILE_SIZE)*(j+1)*SCALE, TILE_SIZE*(i+1)*SCALE, image=monster)
            elif maze[i][j]==2:
                heroId=canvas.create_image((TILE_SIZE)*(j+1)*SCALE, TILE_SIZE*(i+1)*SCALE, image=down1)
                

    canvas.update()
    
def takeControl(event='test'):
    global window
    if window.focus_get()==entry:
        window.focus_set()
        print('window took control')
    else:
        entry.focus_set()
        print('entry took control')

if __name__ == "__main__":
    
    # drawEnvironment()
    canvas.place(x=0,y=0)
    button=Button(window,text='generate maze',font=('arial',int(17*SCALE)),foreground='#D6E4E5',background="#404258",command=genMaze)
    button.place(x=SCALE*700,y=SCALE*200)
    
    label = Label(window,text='Enter maze size N',font=('arial',int(17*SCALE)),foreground='#D6E4E5',background=BACKGROUND_COLOR)
    label.place(x=SCALE*650,y=SCALE*50)
    entry=Entry(window,textvariable=N,font=('arial',int(17*SCALE)))
    entry.place(x=SCALE*650,y=SCALE*100)
    
    # window.bind('<Button-1>',)
    window.bind("<Escape>",terminate)    
    # window.bind("w",goUp)
    # window.bind("s",goDown)
    # window.bind("a",goLeft)
    # window.bind("d",goRight)
    # window.bind("<Button-1>",takeControl)
    window.mainloop()

    
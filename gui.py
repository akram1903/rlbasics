
from tkinter import *
import random
import time
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

N = IntVar(window,5)

canvas:Canvas = Canvas(window,height=600*SCALE,width=600*SCALE,background=CANVAS_BACKGROUND)
button:Button = None
entry:Entry = None
# current_state:list[list[int]] =  []
maze:list[list[int]]=[]
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

# def printKeys(event):
#     print(event.keysym+" key pressed")
#     if event.keysym in ["1","2","3","4","5","6","7","8","9","BackSpace","space"]:
#         editSelectedTile(event)

def terminate(event):
    exit()

def genMaze():
    # global current_state
    # certificate,current_state=generatePuzzle.generatePuzzle()
    # drawPuzzle()
    # unselect()
    global N,maze

    maze = [[0 for _ in range(N.get())] for _ in range(N.get())]

    for i in range(N.get()):
        for j in range(N.get()):
            if i==j:
                if i==0:
                    maze[i][j]=2
                    continue
                if i==N.get()-1:
                    maze[i][j]=0
                    continue

            maze[i][j]=random.randint(0,1)
        print(maze[i])
    print('\n')
    
    drawMaze()
    drawMazeOutline()
    

def solveMaze():

    pass

def drawEnvironment():
    global canvas,image_item

    for i in range(N.get()):
        for j in range(N.get()):
            image_item = canvas.create_image(TILE_SIZE*SCALE*(i+1), TILE_SIZE*SCALE*(j+1), image=monster)

    # global environment
    
    # while environment.__len__()>0:
    #     canvas.delete(environment.pop())

    # for i in range(9):
    #     environment.append(canvas.create_line(100*i*SCALE,0,100*i*SCALE,900*SCALE,width=2*SCALE))
    #     environment.append(canvas.create_line(0,100*i*SCALE,900*SCALE,100*i*SCALE,width=2*SCALE))

    # environment.append(canvas.create_line(300*SCALE,0,300*SCALE,900*SCALE,width=5*SCALE))
    # environment.append(canvas.create_line(600*SCALE,0,600*SCALE,900*SCALE,width=5*SCALE))
    # environment.append(canvas.create_line(0,300*SCALE,900*SCALE,300*SCALE,width=5*SCALE))
    # environment.append(canvas.create_line(0,600*SCALE,900*SCALE,600*SCALE,width=5*SCALE))
    pass

def drawMazeOutline():
    for i in range(N.get()):    
        canvas.create_line(((i+1)*TILE_SIZE+20)*SCALE,0,((i+1)*TILE_SIZE+20)*SCALE,(TILE_SIZE+5)*N.get()*SCALE,width=2*SCALE)
        canvas.create_line(0,((i+1)*TILE_SIZE+20)*SCALE,(TILE_SIZE+5)*N.get()*SCALE,((i+1)*TILE_SIZE+20)*SCALE,width=2*SCALE)
def drawMaze(event=None):
    # global current_state,numberIds
    

    
    # for i in range(9):
    #     for j in range(9):
    #         canvas.delete(numberIds[i][j])
    #         element = current_state[i][j]
    #         if element == 0:
    #             element = ' '
    #         numberIds[i][j]=canvas.create_text((j*100+50)*SCALE,(i*100+50)*SCALE,text=f'{element}',font=('arial',40),fill='#D6E4E5')
    global canvas
    # canvas.delete(image_item)
    # for i in range(N):
    #     for j in range(N):
    #         if maze[i][j]!=0:
    #             pass
    # pass

    canvas.delete('all')
    for i in range(N.get()):
        for j in range(N.get()):
            if maze[i][j]==1:
                canvas.create_image((TILE_SIZE)*(j+1)*SCALE, TILE_SIZE*(i+1)*SCALE, image=monster)
            elif maze[i][j]==2:
                canvas.create_image((TILE_SIZE)*(j+1)*SCALE, TILE_SIZE*(i+1)*SCALE, image=down1)
                

    canvas.update()
    


        


if __name__ == "__main__":
    
    
    drawEnvironment()
    canvas.place(x=0,y=0)
    button=Button(window,text='generate maze',font=('arial',int(17*SCALE)),foreground='#D6E4E5',background="#404258",command=genMaze)
    button.place(x=SCALE*700,y=SCALE*200)
    
    label = Label(window,text='Enter maze size N',font=('arial',int(17*SCALE)),foreground='#D6E4E5',background=BACKGROUND_COLOR)
    label.place(x=SCALE*650,y=SCALE*50)
    entry=Entry(window,textvariable=N,font=('arial',int(17*SCALE)))
    entry.place(x=SCALE*650,y=SCALE*100)
    time.sleep(2)
    
    # window.bind('<Button-1>',)
    window.bind("<Escape>",terminate)    
    window.bind("w",drawMaze)
    window.mainloop()

    
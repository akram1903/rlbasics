
from tkinter import *
import random
import time
# constants
NORMAL_TILE_COLOR = '#50577A'
SELECTED_TILE_COLOR = '#AAAAAA'
BACKGROUND_COLOR = "#404258"
CANVAS_BACKGROUND = "#50577A"
SCALE = 0.7
N = 2

# setting the window
window:Tk = Tk()
window.geometry(f"{int(SCALE*900)}x{int(SCALE*620)}")
window.title("Suduko agent")
window.config(background=BACKGROUND_COLOR)
window.resizable(False,False)

canvas:Canvas = Canvas(window,height=600*SCALE,width=600*SCALE,background=CANVAS_BACKGROUND)
button:Button = None

# current_state:list[list[int]] =  []
maze:list[list[int]]=[]
currentPosition:int = 0


up1 = PhotoImage(file="Walking sprites/boy_up_1.png")  
up2 = PhotoImage(file="Walking sprites/boy_up_2.png")

down1=PhotoImage(file="Walking sprites/boy_down_1.png")
down2=PhotoImage(file="Walking sprites/boy_down_2.png")

left1=PhotoImage(file="Walking sprites/boy_left_1.png")
left2=PhotoImage(file="Walking sprites/boy_left_2.png")

right1=PhotoImage(file="Walking sprites/boy_right_1.png")
right2=PhotoImage(file="Walking sprites/boy_right_2.png")

monster = PhotoImage(file="Walking sprites/monster.png")

image = monster.zoom(2,2)
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

    maze = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            maze[i][j]=random.randint(0,1)
        print(maze[i])
    
    

def solveMaze():

    pass

def drawEnvironment():
    image_item = canvas.create_image(image.width()//2, image.height()//2, image=image)

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


def drawMaze():
    # global current_state,numberIds
    

    
    # for i in range(9):
    #     for j in range(9):
    #         canvas.delete(numberIds[i][j])
    #         element = current_state[i][j]
    #         if element == 0:
    #             element = ' '
    #         numberIds[i][j]=canvas.create_text((j*100+50)*SCALE,(i*100+50)*SCALE,text=f'{element}',font=('arial',40),fill='#D6E4E5')
    global canvas
    canvas.delete('all')
    canvas.update()
    # for i in range(N):
    #     for j in range(N):
    #         if maze[i][j]!=0:
    #             pass
    # pass



        


if __name__ == "__main__":
    
    
    drawEnvironment()
    canvas.place(x=0,y=0)
    button=Button(window,text='generate maze',font=('arial',int(17*SCALE)),foreground='#D6E4E5',background="#404258",command=genMaze)
    button.place(x=SCALE*700,y=SCALE*200)

    time.sleep(2)
    
    # window.bind('<Button-1>',)
    window.bind("<Escape>",terminate)    
    
    window.mainloop()

    time.sleep(2)
    drawMaze()
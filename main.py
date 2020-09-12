from tkinter import *
import time


def up(self):
  self.dy = -5
  self.dx = 0
  print(self.name + " up_button pressed")
  self.update()

def right():
  ball1.dy = 0
  ball1.dx = 5
  ball1.update()

def left():
  ball1.dy = 0
  ball1.dx = -5
  ball1.update()

def down():
  ball1.dy = 5
  ball1.dx = 0
  ball1.update()

root = Tk()
frame = Frame(root)
frame.grid()

bottomframe = Frame(root)
bottomframe.grid(row=1, column=1, columnspan=1)

# up_button = Button(frame, text="UP", fg="red", command=up)
# up_button.grid(row=1, column=2, columnspan=1)

# right_button = Button(frame, text="RIGHT", fg="red", command=right)
# right_button.grid(row=2, column=3, columnspan=1)

# left_button = Button(frame, text="LEFT", fg="red", command=left)
# left_button.grid(row=2, column=1, columnspan=1)

# down_button = Button(frame, text="DOWN", fg="red", command=down)
# down_button.grid(row=2, column=2, columnspan=1)



root = Tk()
canvas = Canvas(root, width=800, height=600)
canvas.pack()


class ball:
  def __init__(self,name,number,x0,y0,x1,y1,outline,fill):
    self.name = name
    self.number = number
    self.dx = 0
    self.dy = 0
    self.x0 = x0
    self.y0 = y0
    self.x1 = x1
    self.y1 = y1
    self.outline = outline
    self.fill = fill
    self.ball = canvas.create_oval(x0,y0,x1,y1,outline = self.outline, fill = self.fill)
    canvas.pack()

    self.up_button = Button(frame, text=self.name + " UP", fg=self.fill, command=up(self))
    self.up_button.grid(row=1, column=2+2*self.number, columnspan=1)

  
  def update(self):
    time.sleep(0.02)
    canvas.move(self.ball,self.dx,self.dy)
    canvas.update


Ball_1 = ball('Ball 1', 0, 120, 260, 220, 360, 'white','blue')
Ball_2 = ball('Ball 2', 1, 380, 280, 420, 320,'white','red')




# while True:
#   ball1.update()
#   ball2.update()




#track = 0

# def animation(track,ball1_direction):
#   while True:
#       ball1x = 6
#       ball2x = 3
#       ball1y = 3
#       ball2y = 1.5
#       print(ball1_direction)
#       if track == 0:
#           for i in range(0,80):
#               time.sleep(0.02)
#               canvas.move(ball1, ball1x, ball1y)
#               canvas.move(ball2, ball2x, ball2y)
#               canvas.update()
#           track = 1

#       elif track == 1:
#           for i in range(0,80):
#               time.sleep(0.02)
#               canvas.move(ball1, -ball1x, -ball1y)
#               canvas.move(ball2, -ball2x, -ball2y)
#               canvas.update()
#           track = 0
      
#       else:
#         canvas.update()
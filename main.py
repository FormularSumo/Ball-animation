from tkinter import *
import time
from functools import partial





def up(self):
  self.dy = -5
  self.dx = 0
  print(self.name + " up_button pressed")
  self.update()

def right(self):
  self.dy = 0
  self.dx = 5
  print(self.name + " up_button pressed")
  self.update()

def left(self):
  self.dy = 0
  self.dx = -5
  print(self.name + " up_button pressed")
  self.update()

def down(self):
  self.dy = 5
  self.dx = 0
  print(self.name + " up_button pressed")
  self.update()


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


    self.up_button = Button(frame, text=self.name + " UP", fg=self.fill, command=partial(up, self))
    self.up_button.grid(row=1, column=2+3*self.number, columnspan=1)

    self.left_button = Button(frame, text=self.name + " LEFT", fg=self.fill, command=partial(left, self))
    self.left_button.grid(row=2, column=1+3*self.number, columnspan=1)


    self.right_button = Button(frame, text=self.name + " RIGHT", fg=self.fill, command=partial(right, self))
    self.right_button.grid(row=2, column=3+3*self.number, columnspan=1)

    
    self.down_button = Button(frame, text=self.name + " DOWN", fg=self.fill, command=partial(down, self))
    self.down_button.grid(row=2, column=2+3*self.number, columnspan=1)



  def update(self):
    time.sleep(0.02)
    canvas.move(self.ball,self.dx,self.dy)
    canvas.update




Ball_1 = ball('Ball 1', 0, 120, 260, 220, 360, 'white','blue')
Ball_2 = ball('Ball 2', 1, 380, 280, 420, 320,'white','red')



# while True:
#   time.sleep(0.02)
#   Ball_1.update()
#   time.sleep(0.02)
#   Ball_2.update()
#   time.sleep(0.02)





#track = 0

# def animation(track,Ball_1_direction):
#   while True:
#       Ball_1x = 6
#       ball2x = 3
#       Ball_1y = 3
#       ball2y = 1.5
#       print(Ball_1_direction)
#       if track == 0:
#           for i in range(0,80):
#               time.sleep(0.02)
#               canvas.move(Ball_1, Ball_1x, Ball_1y)
#               canvas.move(ball2, ball2x, ball2y)
#               canvas.update()
#           track = 1

#       elif track == 1:
#           for i in range(0,80):
#               time.sleep(0.02)
#               canvas.move(Ball_1, -Ball_1x, -Ball_1y)
#               canvas.move(ball2, -ball2x, -ball2y)
#               canvas.update()
#           track = 0
      
#       else:
#         canvas.update()
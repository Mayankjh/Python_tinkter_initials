#canvas random rectangles

from tkinter import*
import random
root = Tk()

canvas = Canvas(root,width=300,height=300)
canvas.pack()
def randomRects(num):
    for i in range(0,num):
        x1 = random.randrange(150)
        y1 = random.randrange(150)
        x2 = x1 + random.randrange(150)
        y2 = y1 + random.randrange(150)
        #canvas.create_rectangle(x1,y1,x2,y2,fill="#298765")
        canvas.create_arc(x1,y1,x2,y2,extent="359",style= ARC,fill="#298765")
        

randomRects(6)
canvas.create_text(150,150, text="This is my space", font=("Times",30))

root.mainloop()

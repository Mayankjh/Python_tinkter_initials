#canvas

from tkinter import*
root = Tk()

canvas = Canvas(root,width=300,height=300)
canvas.pack()

def createrect(x1,y1,x2,y2):
    canvas.create_rectangle(x1,y1,x2,y2,fill="#453423")


createrect(5,50,200,70)
createrect(5,5,40,200)

root.mainloop()

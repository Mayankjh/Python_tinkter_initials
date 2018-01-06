#bind concept

from tkinter import*

root = Tk()

def leftClick(event):
    print("left")

def rightClick(event):
    print("right")

def scroll(event):
    print("scroll")

def leftKey(event):
    print("left key pressed")

def rightKey(event):
    print("right key pressed")

#button1 = Button(root, text="Click me!")
#button1.bind("<Button-1>", printName)
#button1.pack()

root.geometry("500x500")

root.bind("<Button-1>", leftClick)
root.bind("<Button-2>", scroll)
root.bind("<Button-3>", rightClick)
root.bind("<Left>", leftKey)
root.bind("<Right>", rightKey)


root.mainloop()

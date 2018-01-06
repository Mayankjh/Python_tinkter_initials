#message-box

from tkinter import*
import tkinter.messagebox

root = Tk()

#tkinter.messagebox.showinfo("Window Title","Did you know that you just fired a message")


answer = tkinter.messagebox.askquestion("Question","Are you Human?")
if answer == "yes":
    tkinter.messagebox.showinfo("Congrats","You are very lucky!!")

else:
    tkinter.messagebox.showinfo("Alien","Welcome to Earth")
    

root.mainloop()

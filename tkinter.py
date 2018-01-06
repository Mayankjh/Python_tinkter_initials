from tkinter import*

root = Tk()
#thelabel = Label(root, text="This is our tkinter window")
#thelabel.pack()
#thelabell = Label(root, text="This is second tkinter sentence")
#thelabell.pack()

#topframe

#topframe = Frame(root)

#topframe.pack()

#botFrame = Frame(root)

#botFrame.pack(side=BOTTOM)




Button1 = Button(None, text="Click Me!!", fg="yellow", bg="red")
Button1.pack()

Button2 = Button(None, text="Hello!",fg="White", bg="Green")
Button2.pack( fill=X)

Button3 = Button(None, text="Click Me!!", fg="red", bg="Yellow")
Button3.pack(side=RIGHT, fill=Y)

Button4 = Button(None, text="Hello!",fg="White", bg="cyan")
Button4.pack()

root.mainloop()


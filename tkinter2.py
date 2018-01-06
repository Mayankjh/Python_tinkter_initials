#grid concept

from tkinter import*

root = Tk()

label1 = Label(root, text="Name :")
#label2 = Label(root, text="Label 2")
#label3 = Label(root, text="Label 3")
#label4 = Label(root, text="Label 4")

label1.grid(row= 0, column = 0,sticky="E")
#label2.grid(row= 0, column = 1)
#label3.grid(row= 1, column = 0)
#label4.grid(row= 1, column = 1)

label2 = Label(root, text="Password:")
label2.grid(row= 1, column= 0,sticky="E")

entrySpace = Entry(root)

entrySpace.grid(row= 0, column = 1)

entrySpace2 = Entry(root)

entrySpace2.grid(row= 1, column = 1)

cbutton = Checkbutton(root, text="Remember Name")

cbutton.grid(columnspan = 2)


root.mainloop()

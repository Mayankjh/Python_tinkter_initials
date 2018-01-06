#menu

from tkinter import*

def random():
    print("This is a statement")

root = Tk()

mainMenu = Menu(root)

root.configure(menu = mainMenu)

subMenu1 = Menu(mainMenu)
subMenu2 = Menu(mainMenu)

mainMenu.add_cascade(label="File", menu = subMenu1)
mainMenu.add_cascade(label="Edit", menu = subMenu2)

subMenu1.add_command(label = "Random Func",command = random)
subMenu1.add_command(label = "new",command = random)
subMenu1.add_command(label = "save",command = random)
subMenu1.add_command(label = "Open",command = random)
subMenu1.add_command(label = "Exit",command = random)

subMenu1.add_separator()

subMenu1.add_command(label = "Super se upar",command = random)
subMenu2.add_command(label = "Random Func",command = random)
subMenu2.add_command(label = "new",command = random)
    

root.mainloop()

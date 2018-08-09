from tkinter import *

myApp=Tk()

LB=Listbox(myApp,selectmode=EXTENDED)
LB.grid(row=1,column=1)
LB.insert(1,"Option 1")
LB.insert(2,"Option 2")
LB.insert(3,"Option 3")

myApp.mainloop()
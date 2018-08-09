from tkinter import *

root = Tk()
root.geometry('400x480')

c = Canvas(root, height=250, width=300, bg="blue")
c.pack(padx=10, pady=20, side=LEFT)
r = c.create_rectangle(0,0,100,100, fill="yellow", activefill="grey", disabledfill="grey")
f = c.create_rectangle(240,240,100,100, fill="red", activefill="grey", disabledfill="grey")

r = Canvas(root)
r = c.pack(padx=10)

root.mainloop()
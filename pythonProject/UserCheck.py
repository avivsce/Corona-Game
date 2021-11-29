from tkinter import *
from tkinter.ttk import *

root = Tk()
root.geometry("500x300")
v = StringVar(root, "1")
values = {"Simple user": "1",
          "Admin user": "2",
          "Statistician user": "3"}

for (text,value) in values.items():
    Radiobutton(root, text=text, variable=v, value=value).pack(side=TOP, ipady=5)


root.mainloop()
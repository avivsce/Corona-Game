from tkinter import *
from tkinter import ttk
from tkinter import messagebox


root = Tk()
frame_header = ttk.Frame(root)
frame_header.pack()
#logo = PhotoImage(file='logo.gif').subsample(2, 2)
#logolabel = ttk.Label(frame_header, text='logo', image=logo)
#logolabel.grid(row=0, column=0, rowspan=2)
root.title("FeedBack")
headerlabel = ttk.Label(frame_header, text='FEEDBACK', foreground='orange',font=('Arial', 30))
headerlabel.grid(row=0, column=1)
messagelabel = ttk.Label(frame_header,
                         text='please tell us what you think',
                         foreground='yellow', font=('Arial', 20))
messagelabel.grid(row=1, column=1)

frame_content = ttk.Frame(root  )
frame_content.pack()
# def submit():
#     username = entry_name.get()
#     print(username)
myvar = StringVar()
var = StringVar()
# cmnt= StringVar()
commentlabel = ttk.Label(frame_content, text='Comment', font=('Arial', 14))
commentlabel.grid(row=2, column=0, sticky='sw')
textcomment = Text(frame_content, width=55, height=10)
textcomment.grid(row=3, column=0, columnspan=2)
'''
namelabel = ttk.Label(frame_content, text='Name')
namelabel.grid(row=0, column=0, padx=5, sticky='sw')
entry_name = ttk.Entry(frame_content, width=30, font=('Arial', 14), textvariable=myvar)
entry_name.grid(row=1, column=0)
'''
#emaillabel = ttk.Label(frame_content, text='Email')
#emaillabel.grid(row=0, column=1, sticky='sw')
#entry_email = ttk.Entry(frame_content, width=18, font=('Arial', 14), textvariable=var)
#entry_email.grid(row=1, column=1)

namelabel = ttk.Label(frame_content, text='Name')
namelabel.grid(row=0, column=0, padx=5, sticky='sw')
entry_name = ttk.Entry(frame_content, width=18, font=('Arial', 14), textvariable=myvar)
entry_name.grid(row=1, column=0)


textcomment.config(wrap ='word')
# def clear():
#     textcomment.delete(1.0,'end')
def clear():
    global entry_name
    global textcomment
    messagebox.showinfo(title='clear', message='Do you want to clear?')
    entry_name.delete(0, END)
    textcomment.delete(1.0, END)


def submit():

    global entry_name
    global textcomment


    feedback = open("FeedBack", "a+")
    feedback.write('Name:{}'.format(myvar.get()))
    feedback.write(' Comment:{}'.format(textcomment.get(1.0, END)))
    feedback.close()

    #print('Name:{}'.format(myvar.get()))
    #print('Email:{}'.format(var.get()))
    #print('Comment:{}'.format(textcomment.get(1.0, END)))
    messagebox.showinfo(title='Submit', message='Thank you for your Feedback, Your Comments Submited')
    entry_name.delete(0, END)
    textcomment.delete(1.0, END)


submitbutton = ttk.Button(frame_content, text='Submit', command=submit).grid(row=4, column=0, sticky='e')
clearbutton = ttk.Button(frame_content, text='Clear', command=clear).grid(row=4, column=1, sticky='w')

mainloop()


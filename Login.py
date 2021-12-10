import pyrebase
import firebase_admin
from firebase_admin import credentials
import firebase_admin
from firebase_admin import auth
from firebase_admin import db
from tkinter import *
import tkinter as tk
from firebase_admin import credentials

cred_obj = firebase_admin.credentials.Certificate('f.json')
#cred_obj = credentials.Certificate('f.json')

#firebase_admin.initialize_app(cred_obj)

default_app = firebase_admin.initialize_app(cred_obj, {
    'databaseURL': 'https://coronagame-151a7-default-rtdb.firebaseio.com'
})



# Login function

def login(email=None, password=None):
    if email is not None and password is not None:
        print("Log in...")
        email = input("Enter email: ")
        password = input("Enter password: ")
    #try:
    login = auth.generate_sign_in_with_email_link(email=email, action_code_settings='') #, password=password)
    print("Successfully logged in!")
        # print(auth.get_account_info(login['idToken']))
    # email = auth.get_account_info(login['idToken'])['users'][0]['email']
    # print(email)
    #except:
    #    print("Invalid email or password")
    return

def SignUpInfo():
    frame = tk.Tk()
    frame.title("Register Info")
    frame.geometry('400x400')

    name = Label(frame,text="email: ")
    name.pack()
    namevalue = StringVar
    nameentry = Entry(frame, textvariable=namevalue)
    nameentry.pack()

    password = Label(frame, text="passowrd: ")
    password.pack()
    passvalue = StringVar
    passentry = Entry(frame, textvariable=passvalue)
    passentry.pack()

    #Submit Button
    Label(text="").pack()
    Button(frame, text="submit", command=lambda: signup(nameentry, passentry)).pack()

    #Back Button
    Label(text="").pack()
    button = tk.Button(frame,text='Back',command=lambda: frame.destroy())
    button.pack()

    return namevalue,passvalue
    frame.mainloop()

# Signup Function

def signup(email, password):
    print("Sign up...")
    #print(email.get())
    #print(password.get())
    try:
        user = auth.create_user(email=email.get(), password=password.get())
    except:
        print("Email already exists")
        return
    frame = tk.Tk()
    frame.title("Question")
    frame.geometry('400x400')
    name = Label(frame, text="Do you want to login? ")
    name.pack()
    button = tk.Button(frame, text='Yes', command=login)
    button.pack()
    button = tk.Button(frame, text='No', command=lambda: frame.destroy())
    button.pack()


    '''
    ask = input("Do you want to login?[y/n]")
    if ask == 'y':
        login()
    return
    '''


def fu():
    ref = db.reference("/Users")
    users = ref.get()
    print(users)



# Main
def main_screen():
    screen = Tk()
    screen.geometry("600x600")
    screen.title("Game Start")
    Label(text="Game Start", bg="grey", font=("calibri", 13)).pack()
    Label(text="").pack()
    Button(screen,text="Login", command=fu).pack()
    Label(text="").pack()
    Button(screen,text="Register", command=SignUpInfo).pack()
    Label(text="").pack()
    Button(screen,text="Start").pack()
    Label(text="").pack()
    button = tk.Button(screen, text='EXIT', command=lambda: screen.destroy())
    button.pack()
    screen.mainloop()


main_screen()

# ans=input("Are you a new user?[y/n]")

'''if ans == 'n':
    login()
elif ans == 'y':
    signup()'''

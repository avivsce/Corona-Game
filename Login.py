import os

import firebase_admin
from firebase_admin import credentials
import firebase_admin
from firebase_admin import auth
from firebase_admin import db
from firebase_admin import firestore as fs
from tkinter import *
import tkinter as tk
from firebase_admin import credentials
from pyrebase import pyrebase

cred_obj = firebase_admin.credentials.Certificate('f.json')
# cred_obj = credentials.Certificate('f.json')

# firebase_admin.initialize_app(cred_obj)

default_app = firebase_admin.initialize_app(cred_obj, {
    'databaseURL': 'https://coronagame-151a7-default-rtdb.firebaseio.com'
})

firebaseConfig = {
    "apiKey": "AIzaSyCEl580uk5MtaDm0Qs7NHjYWh8IuORVHQE",
    "authDomain": "coronagame-151a7.firebaseapp.com",
    "databaseURL": "https://coronagame-151a7-default-rtdb.firebaseio.com",
    "projectId": "coronagame-151a7",
    "storageBucket": "coronagame-151a7.appspot.com",
    "messagingSenderId": "216602942663",
    "appId": "1:216602942663:web:ad23c5b4b524372c8bb2e2",
    "measurementId": "G-SGGG06494Y"
}

# Initialize Firebase
firebase = pyrebase.initialize_app(firebaseConfig)


# Login function

def login(email=None, password=None):
    # if email is not None and password is not None:
    print("Log in...")
    if email is not None and password is not None:
        auth = firebase.auth()
        user = auth.sign_in_with_email_and_password(email, password)
        first_char = email[0]
        second_char = email[1]
        if user is not None:
           if first_char == 'a' and second_char == '_':
                 import Admin_game.py
           elif first_char == 'u' and second_char == '_':
                 import User_game.py
           elif first_char == 's' and second_char == '_':
                 import Static_game.py
           else:
                 print("Error")
           return
        #print("Fail to login!")
        #return
    #
    frame = tk.Tk()
    frame.title("Login Info")
    frame.geometry('400x400')

    name = Label(frame, text="email: ")
    name.pack()
    namevalue = StringVar
    nameentry = Entry(frame, textvariable=namevalue)
    nameentry.pack()

    password = Label(frame, text="passowrd: ")
    password.pack()
    passvalue = StringVar
    passentry = Entry(frame, textvariable=passvalue)
    passentry.pack()

    # Submit Button
    Label(text="").pack()
    Button(frame, text="submit", command=lambda: login(nameentry.get(), passentry.get())).pack()

    # Back Button
    Label(text="").pack()
    button = tk.Button(frame, text='Back', command=lambda: frame.destroy())
    button.pack()

def SignUpInfo():
    frame = tk.Tk()
    frame.title("Register Info")
    frame.geometry('400x400')

    name = Label(frame, text="email: ")
    name.pack()
    namevalue = StringVar
    nameentry = Entry(frame, textvariable=namevalue)
    nameentry.pack()

    password = Label(frame, text="passowrd: ")
    password.pack()
    passvalue = StringVar
    passentry = Entry(frame, textvariable=passvalue)
    passentry.pack()

    # Submit Button
    Label(text="").pack()
    Button(frame, text="submit", command=lambda: signup(nameentry, passentry)).pack()

    # Back Button
    Label(text="").pack()
    button = tk.Button(frame, text='Back', command=lambda: frame.destroy())
    button.pack()

    noticeUser = Label(frame, text="User select: = u_ ")
    noticeUser.pack()
    noticeAdmin = Label(frame, text="Admin select: = a_ ")
    noticeAdmin.pack()
    noticeStatistician = Label(frame, text="Statistician select: = s_ ")
    noticeStatistician.pack()

    return namevalue, passvalue
    frame.mainloop()


# Signup Function

def signup(email, password):
    print("Sign up...")
    print(email.get())
    print(password.get())
#    first_char = email.get()[0]
#    second_char = email.get()[1]
#    if first_char == 'a' and second_char == '_':
#        print("admin")
#    elif first_char == 'u' and second_char == '_':
#        print("user")
#    elif first_char == 's' and second_char == '_':
#        print("statistician")
#    else:
#        print("Error")

    try:
        user = auth.create_user(email=email.get(), password=password.get(), display_name=str(type))
        userData = {
        u'email': email.get(),
        u'password': password.get(),
        u'type': type
        }

        db = fs.client()
        # Add a new doc in collection 'users' with ID 'email'
        db.collection(u'Users').document(email.get()).set(userData)
    except Exception as e:
        pass
    except:
        print("Email already exists")
        return
    frame = tk.Tk()
    frame.title("Question")
    frame.geometry('400x400')
    name = Label(frame, text="Do you want to login? ")
    name.pack()
    button = tk.Button(frame, text='Yes', command=lambda: login(email.get(), password.get()))
    button.pack()
    button = tk.Button(frame, text='No', command=lambda: frame.destroy())
    button.pack()

def fu():
    ref = db.reference("/Users")
    users = ref.get()
    print(users)


# Main
def main_screen():
    screen = Tk()
    screen.geometry("600x600")
    screen.title("Login")
    Label(text="Game Start", bg="grey", font=("calibri", 13)).pack()
    Label(text="").pack()
    Button(screen, text="Login", command=login).pack()
    Label(text="").pack()
    Button(screen, text="Register", command=SignUpInfo).pack()
    Label(text="").pack()
    Button(screen, text="Start").pack()
    Label(text="").pack()
    button = tk.Button(screen, text='EXIT', command=lambda: screen.destroy())
    button.pack()
    screen.mainloop()


main_screen()

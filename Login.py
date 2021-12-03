import pyrebase
import firebase_admin
from firebase_admin import credentials
import firebase_admin
from firebase_admin import auth
from firebase_admin import db
from tkinter import *
import tkinter as tk
from firebase_admin import credentials

cred_obj = firebase_admin.credentials.Certificate('firebase-sdk.json')
default_app = firebase_admin.initialize_app(cred_obj, {
    'databaseURL': 'https://coronagame-151a7-default-rtdb.firebaseio.com'
})


# Login function

def login():
    print("Log in...")
    email = input("Enter email: ")
    password = input("Enter password: ")
    try:
        login = auth.sign_in_with_email_and_password(email, password)
        print("Successfully logged in!")
        # print(auth.get_account_info(login['idToken']))
    # email = auth.get_account_info(login['idToken'])['users'][0]['email']
    # print(email)
    except:
        print("Invalid email or password")
    return


# Signup Function

def signup():
    print("Sign up...")
    email = input("Enter email: ")
    password = input("Enter password: ")
    try:
        user = auth.create_user_with_email_and_password(email, password)
        ask = input("Do you want to login?[y/n]")
        if ask == 'y':
            login()
    except:
        print("Email already exists")
    return


def fu():
    ref = db.reference("/Users")
    users = ref.get()


# Main
def main_screen():
    screen = Tk()
    screen.geometry("600x600")
    screen.title("Game Start")
    Label(text="Game Start", bg="grey", font=("calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", command=fu).pack()
    Label(text="").pack()
    Button(text="Register", command=signup).pack()
    Label(text="").pack()
    Button(text="Start").pack()

    screen.mainloop()


main_screen()

# ans=input("Are you a new user?[y/n]")

'''if ans == 'n':
    login()
elif ans == 'y':
    signup()'''

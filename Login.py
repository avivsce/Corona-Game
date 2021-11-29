import pyrebase
import firebase_admin
from firebase_admin import credentials
from tkinter import *
import tkinter as tk

from firebase_admin import db

cred = credentials.Certificate('firebase-sdk.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://coronagame-151a7-default-rtdb.firebaseio.com/'

})
firebaseConfig = {
    'apiKey': "AIzaSyCEl580uk5MtaDm0Qs7NHjYWh8IuORVHQE",
    'authDomain': "coronagame-151a7.firebaseapp.com",
    'databaseURL': "https://coronagame-151a7-default-rtdb.firebaseio.com",
    'projectId': "coronagame-151a7",
    'storageBucket': "coronagame-151a7.appspot.com",
    'messagingSenderId': "216602942663",
    'appId': "1:216602942663:web:aafe0b3403e04a7d8bb2e2",
    'measurementId': "G-F1XTC17H44"}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()


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


# Main
def main_screen():
    screen = Tk()
    screen.geometry("600x600")
    screen.title("Game Start")
    Label(text="Game Start", bg="grey", font=("calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login").pack()
    Label(text="").pack()
    Button(text="Register").pack()
    Label(text="").pack()
    Button(text="Start").pack()

    screen.mainloop()

main_screen()

# ans=input("Are you a new user?[y/n]")

'''if ans == 'n':
    login()
elif ans == 'y':
    signup()'''

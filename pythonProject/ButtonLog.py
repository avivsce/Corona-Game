import os
from tkinter import *
from tkinter.ttk import *

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import db
#Use a service account



cred = credentials.Certificate('firebase-sdk.json')
firebase = firebase_admin.initialize_app(cred, {
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

#firebase = firebase_admin.initialize_app(cred)
db = firestore.client()
#auth = firebase_admin.auth()



root = Tk()
root.geometry("500x300")

def getvals():
    print(nameentry.get())
    print(passwordentry.get())
    user = db.create_user_with_email_and_password(nameentry.get(), passwordentry.get())


# heading
Label(root, text="Registration Form", font="arial 15 bold").grid(row=0, column=3)

# Field name
name = Label(root, text="  Name: ")
password = Label(root, text="  Password: ")

# Packing Fields
name.grid(row=1, column=2)
password.grid(row=2, column=2)

# Variable for storing data
namevalue = StringVar
passvalue = StringVar

checkvalue = IntVar

# Creating entry field
nameentry = Entry(root, textvariable=namevalue)
passwordentry = Entry(root, textvariable=passvalue)
print(nameentry.get())
# packiny entry fields
nameentry.grid(row=1, column=3)
passwordentry.grid(row=2, column=3)

def run_p():
    os.system('UserCheck.py')
Button(text="User Select", command=run_p).grid(row=9,column=3)

# Submit button
Button(text="Submit", command=getvals).grid(row=10, column=3)


root.mainloop()
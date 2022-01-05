import unittest

from pyrebase import pyrebase

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

import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth

cred = credentials.Certificate("firebase_sdk.json")
firebase_admin.initialize_app(cred)
Auth = firebase.auth()


class MyTestCase(unittest.TestCase):
    def test_CreateUser(self):
        '''
                sign_up(user)
                run over DB and find user (by email)
                if found -> return true
                else -> return false
                delete user
                :return:
                '''

        email = "test@test.com"
        password = "123456"

        Auth.create_user_with_email_and_password(email, password)  # sign in with email and password data
        user = auth.get_user_by_email(email)  # find the user by email in DB
        try:
            Auth.sign_in_with_email_and_password(email, password)
        except:
            pass
        self.assertNotEqual(user, None)  # check if user not None
        auth.delete_user(user.uid)  # delete the temp user

    def test_CreateUser_alreadyExist(self):
        '''
        sign_up(user)
        run over DB and find user (by email)
        if found -> return true
        else -> return false
        delete user
        :return:
        '''

        email = "test@test.com"
        password = "123456"

        Auth.create_user_with_email_and_password(email, password)  # create user once
        user = auth.get_user_by_email(email)  # find the user by email in DB
        try:
            Auth.create_user_with_email_and_password(email, password)  # create the same user the second time
        except:
            self.assertEqual(True, True)  # if the second trying of creating user raised an exception -> pass the test
            auth.delete_user(user.uid)  # delete the temp user
            return

        self.assertEqual(True, False)  # if there wasn't any exception -> fail the test
        auth.delete_user(user.uid)  # delete the temp user

    def test_SignInUser(self):
        '''
        createUser(email,password)
        signIn(email,password)
        if sign in succeeded -> return true
        return false
        '''

        email = "test@test.com"
        password = "123456"

        Auth.create_user_with_email_and_password(email, password)  # create user with email,password data
        user = auth.get_user_by_email(email)  # find the user by email in DB
        try:
            Auth.sign_in_with_email_and_password(email, password)  # sign in with email and password
        except:
            self.assertEqual(True, False)
            return

        self.assertEqual(True, True)
        auth.delete_user(user.uid)  # delete the temp user

    def test_SignInUser_nonExiting(self):
        '''
        signIn(email,password)
        if sign in succeeded -> return false
        return true
        '''

        email = "test@test.com"
        password = "123456"

        try:
            Auth.sign_in_with_email_and_password(email, password)  # sign in with email and password
        except:
            self.assertEqual(True, True)
            return

        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()

#Username and Password Test
from pickle import *
import os

usernames=[]
passwords=[]


f = open("password.pkl", "rb")
passwords.append(load(f))
f.close()

def askPassword():
    password=input("Password: ")
    passwords.append(password)
    print(usernames)
    print(passwords)

if __name__=="__main__":
    print(usernames)
    print(passwords)
    askPassword()

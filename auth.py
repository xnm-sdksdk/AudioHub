import hashlib
import os
from tkinter import messagebox
import tkinter as tk


usersFile = "/home/xnm/Documents/Algoritmia_Estrutura_de_Dados/24_25/AudioHub/files"

    # funcao login
def loginAccount():
    name = str(input())
    password = str(input())
    user_input = name or 'N/A'
    with open('users.txt', mode = 'r', encoding= 'utf-8') as usersFile:
        usersFile.read(name, password).split("\n")


# funcao criar conta
def createAccount():
    name = str(input("name: "))
    password = str(input("password: "))
    confirm_password = str(input("confirm password: "))
    try:
        with open('users.txt', mode = 'a', encoding= 'utf-8') as usersFile:
            userInfo = f"{name};{password};{confirm_password}\n"
            usersFile.writelines(userInfo) 
    except IOError:
        print("error")
    
    


def logoutAccount():
    pass



def validateSession():
    pass

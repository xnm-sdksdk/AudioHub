from imports import *
from tkinter import *

usersFile = "/home/xnm/Documents/Algoritmia_Estrutura_de_Dados/24_25/AudioHub/files/users.txt"

# Area destined to manage users
def mainLayout():
    
    mainLayout = tk.Tk()
    mainFrame = tk.Frame(mainLayout, width=200, height=200)
    mainFrame.grid(row=0, column=0, padx=0)
    
    
    listbox = Listbox(mainFrame)
    
    listbox.grid(row=0, column=0, padx=0)  


    with open(usersFile, "r") as file:
        users = file.readlines()
        for user in users:
            cleanFile = user.strip().replace(';', '')
            listbox.insert(END, cleanFile)
            
    
    promoteAdmin = tk.Button(mainLayout, text="Promote User")
    promoteAdmin.grid(row=0, column=1)
    
    demoteUser = tk.Button(mainLayout, text="Demote User")
    demoteUser.grid(row=0, column=1)
            
    deleteButton = tk.Button(mainLayout, text="Delete User")
    deleteButton.grid(row=1, column=1)
    
    mainLayout.mainloop()


if __name__ == "__main__":
    mainLayout()
from imports import *
from tkinter import *

usersFile = "/home/xnm/Documents/Algoritmia_Estrutura_de_Dados/24_25/AudioHub/files"

# Area destined to manage users
def mainLayout():
    
    mainLayout = tk.Tk()
    mainFrame = tk.Frame(mainLayout, width=200, height=200)
    mainFrame.grid(row=0, column=0, padx=0)
    
    
    listbox = Listbox(mainFrame)
    
    listbox.grid(row=0, column=0, padx=0)  
    
    mainLayout.mainloop()
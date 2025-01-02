from imports import *

def optionsMenu():
    secondary = customtkinter.CTk()
    secondary.title("Secondary Window")
    secondary.geometry("300x200")
    
    label = customtkinter.CTkLabel(secondary, text="This is the second window")
    label.pack(pady=20)
    
    secondary.mainloop()
    

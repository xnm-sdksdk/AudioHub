from imports import *

def optionsMenu(toggle_frame):
    appEntry = customtkinter.CTk()
    appEntry.title("Secondary Window")
    appEntry.geometry("300x200")
    
    tabView = customtkinter.CTkTabview(appEntry, width=500, height=500, fg_color="black")
    tabView.pack(padx=20, pady=20) 
    
    tabView = tabView.add("Catalog")
    tabView = tabView.add("Settings")
    
    
    tabView.set("Catalog")
       
    
    appEntry.mainloop()
    

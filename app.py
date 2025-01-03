from imports import *

def optionsMenu(toggle_frame):
    appEntry = tk.Tk()
    appEntry.title("Secondary Window")
    appEntry.geometry("300x200")
    
    tabView = tk.Frame(appEntry, width=500, height=500, fg_color="black")
    tabView.pack(padx=20, pady=20)    
    
    appEntry.mainloop()
    

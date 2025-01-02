
#from auth import LoginForm, RegisterForm
from app import optionsMenu
from imports import *



def main():
    main = customtkinter.CTk()
    main.title("Audio Hub")
    

    mainFrame = customtkinter.CTkFrame(main, width=200, height=200)
    mainFrame.grid(row=0, column=0, padx=0)
            
    # Add a button to open the options menu (replaces the view)
    button = customtkinter.CTkButton(mainFrame, text="Open Options Menu", command= lambda: toggleDisplayFrame(mainFrame))
    button.pack(pady=20)
        
        
        
    
def toggleDisplayFrame(frame):
    for widget in frame.winfo_children():
        widget.destroy()
    optionsMenu(frame)
                    
if __name__ == "__main__":
    main()
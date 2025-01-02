
#from auth import LoginForm, RegisterForm
from app import optionsMenu
from imports import *



def main():
    main = customtkinter.CTk()
    main.title("Audio Hub")
    
    
    # open app window
    button = customtkinter.CTkButton(main, text="open my n", command=optionsMenu)
    button.pack(pady=20)
    main.mainloop()
    
    
if __name__ == "__main__":
    main()
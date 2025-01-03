
#from auth import LoginForm, RegisterForm
from app import optionsMenu
from imports import *



def main():
    main = tk.Tk()
    main.title("Audio Hub")
    

    mainFrame = tk.Frame(main, width=200, height=200)
    mainFrame.grid(row=0, column=0, padx=0)
            
    # Add a button to open the options menu (replaces the view)
    button = tk.Button(mainFrame, text="Open Options Menu", command= lambda: toggleDisplayFrame(mainFrame))
    button.pack(pady=20)
    
    main.mainloop()
        
        
        
    
def toggleDisplayFrame(frame):
    for widget in frame.winfo_children():
        widget.destroy()
    optionsMenu(frame)
                    
if __name__ == "__main__":
    main()
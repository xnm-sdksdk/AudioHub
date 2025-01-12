from imports import *
from tkinter import *

usersFile = "/home/xnm/Documents/Algoritmia_Estrutura_de_Dados/24_25/AudioHub/files/users.txt"

# Area destined to manage users
    
mainLayout = tk.Tk()
mainLayout.title("Administration")
mainLayout.geometry("800x800")
mainFrame = tk.Frame(mainLayout, width=800, height=800)
mainFrame.grid(row=0, column=0)
    
    
listbox = Listbox(mainFrame, width=30, height=20)
listbox.grid(row=1, column=0, padx=0)  

if os.path.exists(usersFile):
    with open(usersFile, "r") as file:
        try:
            for line in file:
                user = line.strip()
                if user:
                    listbox.insert(END, user)
        except:
            print("Error reading file: ", __file__)
            
    
def promoteUser():
    pass


def demoteUser():
    pass


def deleteUser():
    selectedUser = listbox.get(tk.ACTIVE)
    
    if not selectedUser:
        messagebox.showerror("Delete", "Select a user to delete." )
        return
    
    if os.path.exists(usersFile):
        with open(usersFile, "r") as file:
            try:
                loadData = file.readline(file)
            except:
                print("Error reading file: ", __file__)
    else:
        messagebox.showerror("Deleting User", "Error deleting user!")
        
        
    if selectedUser in loadData:
        decision = messagebox.askyesno("Delete", "Are you sure you want to delete this user ?")
        if decision:
            loadData[selectedUser]
            
            with open(usersFile, "w") as file:
                file.write(loadData, file, indent=2)
            listbox.delete(tk.ACTIVE)
            messagebox.showinfo("Deleting User", f"User {selectedUser} delete.")
                

promoteAdminButton = tk.Button(mainLayout, text="Promote User")
promoteAdminButton.grid(row=0, column=3)
    
demoteUserButton = tk.Button(mainLayout, text="Demote User")
demoteUserButton.grid(row=0, column=4)
            
deleteButtonButton = tk.Button(mainLayout, text="Delete User")
deleteButtonButton.grid(row=0, column=5)
    
mainLayout.mainloop()

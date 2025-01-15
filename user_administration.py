from imports import *
from tkinter import *

usersFile = "/home/xnm/Documents/Algoritmia_Estrutura_de_Dados/24_25/AudioHub/files/users.txt"

# Area destined to manage users
def mainUserAdministration():
    global mainLayout, treeview
    mainLayout = tk.Tk()
    mainLayout.title("Administration")
    mainLayout.geometry("1000x1000")
    mainFrame = tk.Frame(mainLayout, width=1000, height=1000)
    mainFrame.grid(row=0, column=0)
    
        
    left_frame = tk.Frame(mainFrame)
    left_frame.grid(row=0, column=0, padx=10, pady=1)
    
    paned = PanedWindow(mainFrame, width=7000, height=300, bd="3", relief="sunken")
    paned.grid(row=1, column=0)
    treeview = ttk.Treeview(paned, selectmode="browse", columns=("id", "name", "register", "type"), show="headings")
    treeview.heading("id", text="ID")
    treeview.heading("name", text="Name")
    treeview.heading("register", text="Register Date")
    treeview.heading("type", text="Type")
    treeview.column("id", width=100)
    treeview.column("name", anchor=tk.W, width=200)
    treeview.column("register", width=300)
    treeview.column("type", width=100)
    treeview.grid(row=2, column=0, padx=0)
    
    
    right_frame = tk.Frame(mainFrame)
    right_frame.grid(row=1, column=1, padx=10, pady=10)
    
    promoteAdminButton = tk.Button(right_frame, text="Promote User", command=promoteUser)
    promoteAdminButton.grid(row=0, column=8, pady=5, padx=15)
        
    demoteUserButton = tk.Button(right_frame, text="Demote User", command=demoteUser)
    demoteUserButton.grid(row=1, column=8, pady=5, padx=15)
                
    deleteButtonButton = tk.Button(right_frame, text="Delete User", command=deleteUser)
    deleteButtonButton.grid(row=2, column=8, pady=5, padx=15)

            
def populateTreeView():
    for item in treeview.get_children():
        treeview.delete(item)
        
    if os.path.exists(usersFile):
        try:
            with open(usersFile, "r") as file:
                for line in file:
                    user = line.strip().split(";")
                    if len(user) >= 2:
                        treeview.insert("", "end", values=(user[0], user[1], user[3], user[4]))
        except Exception as e:
            messagebox.showerror("Error", f"Failed to read users file: {str(e)}")
    else:
        messagebox.showerror("Error", "Users file not found")
    
    
def promoteUser():
    selectedUser = treeview.focus()
    
    if not selectedUser:
        messagebox.showerror("Promote", "Select a user to promote." )
        return
    
    data = treeview.item(selectedUser)["values"]
    name = data[1]
    
    confirme = messagebox.askyesno("Confirm Promotion", f"Are you sure you want to promote user '{name}'?")
    if not confirme:
        return
    
    
    try:
        lines = []
        with open(usersFile, "r") as file:
            for line in file:
                uData = line.strip().split(";")
                if len(uData) >= 2 and uData[1] == name and uData[4] == "user":
                    uData[4] = "admin"
                lines.append(";".join(uData) + "\n")

        with open(usersFile, "w") as file:
            file.writelines(lines)
        treeview.delete(selectedUser)
        populateTreeView()
    except Exception as e:
        messagebox.showerror("Error promoting user", f"Error promoting user: {str(e)}")
        return
        

def demoteUser():
    selectedUser = treeview.focus()
    
    if not selectedUser:
        messagebox.showerror("Demote", "Select a user to demote." )
        return
    
    data = treeview.item(selectedUser)["values"]
    name = data[1]
    
    confirme = messagebox.askyesno("Confirm Demotion", f"Are you sure you want to demote user '{name}'?")
    if not confirme:
        return
    
    
    try:
        lines = []
        with open(usersFile, "r") as file:
            for line in file:
                uData = line.strip().split(";")
                if len(uData) >= 2 and uData[1] == name and uData[4] == "admin":
                    uData[4] = "user"
                lines.append(";".join(uData) + "\n")

        with open(usersFile, "w") as file:
            file.writelines(lines)
        treeview.delete(selectedUser)
        populateTreeView()
    except Exception as e:
        messagebox.showerror("Error demoting user", f"Error demoting user: {str(e)}")
        return


def deleteUser():
    selectedUser = treeview.focus()
    
    if not selectedUser:
        messagebox.showerror("Delete", "Select a user to delete." )
        return
    
    data = treeview.item(selectedUser)["values"]
    name = data[1]
    
    confirme = messagebox.askyesno("Confirm Deletion", f"Are you sure you want to delete user '{name}'?")
    if not confirme:
        return
    
    try:
        with open(usersFile, "r") as file:
            loadData = file.readlines()
        with open(usersFile, "w") as file:
            for line in loadData:
                uData = line.strip().split(";")
                if len(uData) >= 2 and uData[1] != name:
                    file.write(line)
        treeview.delete(selectedUser)
        populateTreeView()
        messagebox.showinfo("User deleted", f"User {name}, deleted successfully.")
    except Exception as e:
        messagebox.showerror("Error deleting user", f"Error deleting user: {str(e)}")
        return
            

mainUserAdministration()
populateTreeView() 
mainLayout.mainloop()

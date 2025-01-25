from imports import *
from tkinter import *

usersFile = "/home/xnm/Documents/Algoritmia_Estrutura_de_Dados/24_25/AudioHub/files/users.txt"

# Area destined to manage users
def mainUserAdministration():
    global mainLayout, treeview
    
    mainLayout = Tk()
    mainLayout.title("Administration")
    mainLayout.geometry("800x600")
    mainLayout.resizable(False, False)
    
    mainFrame = Frame(mainLayout, padx=10, pady=10)
    mainFrame.pack(fill=BOTH, expand=True)
    
    # Left Frame
    left_frame = Frame(mainFrame)
    left_frame.pack(side=LEFT, fill=BOTH, expand=True, padx=10, pady=10)
    
    # TreeView Structure
    treeview = ttk.Treeview(left_frame, selectmode="browse", columns=("id", "name", "register", "type"), show="headings")
    treeview.heading("id", text="ID")
    treeview.heading("name", text="Name")
    treeview.heading("register", text="Register Date")
    treeview.heading("type", text="Type")
    treeview.column("id", width=100)
    treeview.column("name", anchor=W, width=150)
    treeview.column("register", width=200)
    treeview.column("type", width=100)
    treeview.pack(fill=BOTH, expand=True, padx=5, pady=5)
    
    # Right Frame
    right_frame = Frame(mainFrame)
    right_frame.pack(side=RIGHT, fill=Y, padx=10, pady=10)
    
    promoteAdminButton = Button(right_frame, text="Promote User", command=promoteUser, width=15)
    promoteAdminButton.pack(pady=5)
    
    demoteUserButton = Button(right_frame, text="Demote User", command=demoteUser, width=15)
    demoteUserButton.pack(pady=5)
    
    deleteButtonButton = Button(right_frame, text="Delete User", command=deleteUser, width=15)
    deleteButtonButton.pack(pady=5)
    
# Function to load into the TreeView the data
def populateTreeView():
    for item in treeview.get_children():
        treeview.delete(item)
    
    if os.path.exists(usersFile):
        try:
            with open(usersFile, "r") as file:
                for line in file:
                    user = line.strip().split(";")
                    if len(user) >= 4:
                        treeview.insert("", "end", values=(user[0], user[1], user[3], user[4]))
        except Exception as e:
            messagebox.showerror("Error", f"Failed to read users file: {str(e)}")
    else:
        messagebox.showerror("Error", "Users file not found")

# Function to promote user
def promoteUser():
    selectedUser = treeview.focus()
    if not selectedUser:
        messagebox.showerror("Promote", "Select a user to promote.")
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
                if len(uData) >= 5 and uData[1] == name and uData[4] == "user":
                    uData[4] = "admin"
                lines.append(";".join(uData) + "\n")

        with open(usersFile, "w") as file:
            file.writelines(lines)
        populateTreeView()
    except Exception as e:
        messagebox.showerror("Error", f"Error promoting user: {str(e)}")

# Function to demote user
def demoteUser():
    selectedUser = treeview.focus()
    if not selectedUser:
        messagebox.showerror("Demote", "Select a user to demote.")
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
                if len(uData) >= 5 and uData[1] == name and uData[4] == "admin":
                    uData[4] = "user"
                lines.append(";".join(uData) + "\n")

        with open(usersFile, "w") as file:
            file.writelines(lines)
        populateTreeView()
    except Exception as e:
        messagebox.showerror("Error", f"Error demoting user: {str(e)}")

# Function to delete user
def deleteUser():
    selectedUser = treeview.focus()
    if not selectedUser:
        messagebox.showerror("Delete", "Select a user to delete.")
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
                if len(uData) >= 5 and uData[1] != name:
                    file.write(line)
        populateTreeView()
        messagebox.showinfo("User deleted", f"User {name} deleted successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"Error deleting user: {str(e)}")

mainUserAdministration()
populateTreeView()
mainLayout.mainloop()

from imports import *

authFile = "/home/xnm/Documents/Algoritmia_Estrutura_de_Dados/24_25/AudioHub/files/users.txt"

# function to validate the session of the user
def validateSession():
    username = os.getenv("USERNAME_SESSION")
    user_uuid = os.getenv("USER_UUID")
    print(f"Session check: {username}, {user_uuid}") 
    if username and user_uuid:
        return True
    else:
        messagebox.showerror("Authentication Required", "Please log in first.")
        return False

# function to validate permissions
def validatePermissions():
    try:
        username_session = os.getenv("USERNAME_SESSION")
        if not username_session:
            messagebox.showerror("Permission", "Error: No active session found.")
            return False 
        
        with open(authFile) as file:
            for line in file:
                data = line.strip().split(";")
                if len(data) >= 5 and data[1] == username_session:
                    if data[4] == "admin":
                        return True
                    else:
                        messagebox.showerror("Permission", "Error: You don't have permission to access.")
                        return False
        messagebox.showerror("Permission", "Error: You don't have permission to access.")
        return False
    except Exception as e:
        messagebox.showerror("Permission", f"Error reading authentication file: {str(e)}")
        return False
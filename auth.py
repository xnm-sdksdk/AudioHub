from imports import *
from catalog import mainCatalog

authFile = "/home/xnm/Documents/Algoritmia_Estrutura_de_Dados/24_25/AudioHub/files/users.txt"

# Authentication Main Layout
def mainAuth():
    global authLayout, userName, passWord, authLoginFrame, authRegisterFrame, toggleLoginButton, toggleRegisterButton
    
    authLayout = tk.Tk()
    authLayout.title("Authentication")
    authLayout.geometry("400x300")
    authLayout.resizable(False, False)
    
    # Main Container Frame
    authFrame = tk.Frame(authLayout, padx=20, pady=20)
    authFrame.pack(expand=True)
    
    # Entry Variables
    userName = tk.StringVar()
    passWord = tk.StringVar()
    
    # Username and Password Label/Entry
    tk.Label(authFrame, text="Username").grid(row=0, column=0, sticky='w', pady=5)
    tk.Entry(authFrame, width=30, textvariable=userName).grid(row=0, column=1, pady=5)
    
    tk.Label(authFrame, text="Password").grid(row=1, column=0, sticky='w', pady=5)
    tk.Entry(authFrame, width=30, textvariable=passWord, show="*").grid(row=1, column=1, pady=5)
    
    # Login Frame
    authLoginFrame = tk.Frame(authFrame)
    loginButton = tk.Button(authLoginFrame, text="Login", command=loginAccount, width=20).pack()
    
    # Register Frame
    authRegisterFrame = tk.Frame(authFrame)
    registerButton = tk.Button(authRegisterFrame, text="Register", command=createAccount, width=20).pack()
    
    #buttons to toggle frame
    toggleRegisterButton = tk.Button(authFrame, text="Go to Register", command=lambda: toggleFrames("Register"))
    toggleRegisterButton.grid(row=3, column=0, columnspan=2, pady=5)
    
    toggleLoginButton = tk.Button(authFrame, text="Go to Login", command=lambda: toggleFrames("Login"))
    toggleLoginButton.grid(row=3, column=0, columnspan=2, pady=5)
    
    # Initialize with Login Frame
    toggleFrames("Login")
    
# Login Method
def loginAccount():
    username = userName.get()
    password = passWord.get()
    
    if not username or not password:
        messagebox.showwarning("Login", "Username or Password not filled!")
        return
    
    if os.path.exists(authFile):
        try:
            with open(authFile, "r") as usersFile:
                for user in usersFile:
                    data = user.strip().split(";")
                    if len(data) >= 3 and data[1] == username and data[2] == password:
                        messagebox.showinfo("Login", "Login Successful!")
                        os.environ["USERNAME_SESSION"] = data[1]
                        os.environ["ROLE_SESSION"] = data[4]
                        os.environ["USER_UUID"] = data[0]
                        authLayout.destroy()
                        mainCatalog()
                        return
            messagebox.showerror("Login", "User not found!")
        except Exception as e:
            messagebox.showerror("Login", f"Error: {str(e)}")

# Create Account Method
def createAccount():
    name = userName.get()
    password = passWord.get()
    
    if not name or not password:
        messagebox.showwarning("Register", "Username or Password not filled!")
        return
    
    if os.path.exists(authFile):
        try:
            with open(authFile, "r") as usersFile:
                for user in usersFile:
                    data = user.strip().split(";")
                    if len(data) >= 2 and data[1] == name:
                        messagebox.showerror("Register", "Username already exists!")
                        return
        except Exception as e:
            messagebox.showerror("Register", "Something went wrong!")
            return
    
    try:
        with open(authFile, "a") as write:
            data = f"{uuid.uuid4()};{name};{password};{datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')};user;\n"
            write.write(data)
            userName.set("")
            passWord.set("")
        messagebox.showinfo("Register", "Account created successfully!")
        toggleFrames("Login")
        return
    except Exception as e:
        messagebox.showerror("Register", f"Error creating account: {str(e)}")

# Toggle Frames
def toggleFrames(buttonType):
    if buttonType == "Login":
        authRegisterFrame.grid_remove()
        authLoginFrame.grid(row=2, column=0, columnspan=2, pady=10)
        toggleLoginButton.grid_remove()
        toggleRegisterButton.grid()
    else:
        authLoginFrame.grid_remove()
        authRegisterFrame.grid(row=2, column=0, columnspan=2, pady=10)
        toggleRegisterButton.grid_remove()
        toggleLoginButton.grid()
        
        
# function to logout the user of his session
def logout():
    os.environ.pop("USERNAME_SESSION", None)
    os.environ.pop("ROLE_SESSION", None)
    os.environ.pop("USER_UUID", None)
    
    messagebox.showinfo("Logout", "You have been logged out successfully!")
    mainAuth()
    return

# function to validate the session of the user
def validateSession():
    username = os.getenv("USERNAME_SESSION")
    user_uuid = os.getenv("USER_UUID")
    if username and user_uuid:
        return True
    else:
        return False

def validatePermissions():
    try:
        with open(authFile) as file:
            for line in file:
                data = line.strip().split(";")
                if data[4] == "admin":
                    return True
        messagebox.showerror("Permission", "Error: You don't have permission to access.")
        return False
    except Exception as e:
        messagebox.showerror("Permission", f"Error reading authentication file: {str(e)}")
        return
    
# Run the Application
mainAuth()
authLayout.mainloop()

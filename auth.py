from imports import *

authFile = "/home/xnm/Documents/Algoritmia_Estrutura_de_Dados/24_25/AudioHub/files/users.txt"


# auth mainlayout
authLayout = tk.Tk()
authLayout.title("Authentication")
authLayout.geometry("500x500")
authFrame = tk.Frame(authLayout, width=500, height=500)
authFrame.grid(row=0, column=0)

# entry variables
userName = tk.StringVar()
passWord = tk.StringVar()


# username and password label
usernameLabel = tk.Label(authFrame, text="Username")
usernameLabel.grid(row=0, column=0)

passwordLabel = tk.Label(authFrame, text="Password")
passwordLabel.grid(row=0, column=2)

# username and password input
usernameEntry = tk.Entry(authFrame, width=20, textvariable = userName)
usernameEntry.grid(row=1, column=0)

passwordEntry = tk.Entry(authFrame, width=20, textvariable = passWord)
passwordEntry.grid(row=1, column=2)


# login method
def loginAccount():
    username = userName.get()
    password = passWord.get()
    
    if os.path.exists(authFile):
        with open(authFile, "r") as usersFile:
            loadUser = usersFile.readline(usersFile)
            if username in loadUser:
                userData = loadUser[username]
                if userData["password"] == password:
                    messagebox.showinfo("Login", "Login Successful!")
            else:
                messagebox.showerror("Login", "User not found!")    

                

# create account method
def createAccount():
    name = userName.get()
    password = passWord.get()

    if not name or not password:
        messagebox.showerror("Register", "Username or Password not filled!")
        return

    if os.path.exists(authFile):
        with open(authFile, "r") as usersFile:
            for line in usersFile:
                try:
                    loadData = usersFile.readline(line)
                    print("Loaded data from file:", loadData)
                except:
                    messagebox.showerror("Register", "User not found")

    fileToWrite = open(authFile, "a")
    fieldData = name + ";" + password + ";" + datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S") + ";" + "user" + ";" + "\n"
    fileToWrite.write(fieldData)
    fileToWrite.close()
    messagebox.showinfo("Register", "Account created successfully!")
    return

def logoutAccount():
    pass



def validateSession():
    pass





# button register
registerButton = tk.Button(authFrame, text="Register", command=createAccount)
registerButton.grid(row=2, column=0)

# button login
loginButton = tk.Button(authFrame, text="Login", command=loginAccount)
loginButton.grid(row=3, column=0)

authLayout.mainloop()
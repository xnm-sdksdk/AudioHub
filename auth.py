from imports import *

usersFile = "/home/xnm/Documents/Algoritmia_Estrutura_de_Dados/24_25/AudioHub/files"


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

authObject =  {
"id": uuid.uuid4(),
"name": userName,
"resources": {
    "music": [],
    "podcasts": [],
},
    "auth": "user"
}


# login method
def loginAccount():
    username = userName.get()
    password = passWord.get()
    #with open('users.txt', mode = 'r', encoding= 'utf-8') as usersFile:
    for user in usersFile:
        usersFile.read(username, password).split("\n")


# create account method
def createAccount(name):
    file = open(usersFile, "r", encoding="utf-8")

    
    ##for user in usersFile:
        
    
    


def logoutAccount():
    pass



def validateSession():
    pass





# button register
registerButton = tk.Button(authFrame, text="Register", command=createAccount)
registerButton.grid(row=2, column=0)

authLayout.mainloop()
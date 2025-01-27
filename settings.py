from imports import *

def mainLayoutSettings():
    global settingsLayout
    
    settingsLayout = tk.Tk()
    settingsLayout.title("Settings")
    settingsLayout.geometry("400x400")
    settingsLayout.resizable(False, False)
    
    mainFrame = tk.Frame(settingsLayout, padx=10, pady=10)
    mainFrame.grid(row=0, column=0, padx=20, pady=20, sticky="nw")
    
    # Positioning buttons in different rows and columns
    tk.Button(mainFrame, text="Back", command= backToCatalog).grid(row=0, column=0, padx=5, pady=5, sticky="w")
    tk.Button(mainFrame, text="Categories Administration", command=openCategories).grid(row=1, column=0, padx=5, pady=5, sticky="w")
    tk.Button(mainFrame, text="Usage Statistics", command=openStatistics).grid(row=2, column=0, padx=5, pady=5, sticky="w")
    tk.Button(mainFrame, text="User Administration", command= openAdmin).grid(row=3, column=0, padx=5, pady=5, sticky="w")
    tk.Button(mainFrame, text="Logout", command=openLogout).grid(row=4, column=0, padx=5, pady=5, sticky="w")
    
    settingsLayout.mainloop()
    
def openCategories():
    from categories_administration import mainCategoriesAdministration
    from permissions import validatePermissions
    if validatePermissions():
        settingsLayout.destroy()
        mainCategoriesAdministration()     
    
def openStatistics():
    from usageStatistics import mainLayoutUsageStatistics
    from permissions import validatePermissions
    if validatePermissions():
        settingsLayout.destroy()
        mainLayoutUsageStatistics()
    
def openAdmin():    
    from user_administration import mainUserAdministration
    from permissions import validatePermissions
    if validatePermissions():
        settingsLayout.destroy()
        mainUserAdministration()
    
def openLogout():
    settingsLayout.destroy()
    from auth import logout
    logout()

def backToCatalog():
    from catalog import mainCatalog
    settingsLayout.destroy()
    mainCatalog()

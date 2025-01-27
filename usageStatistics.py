from imports import *

# files that hold the data
categoryData = "/home/xnm/Documents/Algoritmia_Estrutura_de_Dados/24_25/AudioHub/files/categories.txt"
imageData = "/home/xnm/Documents/Algoritmia_Estrutura_de_Dados/24_25/AudioHub/images"
resourcesData = "/home/xnm/Documents/Algoritmia_Estrutura_de_Dados/24_25/AudioHub/files/resources.txt"
likedSongsData = "/home/xnm/Documents/Algoritmia_Estrutura_de_Dados/24_25/AudioHub/files/liked_songs.txt"
likesData = "/home/xnm/Documents/Algoritmia_Estrutura_de_Dados/24_25/AudioHub/files/likes_favourites_comments.txt"
usersData = "/home/xnm/Documents/Algoritmia_Estrutura_de_Dados/24_25/AudioHub/files/users.txt"


def mainLayoutUsageStatistics():
    global userLayout
    userLayout = tk.Tk()
    userLayout.title("Usage Statistics")
    userLayout.geometry("400x400")
    userLayout.resizable(False, False)
    
    mainFrame = tk.Frame(userLayout, padx=10, pady=10)
    mainFrame.grid(row=0, column=0, padx=20, pady=20, sticky="nw")
    
    
    tk.Button(mainFrame, text="Back", command=backToSettings).grid(row=0, column=0, sticky="w")
    tk.Label(mainFrame, text=f"Number of Users: {numberOfUsers()}", font=40).grid(row=1, column=0, sticky="w")
    tk.Label(mainFrame, text=f"Number of Categories: {numberOfCategories()}", font=40).grid(row=2, column=0, sticky="w")
    tk.Label(mainFrame, text=f"Number of Musics: {numberOfMusics()}", font=40).grid(row=3, column=0, sticky="w")
    tk.Label(mainFrame, text=f"Number of Podcasts: {numberOfPodcasts()}", font=40).grid(row=4, column=0, sticky="w")

    userLayout.mainloop()
    
def numberOfUsers():
    if os.path.exists(usersData):
        try:
            with open(usersData, "r") as file:
                return sum(1 for line in file if line.strip())
        except Exception as e:
            messagebox.showerror("Error", f"Failed to read users file: {str(e)}")
            return 0
    return 0        

def numberOfCategories():
    if os.path.exists(categoryData):
        try:
            with open(categoryData, "r") as file:
                return sum(1 for line in file if line.strip())
        except Exception as e:
            messagebox.showerror("Error", f"Failed to read users file: {str(e)}")
            return 0
    return 0 

def numberOfMusics():
    if os.path.exists(categoryData):
        try:
            with open(categoryData, "r") as file:
                return sum(1 for line in file if line.strip().startswith("Music"))
        except Exception as e:
            messagebox.showerror("Error", f"Failed to read users file: {str(e)}")
            return 0
    return 0 

def numberOfPodcasts():
    if os.path.exists(categoryData):
        try:
            with open(categoryData, "r") as file:
                return sum(1 for line in file if line.strip().startswith("Podcast"))
        except Exception as e:
            messagebox.showerror("Error", f"Failed to read users file: {str(e)}")
            return 0
    return 0 


def backToSettings():
    from settings import mainLayoutSettings
    userLayout.destroy()
    mainLayoutSettings()
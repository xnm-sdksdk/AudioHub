# imports
from imports import *
from tkinter import *

# file to hold the data
categoryData = "/home/xnm/Documents/Algoritmia_Estrutura_de_Dados/24_25/AudioHub/files/categories.txt"
imageData = "/home/xnm/Documents/Algoritmia_Estrutura_de_Dados/24_25/AudioHub/images"
resourcesData = "/home/xnm/Documents/Algoritmia_Estrutura_de_Dados/24_25/AudioHub/files/resources.txt"
likedSongsData = "/home/xnm/Documents/Algoritmia_Estrutura_de_Dados/24_25/AudioHub/files/liked_songs.txt"
likesData = "/home/xnm/Documents/Algoritmia_Estrutura_de_Dados/24_25/AudioHub/files/likes_favourites_comments.txt"



# main layout
def mainCatalog():
    global catalogLayout, selectedCategory, genderMusic, genderPodcast, term, textDummy, searchEntry, combobox, canvas, categoryValue, typeCategory, selectedCategory
    
    catalogLayout = tk.Tk()
    catalogLayout.title("Catalog")
    catalogLayout.geometry("1000x800")
    
    catalogFrame = tk.Frame(catalogLayout)
    catalogFrame.grid(row=0, column=0, padx=20, pady=20, sticky="nw")
    
    # Select Category
    categoryValue = tk.StringVar()
    tk.Label(catalogFrame, text="Select a category:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
    combobox = ttk.Combobox(catalogFrame, textvariable=categoryValue, width=20)
    combobox.grid(row=0, column=1, padx=5, pady=5)
    
    # Resource Selection
    resource = tk.StringVar()
    tk.Label(catalogFrame, text="Add a resource:").grid(row=0, column=2, sticky="w", padx=5, pady=5)
    tk.Entry(catalogFrame, textvariable=resource, width=20).grid(row=0, column=3, padx=5, pady=5)
           
    # Add Resource Button
    tk.Button(catalogFrame, text="Add Resource", command=addResource).grid(row=0, column=4, padx=25, pady=5)
    
    buttonFrame = tk.Frame(catalogLayout)
    buttonFrame.grid(row=1, column=0, padx=20, pady=10, sticky="nw")
    
    # Align buttons within buttonFrame
    tk.Button(buttonFrame, text="Like Resource", command=likeResource).grid(row=0, column=0, padx=5, pady=5)
    tk.Button(buttonFrame, text="Comment Resource", command=commentResource).grid(row=0, column=1, padx=5, pady=5)
    tk.Button(buttonFrame, text="Add To Liked Songs", command=addToFavoritesSongs).grid(row=0, column=2, padx=5, pady=5)
    tk.Button(buttonFrame, text="My Liked Songs", command=getMyLikedSongs).grid(row=0, column=3, padx=5, pady=5)
    tk.Button(buttonFrame, text="Upload Cover", command=uploadCover).grid(row=0, column=4, padx=5, pady=5)
    
    contentFrame = tk.Frame(catalogLayout)
    contentFrame.grid(row=2, column=0, padx=10, pady=20, sticky="nw")
    
    # Treeview for displaying resources
    treeview = ttk.Treeview(contentFrame, selectmode="browse", columns=["category", "resource"], show="headings",)
    treeview.heading("category", text="Category")
    treeview.heading("resource", text="Resource")
    treeview.column("category", width=100)
    treeview.column("resource", width=100)
    treeview.grid(row=0, column=0, padx=5, pady=5, sticky="nw")
    
    # Canvas for cover upload or images
    canvasFrame = tk.Frame(contentFrame)
    canvasFrame.grid(row=0, column=1, padx=50, pady=5, sticky="nw")
    canvas = tk.Canvas(canvasFrame, width=300, height=300, bg="lightgray", relief="solid", borderwidth=1)
    canvas.grid(row=0, column=0, padx=5, pady=5)
    
    
    readGenders()
    catalogLayout.mainloop()
    
def addCategory():
    pass
    # type = selectedCategory.get().lower() + "_categories"
    # name = category.get().strip()
    
    # if not name or not type:
    #     messagebox.showerror("Category", "All category fields must be provided.")
    #     return
    
    # if os.path.exists(saveData):
    #     try:
    #         with open(saveData, 'r') as categoryFile:
    #             for categoryIteration in categoryFile:
    #                 data = categoryIteration.strip().split(";")
    #                 print(data)
    #     except Exception as e:
    #         messagebox.showerror("Category", "Something went wrong.")
    #         return
    
    # if name:
    #     if name not in categoryFile[type]:
    #         categoryFile[type][name] = []
    #         with open(saveData, "a") as saveFile:
    #             saveFile.write(categoryFile, saveFile)
    #         messagebox.showinfo("Category", "Category added!")
    #         populateGenders()
    #     else:
    #         messagebox.showerror("Category", "Category already exists!")
    # else:
    #     messagebox.showerror("Category", "Category cannot be empty!")
    


def addResource():
    pass


def likeResource():
    pass


def commentResource():
    pass


def addToFavoritesSongs():
    pass

def uploadCover():
    global imageCover
    
    try:
        fileTypes = [('Jpg Files', '*.jpg'), ('Webp Files', '*.webp')]
        fileName = filedialog.askopenfilename(filetypes=fileTypes)
        
        if not fileName or os.path.isdir(fileName):
            messagebox.showerror("Error", "Invalid file selected. Please select an image file.")
            return

        img = Image.open(fileName)
        img = img.resize((400, 300))
        imageCover = ImageTk.PhotoImage(img)

        canvas.delete("all")
        canvas.create_image(0, 0, anchor="nw", image=imageCover)
        canvas.image = imageCover
        
    except FileNotFoundError:
        messagebox.showerror("Image", "File not found. Please select a valid image.")
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong: {e}")

    
def getMyLikedSongs():
    pass

def getAllSongs():
    pass

def getAllPodcasts():
    pass


def updateGenres():
    pass

def readGenders():
    if os.path.exists(categoryData):
        try:
            with open(categoryData, "r") as file:
                for line in file:
                    clean_line = line.strip().split(";")[1]
                    if clean_line not in combobox['values']:
                        combobox['values'] = (*combobox['values'], clean_line)
        except Exception as e:
            messagebox.showerror("Genres", "Something went wrong while reading genres!")
            return


# def populateGenders():
#     selected = selectedCategory.get().lower()
#     genres = readGenders()
    
#     if selected == "music":
#         genderMusic["values"] = genres["music"]
#     else:
#         messagebox.showerror("Category", "Category not found!")



# run the app
mainCatalog()
# imports
from imports import *

# file to hold the data
categoryData = "/home/xnm/Documents/Algoritmia_Estrutura_de_Dados/24_25/AudioHub/files/categories.txt"
imageData = "/home/xnm/Documents/Algoritmia_Estrutura_de_Dados/24_25/AudioHub/images"
resourcesData = "/home/xnm/Documents/Algoritmia_Estrutura_de_Dados/24_25/AudioHub/files/resources.txt"
likedSongsData = "/home/xnm/Documents/Algoritmia_Estrutura_de_Dados/24_25/AudioHub/files/liked_songs.txt"
likesData = "/home/xnm/Documents/Algoritmia_Estrutura_de_Dados/24_25/AudioHub/files/likes_favourites_comments.txt"



# main layout
def mainCatalog():
    global catalogLayout, selectedCategory, category, genderMusic, genderPodcast, term, textDummy, searchEntry, canvas, categoryValue
    
    catalogLayout = tk.Tk()
    catalogLayout.title("Catalog")
    catalogLayout.geometry("1000x800")
    
    catalogFrame = tk.Frame(catalogLayout)
    catalogFrame.grid(row=0, column=0, padx=20, pady=20, sticky="nw")
    
    # Category Selection
    category = tk.StringVar()
    tk.Label(catalogFrame, text="Add a category:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
    tk.Entry(catalogFrame, textvariable=category, width=20).grid(row=0, column=1, padx=5, pady=5)
    
    
    # Select Category
    categoryValue = tk.StringVar()
    tk.Label(catalogFrame, text="Select a category:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
    ttk.Combobox(catalogFrame, textvariable=categoryValue, width=20).grid(row=1, column=1, padx=5, pady=5)
    
    # Resource Selection
    resource = tk.StringVar()
    tk.Label(catalogFrame, text="Add a resource:").grid(row=1, column=2, sticky="w", padx=50, pady=5)
    tk.Entry(catalogFrame, textvariable=resource, width=20).grid(row=1, column=3, padx=5, pady=5)
    
    # Category Dropdown
    tk.Label(catalogFrame, text="Type:").grid(row=2, column=0, sticky="w", padx=5, pady=5)
    selectedCategory = tk.StringVar()
    typeCategory = ttk.Combobox(catalogFrame, textvariable=selectedCategory, state="readonly", width=18)
    typeCategory['values'] = ('Podcast', 'Music')
    typeCategory.current(1)
    typeCategory.grid(row=2, column=1, padx=5, pady=5)
    
    # Gender Selection (Music & Podcast)
    tk.Label(catalogFrame, text="Select Genre:").grid(row=3, column=0, sticky="w", padx=5, pady=5)
    
    genderMusic = ttk.Combobox(catalogFrame, state="normal", width=18)
    genderMusic.grid(row=3, column=1, padx=5, pady=5)
    
    genderPodcast = ttk.Combobox(catalogFrame, state="disable", width=18)
    genderPodcast.grid(row=3, column=2, padx=5, pady=5)
    
    typeCategory.bind('<<ComboboxSelected>>', updateGenres)
    updateGenres()
    
    # Search Section
    searchFrame = tk.Frame(catalogLayout)
    searchFrame.grid(row=1, column=0, padx=20, pady=10, sticky="nw")
    
    tk.Label(searchFrame, text="Search:").grid(row=0, column=0, padx=5, pady=5)
    term = tk.StringVar()
    searchEntry = tk.Entry(searchFrame, textvariable=term, width=20)
    searchEntry.grid(row=0, column=1, padx=5, pady=5)
    searchEntry.focus_set()
    
    tk.Button(searchFrame, text="Search", command=searchMethod).grid(row=0, column=2, padx=5, pady=5)
    
    textDummy = tk.Text(searchFrame, height=1, width=30)
    textDummy.insert('1.0', "Search here...")
    textDummy.grid(row=1, column=0, columnspan=3, padx=5, pady=5)
    
    buttonFrame = tk.Frame(catalogLayout)
    buttonFrame.grid(row=2, column=0, padx=20, pady=10, sticky="nw")
    
    contentFrame = tk.Frame(catalogLayout)
    contentFrame.grid(row=3, column=0, padx=10, pady=20, sticky="nw")  
    
    listboxFrame = tk.Frame(contentFrame)
    listboxFrame.grid(row=0, column=0, padx=5, pady=5, sticky="w")  
    listbox = tk.Listbox(listboxFrame, height=15, width=40)
    listbox.grid(row=0, column=0, padx=5, pady=5)
    
    canvasFrame = tk.Frame(contentFrame)
    canvasFrame.grid(row=0, column=2, padx=50, pady=5, sticky="w")
    canvas = tk.Canvas(canvasFrame, width=300, height=300, bg="lightgray", relief="solid", borderwidth=1)
    canvas.grid(row=0, column=0, padx=5, pady=5)
    
    tk.Button(catalogFrame, text="Add Category", command=addCategory).grid(row=0, column=2, padx=5, pady=5)
    tk.Button(catalogFrame, text="Add Resource", command=addResource).grid(row=1, column=6, padx=25, pady=5)
    tk.Button(buttonFrame, text="Like Resource", command=likeResource).grid(row=1, column=2, padx=5, pady=5)
    tk.Button(buttonFrame, text="Comment Resource", command=commentResource).grid(row=1, column=3, padx=5, pady=5)
    tk.Button(buttonFrame, text="Add To Favorites", command=addToFavorites).grid(row=1, column=0, padx=5, pady=5)
    tk.Button(buttonFrame, text="My Liked Songs", command=getMyLikedSongs).grid(row=1, column=1, padx=5, pady=5)
    tk.Button(buttonFrame, text="Upload Cover", command=uploadCover).grid(row=1, column=4, padx=5, pady=5)

def addCategory():
    type = selectedCategory.get().lower() + "_categories"
    name = category.get().strip()
    
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


def addToFavorites():
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


def searchMethod():
    textDummy.tag_remove('found', '1.0', tk.END)
    term = searchEntry.get()
    
    if term:
        index = '1.0'
        while 1:
            index = textDummy.search(term, index, nocase=1, stopindex=tk.END)
            if not index:
                break
            lastIndex = '%s+%dc' % (index, len(term))
            
            textDummy.tag_add('found', index, lastIndex)
            index = lastIndex
        textDummy.tag_config('found', foreground='red')
    searchEntry.focus_set()
    
    
    
def getMyLikedSongs():
    pass

def getAllSongs():
    pass

def getAllPodcasts():
    pass


def updateGenres():
    pass

def readGenders():
    categories = []
    genres = []
    
    if os.path.exists(categoryData):
        try:
            with open(categoryData, "r") as file:
                for line in file:
                    category, genre = line.split().split("=")
                    categories.append(category)
                    genres.append(genre.split(";"))
        except Exception as e:
            messagebox.showerror("Genres", "Something went wrong while reading genres!")
    return categories, genres


def populateGenders():
    selected = selectedCategory.get().lower()
    genres = readGenders()
    
    if selected == "music":
        genderMusic["values"] = genres["music"]
    else:
        messagebox.showerror("Category", "Category not found!")



# run the app
mainCatalog()
catalogLayout.mainloop()
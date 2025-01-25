# imports
from imports import *

# file to hold the data
saveData = "/home/xnm/Documents/Algoritmia_Estrutura_de_Dados/24_25/AudioHub/files/categories.txt"


# main layout
def mainCatalog():
    global catalogLayout, selectedCategory, category, genderMusic, genderPodcast, term, textDummy, searchEntry
    
    catalogLayout = tk.Tk()
    catalogLayout.title("Catalog")
    catalogLayout.geometry("1000x800")
    
    catalogFrame = tk.Frame(catalogLayout)
    catalogFrame.grid(row=0, column=0, padx=20, pady=20, sticky="nw")
    
    # Category Selection
    tk.Label(catalogFrame, text="Add a category:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
    category = tk.StringVar()
    categoryEntry = tk.Entry(catalogFrame, textvariable=category, width=20)
    categoryEntry.grid(row=0, column=1, padx=5, pady=5)
    
    # Resource Selection
    tk.Label(catalogFrame, text="Add a resource:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
    resource = tk.StringVar()
    resourceEntry = tk.Entry(catalogFrame, textvariable=resource, width=20)
    resourceEntry.grid(row=1, column=1, padx=5, pady=5)
    
    # Category Dropdown
    tk.Label(catalogFrame, text="Type:").grid(row=2, column=0, sticky="w", padx=5, pady=5)
    selectedCategory = tk.StringVar()
    typeCategory = ttk.Combobox(catalogFrame, textvariable=selectedCategory, state="readonly", width=18)
    typeCategory['values'] = ('Podcast', 'Music')
    typeCategory.current(1)
    typeCategory.grid(row=2, column=1, padx=5, pady=5)
    
    # Gender Selection (Music & Podcast)
    tk.Label(catalogFrame, text="Select Genre:").grid(row=3, column=0, sticky="w", padx=5, pady=5)
    
    selectedComboMusic = tk.StringVar()
    genderMusic = ttk.Combobox(catalogFrame, textvariable=selectedComboMusic, state="readonly", width=18)
    genderMusic['values'] = ('Music',)
    genderMusic.current(0)
    genderMusic.grid(row=3, column=1, padx=5, pady=5)
    
    selectedComboPodcast = tk.StringVar()
    genderPodcast = ttk.Combobox(catalogFrame, textvariable=selectedComboPodcast, state="readonly", width=18)
    genderPodcast['values'] = ('Podcast',)
    genderPodcast.current(0)
    genderPodcast.grid(row=3, column=2, padx=5, pady=5)
    
    # Search Section
    searchFrame = tk.Frame(catalogLayout)
    searchFrame.grid(row=1, column=0, padx=20, pady=10, sticky="nw")
    
    tk.Label(searchFrame, text="Search:").grid(row=0, column=0, padx=5, pady=5)
    term = tk.StringVar()
    searchEntry = tk.Entry(searchFrame, textvariable=term, width=20)
    searchEntry.grid(row=0, column=1, padx=5, pady=5)
    searchEntry.focus_set()
    
    searchButton = tk.Button(searchFrame, text="Search", command=searchMethod)
    searchButton.grid(row=0, column=2, padx=5, pady=5)
    
    textDummy = tk.Text(searchFrame, height=1, width=30)
    textDummy.insert('1.0', "Search here...")
    textDummy.grid(row=1, column=0, columnspan=3, padx=5, pady=5)
    
    # Action Buttons
    buttonFrame = tk.Frame(catalogLayout)
    buttonFrame.grid(row=2, column=0, padx=20, pady=10, sticky="nw")
    
    tk.Button(catalogFrame, text="Add Category", command=addCategory).grid(row=0, column=2, padx=5, pady=5)
    tk.Button(catalogFrame, text="Add Resource", command=addResource).grid(row=1, column=2, padx=5, pady=5)
    tk.Button(buttonFrame, text="Like Resource", command=likeResource).grid(row=1, column=2, padx=5, pady=5)
    tk.Button(buttonFrame, text="Comment Resource", command=commentResource).grid(row=1, column=3, padx=5, pady=5)
    tk.Button(buttonFrame, text="Add To Favorites", command=addToFavorites).grid(row=1, column=0, padx=5, pady=5)
    tk.Button(buttonFrame, text="My Liked Songs", command=getMyLikedSongs).grid(row=1, column=1, padx=5, pady=5)

def addCategory():
    type = selectedCategory.get().lower() + "_categories"
    name = category.get().strip()
    
    if not name or not type:
        messagebox.showerror("Category", "All category fields must be provided.")
        return
    
    if os.path.exists(saveData):
        try:
            with open(saveData, 'r') as categoryFile:
                for categoryIteration in categoryFile:
                    data = categoryIteration.strip().split(";")
                    print(data)
        except Exception as e:
            messagebox.showerror("Category", "Something went wrong.")
            return
    
    if name:
        if name not in categoryFile[type]:
            categoryFile[type][name] = []
            with open(saveData, "a") as saveFile:
                saveFile.write(categoryFile, saveFile)
            messagebox.showinfo("Category", "Category added!")
            populateGenders()
        else:
            messagebox.showerror("Category", "Category already exists!")
    else:
        messagebox.showerror("Category", "Category cannot be empty!")
    


def addResource():
    pass


def likeResource():
    pass


def commentResource():
    pass


def addToFavorites():
    pass


def readGenders():
    global catalogFile
    with open(saveData, "r") as genderFile:
        try:
            catalogFile = genderFile.readline(genderFile)
        except:
            catalogFile


def populateGenders():
    getType = selectedCategory.get().lower() + "_categories"
    category_name = category.get().strip()
    
    if getType in catalogFile and category_name in catalogFile[type]:
        gender = catalogFile[type][category_name]
        if selectedCategory.get().lower() == "music":
            genderMusic["values"] = gender
        elif selectedCategory.get().lower() == "podcast":
            genderPodcast["values"] = gender
    else:
        messagebox.showerror("Category", "Category not found!")


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



# run the app
mainCatalog()
catalogLayout.mainloop()
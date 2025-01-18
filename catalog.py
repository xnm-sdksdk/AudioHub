# imports
from imports import *

# file to hold the data
saveData = "/home/xnm/Documents/Algoritmia_Estrutura_de_Dados/24_25/AudioHub/files/categories.txt"


# main layout
def mainCatalog():
    global catalogLayout, selectedCategory, category, genderMusic, genderPodcast, term, textDummy, searchEntry
    catalogLayout = tk.Tk()
    catalogLayout.title("Catalog")
    catalogLayout.geometry("800x800")
    catalogFrame = tk.Frame(catalogLayout, width=500, height=500)
    catalogFrame.grid(row=0, column=0)

        
    # category entry and label
    categoryLabel = tk.Label(catalogFrame, text="Select a category:")
    categoryLabel.grid(row=3, column=0)

    category = tk.StringVar()
    categoryEntry = tk.Entry(catalogFrame, width=20, textvariable = category)
    categoryEntry.grid(row=3, column=1)

    # resource entry and label
    resourceLabel = tk.Label(catalogFrame, text="Select a resource:")
    resourceLabel.grid(row=4, column=0)

    resource = tk.StringVar()
    resourceEntry = tk.Entry(catalogFrame, width=20, textvariable = resource)
    resourceEntry.grid(row=4, column=1)


    # combobox for the gender of music or podcast
    selectedComboMusic = tk.StringVar()
    genderMusic = ttk.Combobox(catalogFrame, textvariable = selectedComboMusic, state="readonly")
    genderMusic['values'] = ('Music')
    genderMusic.current(0)
    genderMusic.grid(row=2, column=3)

    selectedComboPodcast = tk.StringVar()
    genderPodcast = ttk.Combobox(catalogFrame, textvariable = selectedComboPodcast, state="readonly")
    genderPodcast['values'] = ('Podcast')
    genderPodcast.current(0)
    genderPodcast.grid(row=2, column=4)

    # combobox for categories selection
    selectedCategory = tk.StringVar()
    typeCategory = ttk.Combobox(catalogFrame, textvariable=selectedCategory)
    typeCategory['values'] = ('Podcast', 'Music')
    typeCategory.current(1)
    typeCategory.grid(row=2, column=1)
    
    # search Box
    term = tk.StringVar()
    searchFrame = tk.Frame(catalogLayout, width=500, height=500)
    searchFrame.grid(row=7, column=0)
    searchLabel = tk.Label(searchFrame, text="Search...")
    searchLabel.grid(row=7, column=2)
    searchEntry = tk.Entry(searchFrame, width=20, textvariable=term)
    searchEntry.grid(row=7, column=3)
    searchEntry.focus_set()
    searchButton = tk.Button(searchFrame, text="Search", command=searchMethod)
    searchButton.grid(row=7, column=6)
    # testing stage, change to array of songs or albums etc
    textDummy = tk.Text(searchFrame, height=1, width=20)
    textDummy.insert('1.0', "Search here...")
    textDummy.grid(row=10, column=3)
    
    # button category
    addCategoryButton = tk.Button(catalogFrame, text="Add Category", command=addCategory)
    addCategoryButton.grid(row=3, column=3)

    # # button resource
    addResourceButton = tk.Button(catalogFrame, text="Add Resource", command=addResource)
    addResourceButton.grid(row=4, column=3)

    # # button Like Resource
    # likeResourceButton = tk.Button(catalogLayout, text="Like Resource", command=likeResource)
    # likeResourceButton.grid(row=1, column=0)

    # # button comment Resource
    # commentResourceButton = tk.Button(catalogLayout, text="Comment Resource", command=commentResource)
    # commentResourceButton.grid(row=1, column=0)

    # # button favorites
    # addToFavoritesButton = tk.Button(catalogLayout, text="Add To Favorites", command=addToFavorites)
    # addToFavoritesButton.grid(row=1, column=0)


def addCategory():
    type = selectedCategory.get().lower() + "_categories"
    name = category.get().strip()
    if name:
        if name not in catalogFile[type]:
            catalogFile[type][name] = []
            with open(saveData, "a") as saveFile:
                saveFile.write(catalogFile, saveFile)
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

# run the app
mainCatalog()
catalogLayout.mainloop()





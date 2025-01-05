# imports
from imports import *

# initialization of the data
file = {"music_categories": {}, "podcast_categories": {}, "favorites": []}

# file to hold the data
saveData = "/home/xnm/Documents/Algoritmia_Estrutura_de_Dados/24_25/AudioHub/files/categories.json"


# main layout
catalogLayout = tk.Tk()
catalogLayout.title("Catalog")
catalogFrame = tk.Frame(catalogLayout, width=200, height=200)
catalogFrame.grid(row=0, column=0)

# combobox for categories selection
selectedCategory = tk.StringVar()
typeCategory = ttk.Combobox(catalogLayout, textvariable=selectedCategory)
typeCategory['values'] = ('Podcast', 'Music')
typeCategory.current(1)

typeCategory.grid(row=0, column=2)
    
# category layout
category = tk.StringVar()
categoryEntry = tk.Entry(catalogLayout, width=20, textvariable = category)
categoryEntry.grid(row=0, column=0)

def addCategory():
    type = selectedCategory.get().lower() + "_categories"
    name = category.get().strip()
    if name:
        if name not in file[type]:
            file[type][name] = []
            with open(saveData, "w") as saveFile:
                json.dump(file, saveFile, indent=4)
            print(f"Category '{name}' added.")
    
    


def addResource():
    pass


def likeResource():
    pass


def commentResource():
    pass


def addToFavorites():
    pass


# button category
addCategoryButton = tk.Button(catalogLayout, text="Add Category", command=addCategory)
addCategoryButton.grid(row=2, column=0)

# # button resource
# addResourceButton = tk.Button(catalogLayout, text="Add Resource", command=addResource)
# addResourceButton.grid(row=1, column=0)

# # button Like Resource
# likeResourceButton = tk.Button(catalogLayout, text="Like Resource", command=likeResource)
# likeResourceButton.grid(row=1, column=0)

# # button comment Resource
# commentResourceButton = tk.Button(catalogLayout, text="Comment Resource", command=commentResource)
# commentResourceButton.grid(row=1, column=0)

# # button favorites
# addToFavoritesButton = tk.Button(catalogLayout, text="Add To Favorites", command=addToFavorites)
# addToFavoritesButton.grid(row=1, column=0)

# run the app
catalogLayout.mainloop()





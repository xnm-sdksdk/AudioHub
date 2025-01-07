# imports
from imports import *

# initialization of the data
catalogFile = {"music_categories": {}, "podcast_categories": {}, "favorites": []}

# file to hold the data
saveData = "/home/xnm/Documents/Algoritmia_Estrutura_de_Dados/24_25/AudioHub/files/categories.json"


# main layout
catalogLayout = tk.Tk()
catalogLayout.title("Catalog")
catalogLayout.geometry("500x500")
catalogFrame = tk.Frame(catalogLayout, width=500, height=500)
catalogFrame.grid(row=0, column=0)

# combobox for categories selection
selectedCategory = tk.StringVar()
typeCategory = ttk.Combobox(catalogFrame, textvariable=selectedCategory)
typeCategory['values'] = ('Podcast', 'Music')
typeCategory.current(1)
typeCategory.grid(row=0, column=0)

    
# category entry and label
categoryLabel = tk.Label(catalogFrame, text="Select a category:")
categoryLabel.grid(row=1, column=0)

category = tk.StringVar()
categoryEntry = tk.Entry(catalogFrame, width=20, textvariable = category)
categoryEntry.grid(row=1, column=1)

# resource entry
category = tk.StringVar()
categoryEntry = tk.Entry(catalogFrame, width=20, textvariable = category)
categoryEntry.grid(row=2, column=0)


def addCategory():
    type = selectedCategory.get().lower() + "_categories"
    name = category.get().strip()
    if name:
        if name not in catalogFile[type]:
            catalogFile[type][name] = []
            with open(saveData, "a") as saveFile:
                json.dump(catalogFile, saveFile, indent=4)
            messagebox.showinfo("Category", "Category added!")
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


# button category
addCategoryButton = tk.Button(catalogFrame, text="Add Category", command=addCategory)
addCategoryButton.grid(row=2, column=0)

# # button resource
addResourceButton = tk.Button(catalogFrame, text="Add Resource", command=addResource)
addResourceButton.grid(row=2, column=1)

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





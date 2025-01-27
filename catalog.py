# imports
from imports import *
from tkinter import *

# file to hold the data
categoryData = "/home/xnm/Documents/Algoritmia_Estrutura_de_Dados/24_25/AudioHub/files/categories.txt"
imageData = "/home/xnm/Documents/Algoritmia_Estrutura_de_Dados/24_25/AudioHub/images"
resourcesData = "/home/xnm/Documents/Algoritmia_Estrutura_de_Dados/24_25/AudioHub/files/resources.txt"
likedSongsData = "/home/xnm/Documents/Algoritmia_Estrutura_de_Dados/24_25/AudioHub/files/liked_songs.txt"



# main layout
def mainCatalog():
    global catalogLayout, combobox, categoryValue, resourceVar, treeview
    
    catalogLayout = tk.Tk()
    catalogLayout.title("Catalog")
    catalogLayout.geometry("1000x800")
    
    mainFrame = tk.Frame(catalogLayout)
    mainFrame.grid(row=0, column=0, padx=20, pady=20, sticky="nw")
    
    topFrame = tk.Frame(mainFrame)
    topFrame.grid(row=0, column=0, padx=10, pady=10, sticky="nw")
    
    categoryValue = tk.StringVar()
    tk.Label(topFrame, text="Select a category:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
    combobox = ttk.Combobox(topFrame, textvariable=categoryValue, width=20)
    combobox.grid(row=0, column=1, padx=5, pady=5)
    
    resourceVar = tk.StringVar()
    tk.Label(topFrame, text="Add a resource:").grid(row=0, column=2, sticky="w", padx=5, pady=5)
    tk.Entry(topFrame, textvariable=resourceVar, width=20).grid(row=0, column=3, padx=5, pady=5)
    buttonFrame = tk.Frame(mainFrame)
    buttonFrame.grid(row=1, column=0, padx=10, pady=10, sticky="nw")
    
    
    tk.Button(buttonFrame, text="Get All", command=populateTreeView).grid(row=0, column=0, padx=15, pady=5)
    tk.Button(buttonFrame, text="Add Resource", command=addResource).grid(row=0, column=1, padx=15, pady=5)
    tk.Button(buttonFrame, text="Remove Resource", command=removeResource).grid(row=0, column=2, padx=15, pady=5)
    tk.Button(buttonFrame, text="Add To Liked Songs", command=addToFavoritesSongs).grid(row=0, column=3, padx=15, pady=5)
    tk.Button(buttonFrame, text="My Liked Songs", command=getMyLikedSongs).grid(row=0, column=4, padx=15, pady=5)
    tk.Button(buttonFrame, text="Settings", command=settings).grid(row=0, column=5, padx=15, pady=5)
    
    
    contentFrame = tk.Frame(mainFrame)
    contentFrame.grid(row=2, column=0, padx=10, pady=20, sticky="nw")
    
    treeview = ttk.Treeview(contentFrame, selectmode="browse", columns=["category", "resource"], show="headings")
    treeview.heading("category", text="Category", command=lambda: sortTreeView(treeview, "category", False))
    treeview.heading("resource", text="Resource", command=lambda: sortTreeView(treeview, "resource", False))
    treeview.column("category", width=250)
    treeview.column("resource", width=250)
    treeview.grid(row=0, column=0, padx=5, pady=5, sticky="nw")
    
    readGenders()
    populateTreeView()
    catalogLayout.mainloop()


def addResource():
    category = categoryValue.get()
    resource = resourceVar.get().strip()
    
    if not category:
        messagebox.showerror("Category", "Please select a category.")
        return
    
    if not resource:
        messagebox.showerror("Resource", "Please enter a resource.")
        return
    
    if category not in combobox['values']:
        messagebox.showerror("Category", "Invalid category selected.")
        return
    
    try:
        with open(resourcesData, "a") as file:
            file.write(f"{category};{resource}\n")
        messagebox.showinfo("Success", f"Resource '{resource}' added successfully under '{category}' category.")
        resourceVar.set("")
        populateTreeView()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while adding the resource: {str(e)}")
    
def removeResource():
    selected = treeview.focus()
    
    if not selected:
        messagebox.showerror("Remove Resource", "Select a resource to delete")
        return

    data = treeview.item(selected)["values"]
    name = data[1]
    
    confirme = messagebox.askyesno("Confirm Deletion", f"Are you sure you want to delete the resource '{name}'?")
    if not confirme:
        return
    
    try:
        with open(resourcesData, "r") as file:
            loadData = file.readlines()
        with open(resourcesData, "w") as file:
            for line in loadData:
                data = line.strip().split(";")
                if data[1] != name:
                    file.write(line)
        populateTreeView()
        messagebox.showinfo("Resource Deleted", f"Resource {name} deleted successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Error deleting resource: {str(e)}")
        return

def allResources():
    pass

def addToFavoritesSongs():
    selected = treeview.focus()
    
    if not selected:
        messagebox.showerror("Add to Favorites", "Select a resource to add to favorites")
        return

    data = treeview.item(selected)["values"]
    category = data[0]
    resource = data[1]
    
    try:
        with open(likedSongsData, "a") as file:
            file.write(f"{category};{resource}\n")
        messagebox.showinfo("Liked Songs", f"Resource '{resource}' added to your liked songs.")
        return
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while adding the resource to favorites: {str(e)}")
        return
    
def getMyLikedSongs():
    for item in treeview.get_children():
        treeview.delete(item)
    if os.path.exists(likedSongsData):
        try:
            with open(likedSongsData, "r") as file:
                for line in file:
                    resource = line.strip().split(";")
                    treeview.insert("", "end", values=(resource[0], resource[1]))
            messagebox.showinfo("Liked Songs", "Your liked songs have been loaded successfully.")
            return
        
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while loading the liked songs: {str(e)}")
            return
    else:
        messagebox.showinfo("No Liked Songs", "No liked songs found.")


def sortTreeView(treeview, col, descending):
    data = [(treeview.set(item, col), item) for item in treeview.get_children('')]
    data.sort(reverse = descending)
    for index, (val, item) in enumerate(data):
        treeview.move(item, '', index)
    treeview.heading(col, command = lambda: sortTreeView(treeview, col, not descending))


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


def populateTreeView():
    for item in treeview.get_children():
        treeview.delete(item)
        
    if os.path.exists(resourcesData):
        try:
            with open(resourcesData, "r") as file:
                for line in file:
                    resource = line.strip().split(";")
                    treeview.insert("", "end", values=(resource[0], resource[1]))
        except Exception as e:
            messagebox.showerror("Error", f"Failed to read resources file: {str(e)}")
            return
    else:
        messagebox.showerror("Error", "Resources file not found")
        return
        


def settings():
    from settings import mainLayoutSettings
    catalogLayout.destroy()
    mainLayoutSettings()
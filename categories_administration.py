from imports import *
from tkinter import *

categoriesFile = "/home/xnm/Documents/Algoritmia_Estrutura_de_Dados/24_25/AudioHub/files/categories.txt"

def mainCategoriesAdministration():
    global mainLayout, treeview, category_entry, categoryVar, typeVar
    
    mainLayout = Tk()
    mainLayout.title("Categories Administration")
    mainLayout.geometry("800x600")
    mainLayout.resizable(False, False)
    
    mainFrame = Frame(mainLayout, padx=10, pady=10)
    mainFrame.pack(fill=BOTH, expand=True)
    
    categoryVar = tk.StringVar()
    typeVar = tk.StringVar(value="Music")

    inputFrame = Frame(mainFrame)
    inputFrame.pack(pady=5)
    
    tk.Label(inputFrame, text="Add category:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
    category_entry = Entry(inputFrame, textvariable=categoryVar, width=30).grid(row=0, column=1, padx=5, pady=5, sticky="w")
    
    tk.Label(inputFrame, text="Type:").grid(row=0, column=2, padx=10, pady=5, sticky="w")
    musicRadioBtn = tk.Radiobutton(inputFrame, text="Music", variable=typeVar, value="Music")
    musicRadioBtn.grid(row=0, column=3, padx=5, pady=5, sticky="w")
    podcastRadioBtn = tk.Radiobutton(inputFrame, text="Podcast", variable=typeVar, value="Podcast")
    podcastRadioBtn.grid(row=0, column=4, padx=5, pady=5, sticky="w")
    
    # Left Frame
    left_frame = Frame(mainFrame)
    left_frame.pack(side=LEFT, fill=BOTH, expand=True, padx=10, pady=10)
    
    # TreeView Structure
    treeview = ttk.Treeview(left_frame, selectmode="browse", columns=("type", "name"), show="headings")
    treeview.heading("type", text="TYPE")
    treeview.heading("name", text="Name")
    treeview.column("type", width=100)
    treeview.column("name", anchor=W, width=150)
    treeview.pack(fill=BOTH, expand=True, padx=5, pady=5)
    
    # Right Frame
    right_frame = Frame(mainFrame)
    right_frame.pack(side=RIGHT, fill=Y, padx=10, pady=10)
    
    tk.Button(right_frame, text="Add category", command=addCategory, width=15).pack(pady=5)
    tk.Button(right_frame, text="Remove category", command=removeCategory, width=15).pack(pady=5)




def populateTreeView():
    for item in treeview.get_children():
        treeview.delete(item)
    if os.path.exists(categoriesFile):
        try:
            with open(categoriesFile, "r") as file:
                for line in file:
                    category = line.strip().split(";")
                    treeview.insert("", "end", values=(category[0], category[1]))
        except Exception as e:
            messagebox.showerror("Error", f"Failed to read categories file: {str(e)}")
    else:
        messagebox.showerror("Error", "Categories file not found")
        
        
def addCategory():
    categoryInputVar = categoryVar.get().strip().lower()
    typeInputVar = typeVar.get()
    
    if not categoryInputVar:
        messagebox.showwarning("Add Category", "Category name must be filled.")
        return
    
    if os.path.exists(categoriesFile):
        try:
            with open(categoriesFile, 'r') as file:
                for line in file:
                    data = line.strip().split(";")
                    if data[1] == categoryInputVar and data[0] == typeInputVar:
                        messagebox.showerror("Categories Administration", "Category already exists!")
                        return
        except Exception as e:
            messagebox.showerror("Categories Administration", "Something went wrong!")
            return
    
    if os.path.exists(categoriesFile):
        try:
            with open(categoriesFile, "a") as writeToFile:
                writeToFile.write(f"{typeInputVar};{categoryInputVar}\n")
            populateTreeView()
            categoryVar.set("")
        except Exception as e:
            messagebox.showerror("Add Category", f"Error adding category: {str(e)}")
            return
        
        
def removeCategory():
    selectedCategory = treeview.focus()
    if not selectedCategory:
        messagebox.showwarning("Delete Category", "Select a category to delete.")
        return

    data = treeview.item(selectedCategory)["values"]
    name = data[1]
    
    confirme = messagebox.askyesno("Confirm Deletion", f"Are you sure you want to delete user '{name}'?")
    if not confirme:
        return
    
    try:
        with open(categoriesFile, "r") as file:
            loadData = file.readlines()
        with open(categoriesFile, "w") as file:
            for line in loadData:
                uData = line.strip().split(";")
                if uData[1] != name:
                    file.write(line)
        populateTreeView()
    except Exception as e:
        messagebox.showerror("Error", f"Error deleting category: {str(e)}")
        return

mainCategoriesAdministration()
populateTreeView()
mainLayout.mainloop()
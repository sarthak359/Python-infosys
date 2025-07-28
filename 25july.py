import tkinter as tk
from tkinter import messagebox

# Callback function for menu actions
def menu_callback(action):
    print(f"{action} menu item clicked")

# Create the root window
root = tk.Tk()
root.title("Drop-Down Menu Example")

# Create the main menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Create the File menu and add it to the menu bar
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)

# You can add commands to the file_menu like this:
file_menu.add_command(label="New", command=lambda: menu_callback("New"))
file_menu.add_command(label="Open", command=lambda: menu_callback("Open"))
file_menu.add_command(label="Save", command=lambda: menu_callback("Save"))
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Run the main loop
root.mainloop()

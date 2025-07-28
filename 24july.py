import tkinter as tk
from tkinter import *

root = tk.Tk()
icon = PhotoImage(file='icon.png')
root.iconphoto(False, icon)

root.configure(bg="black")
root.title("hello sarthak here")
root.geometry("400x400")


label1 = tk.Label(root, text="hello sarthak here", bg="#FF5733")
label1.pack(fill=tk.BOTH, expand=True)

label1 = tk.Label(root, text="hello aggarwal here", bg="white")
label1.pack(fill=tk.BOTH, expand=True)

label2 = tk.Label(root, text="hello aggarwal sahab here", bg="red")
label2.pack(fill=tk.BOTH, expand=True)


root.mainloop()

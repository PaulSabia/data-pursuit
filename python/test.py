import tkinter as tk
from PIL import Image, ImageTk



root = tk.Tk()

image = Image.open("image.png")
image = ImageTk.PhotoImage(image)


label = tk.Label(root, image=image)
label.pack()


root.mainloop()


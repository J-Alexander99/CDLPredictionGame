import tkinter as tk
from tkinter import ttk

def create_gradient(canvas, color1, color2):
    width = canvas.winfo_width()
    height = canvas.winfo_height()
    r1, g1, b1 = int(color1[1:3], 16), int(color1[3:5], 16), int(color1[5:7], 16)
    r2, g2, b2 = int(color2[1:3], 16), int(color2[3:5], 16), int(color2[5:7], 16)
    
    for x in range(width):
        r = int((1.0 * (width - x) / width) * r1 + (1.0 * x / width) * r2)
        g = int((1.0 * (width - x) / width) * g1 + (1.0 * x / width) * g2)
        b = int((1.0 * (width - x) / width) * b1 + (1.0 * x / width) * b2)
        canvas.create_line(x, 0, x, height, fill=f'#{r:02x}{g:02x}{b:02x}')

def update_background(event=None):  
    left_color = left_dropdown.get()
    right_color = right_dropdown.get()
    canvas.delete("all")
    create_gradient(canvas, left_color, right_color)

root = tk.Tk()
root.title("Color Gradient Background")

# Dropdown for left color
left_label = ttk.Label(root, text="Left Color:")
left_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

left_dropdown = ttk.Combobox(root, values=["#FF0000", "#00FF00", "#0000FF", "#FFFF00", "#FFA500", "#800080"])
left_dropdown.grid(row=0, column=1, padx=10, pady=10)
left_dropdown.current(0)
left_dropdown.bind("<<ComboboxSelected>>", update_background)  

# Dropdown for right color
right_label = ttk.Label(root, text="Right Color:")
right_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

right_dropdown = ttk.Combobox(root, values=["#FF0000", "#00FF00", "#0000FF", "#FFFF00", "#FFA500", "#800080"])
right_dropdown.grid(row=1, column=1, padx=10, pady=10)
right_dropdown.current(1)
right_dropdown.bind("<<ComboboxSelected>>", update_background)  

# Canvas to display gradient
canvas = tk.Canvas(root, width=400, height=200)
canvas.grid(row=2, columnspan=2)

# Initial gradient
update_background()

root.mainloop()

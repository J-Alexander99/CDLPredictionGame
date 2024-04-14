import tkinter as tk
import subprocess

def run_file_with_link(file_name, link):
    subprocess.Popen(["python", file_name, link])

def run_third_file():
    subprocess.Popen(["python", "CDLGameScoreCount.py"])

def run_first_file():
    link = link_entry.get()
    print("running ggScraper...")
    run_file_with_link("ggScraper.py", link)

def run_second_file():
    link = link_entry.get()
    run_file_with_link("scoreline.py", link)

def create_gradient_background(canvas, color1, color2):
    canvas.delete('gradient')  # Clear previous gradient
    width = canvas.winfo_width()  # Get current canvas width
    height = canvas.winfo_height()  # Get current canvas height
    for x in range(width):
        # Interpolate between color1 and color2
        r = int(color1[0] + (color2[0] - color1[0]) * x / width)
        g = int(color1[1] + (color2[1] - color1[1]) * x / width)
        b = int(color1[2] + (color2[2] - color1[2]) * x / width)
        color = '#{:02x}{:02x}{:02x}'.format(r, g, b)
        canvas.create_line(x, 0, x, height, fill=color, tags='gradient')

# Create main window
root = tk.Tk()
root.title("CDL Prediction Game Results")

def on_resize(event):
    create_gradient_background(canvas, color1, color2)

# Bind the resize event
root.bind("<Configure>", on_resize)

# Create canvas for gradient background
canvas = tk.Canvas(root, width=400, height=300)
canvas.pack(fill='both', expand=True)

# Define the colors for the gradient
color1 = (255, 255, 255)  # white
color2 = (0, 0, 0)      # blue

# Create gradient background
create_gradient_background(canvas, color1, color2)

# Create frame for content
content_frame = tk.Frame(root, bg='white', padx=20, pady=20)
content_frame.place(relx=0.5, rely=0.5, anchor='center')

# Create entry for website link
link_label = tk.Label(content_frame, text="Enter website link:")
link_label.pack()

link_entry = tk.Entry(content_frame, width=50)
link_entry.pack()

# Create buttons
button1 = tk.Button(content_frame, text="Grab Player Stats", command=run_first_file)
button1.pack()

button2 = tk.Button(content_frame, text="Grab Game Scoreline", command=run_second_file)
button2.pack()

button3 = tk.Button(content_frame, text="Generate Prediction Results", command=run_third_file)
button3.pack()

# Run the Tkinter event loop
root.mainloop()

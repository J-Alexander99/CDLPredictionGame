import tkinter as tk
import subprocess

def run_file_with_link(file_name, link):
    subprocess.Popen(["python", file_name, link])

def run_third_file():
    subprocess.Popen(["python", "CDLGameScoreCount.py"])

def run_first_file():
    link = link_entry.get()
    run_file_with_link("ggScraper.py", link)

def run_second_file():
    link = link_entry.get()
    run_file_with_link("scoreline.py", link)

# Create main window
root = tk.Tk()
root.title("CDL Prediction Game Results")

# Create entry for website link
link_label = tk.Label(root, text="Enter website link:")
link_label.pack()
link_entry = tk.Entry(root, width=50)
link_entry.pack()

# Create buttons
button1 = tk.Button(root, text="Grab Player Stats", command=run_first_file)
button1.pack()

button2 = tk.Button(root, text="Grab Game Scoreline", command=run_second_file)
button2.pack()

button3 = tk.Button(root, text="Generate Prediction Results", command=run_third_file)
button3.pack()

# Run the Tkinter event loop
root.mainloop()

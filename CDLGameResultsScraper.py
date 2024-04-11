from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import os
import re
import time

def save_to_text_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

# URL of the webpage to scrape
url = "https://www.breakingpoint.gg/match/27258/Atlanta-FaZe-vs-Toronto-Ultra-at-CDL-Major-2-Qualifier-2024"

# Set up the Selenium Chrome driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Navigate to the URL
driver.get(url)

# Wait for the presence of all elements
time.sleep(5)  # Wait for 5 seconds (you can adjust this as needed)

# Parse the HTML content of the page
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Find all elements with class "mantine-155beqj" (each game mode section)
game_modes = soup.find_all(class_="mantine-155beqj")

# Prepare content to be written to the file
file_content = ""

# Iterate through each game mode section and extract relevant information
for game_mode in game_modes:
    mode_name = game_mode.find(class_="mantine-1ey6z4x").text
    file_content += "Game Mode: {}\n".format(mode_name)
    
    maps = game_mode.find_all(class_="mantine-1fr50if")
    for map_info in maps:
        map_name = map_info.find(class_="mantine-6cg8ua").text
        file_content += "Map Name: {}\n".format(map_name)
        
        # Print all plaintext within the map_info div
        plaintext = map_info.get_text(separator='\n', strip=True)
        print("Plaintext within map_info div:")
        print(plaintext)
        print()  # Adding a newline for better readability

# Get the absolute path of the directory where you want to save the file
save_directory = "C:/Users/joela/Downloads/CDL Game-20240405T204723Z-001/CDL Game/data"  # Replace this with your desired directory
filename = os.path.join(save_directory, "scraped_maps.txt")

# Save the extracted information to a text file
try:
    save_to_text_file(filename, file_content)
    print("File 'scraped_data.txt' created successfully in:", save_directory)
except Exception as e:
    print("Error occurred while creating the file:", e)

# Quit the Selenium driver
driver.quit()

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import os

def save_to_text_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

# URL of the webpage to scrape
url = "https://www.breakingpoint.gg/match/27278/Los-Angeles-Guerrillas-vs-Las-Vegas-Legion-at-CDL-Major-3-Qualifier-2024"

# Set up the Selenium Chrome driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Navigate to the URL
driver.get(url)

# Wait for the presence of all elements (you can adjust the sleep time as needed)
import time
time.sleep(5)

# Parse the HTML content of the page
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Find all scoreline elements
scoreline_elements = soup.find_all(class_="mantine-Text-root mantine-x468zj")

# Prepare content to be written to the file
file_content = ""

# Extracted scorelines
scorelines = [scoreline_element.text.strip() for scoreline_element in scoreline_elements if scoreline_element.text.strip().isdigit() or scoreline_element.text.strip() == "-"]

# Group scorelines into threes and concatenate
grouped_scorelines = [''.join(scorelines[i:i+3]) for i in range(0, len(scorelines), 3)]

# Labels for the groups
labels = ["Hardpoint", "SnD", "Control"]

# Assign labels to concatenated scorelines
for i, scoreline_group in enumerate(grouped_scorelines):
    label = labels[i % len(labels)]  # Cycle through labels if there are more than three groups
    file_content += "{}:\n{}\n".format(label, scoreline_group)

# Get the absolute path of the directory where you want to save the file
save_directory = "C:/Users/joela/Desktop/CDL Game/data"  # Replace this with your desired directory
filename = os.path.join(save_directory, "scraped_scorelines.txt")

# Save the extracted information to a text file
try:
    save_to_text_file(filename, file_content)
    print("File 'scraped_data.txt' created successfully in:", save_directory)
except Exception as e:
    print("Error occurred while creating the file:", e)

# Quit the Selenium driver
driver.quit()

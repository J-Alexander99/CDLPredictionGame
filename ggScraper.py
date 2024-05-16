from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import os
import sys
import time

def save_to_text_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

def scrape_website(url):
    # Set up the Selenium Chrome driver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    # Navigate to the URL
    driver.get(url)

    # Wait for the presence of the table elements
    time.sleep(5)  # Wait for 5 seconds (you can adjust this as needed)

    # Parse the HTML content of the page
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # Find all tables on the page
    tables = soup.find_all('tbody')

    # Determine the number of tables present
    num_tables = len(tables)

    # Define the table labels based on the number of tables
    table_labels = []
    if num_tables == 6:
        table_labels = ["Hardpoint", "Search and Destroy","Search and Destroy Info", "Control","Control Info", "Overall"]
    elif num_tables == 7:
        table_labels = ["Hardpoint", "Search and Destroy","Search and Destroy Info", "Control","Control Info","Hardpoint", "Overall"]
    elif num_tables == 10:
        table_labels = ["Hardpoint", "Search and Destroy","Search and Destroy Info", "Control","Control Info","Hardpoint","Search and Destroy", "Search and Destroy Info" ,"Overall"]
    else:
        print("Invalid number of tables present. " , "We Found: " , num_tables , " Tables")
        print(tables)

    # Output variable to store the printed data
    output = ""
    # Define the tables to skip
    tables_to_skip = {3, 5, 8}

    # Iterate over each table
    for i, (table, label) in enumerate(zip(tables, table_labels), start=1):
        if i in tables_to_skip:
            continue
        output += f"Table {i} ({label}):\n"

        # Find all rows in the table
        rows = table.find_all('tr')

        # Iterate over each row
        for row in rows:
            # Find all cells in the row
            cells = row.find_all('td')

            # Check if the first cell contains an image
            if cells[0].find('img'):
                # Extract team name
                team_name = cells[0].text.strip()
                # Append team name to output
                output += f"Team Name: {team_name}\n"
                # Skip this row
                continue

            # Extract player name and statistics
            player_name = cells[0].text.strip()
            statistics = [cell.text.strip() for cell in cells[1:]]

            # Append player name and statistics to output
            output += f"Player Name: {player_name}\n"
            output += f"Statistics: {statistics}\n"

        output += "\n"  # Add a newline between tables

    # Print the content before saving it to the file
    print(output)

    # Get the absolute path of the current working directory
    current_directory = os.getcwd()

   # Get the absolute path of the directory where you want to save the file
    save_directory = os.path.join(os.path.expanduser('~'), 'Desktop', 'CDLGame', 'data')
    filename = os.path.join(save_directory, 'scraped_data.txt')
    
    # Save the printed data to a text file directly
    try:
        with open(os.path.join(save_directory, "scraped_data.txt"), "w") as file:
            file.write(output)
        print("File 'scraped_data.txt' created successfully in:", save_directory)
    except Exception as e:
        print("Error occurred while creating the file:", e)

    # Quit the Selenium driver
    driver.quit()

if __name__ == "__main__":
    # Check if URL argument is provided
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <url>")
        sys.exit(1)

    # Get URL from command line arguments
    url = sys.argv[1]
    scrape_website(url)

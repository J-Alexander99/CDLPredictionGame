import json
import os

def combine_json_files(folder_path, output_file):
    combined_data = []

    # Iterate over all files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith('.json'):
            with open(os.path.join(folder_path, filename), 'r') as file:
                data = json.load(file)
                combined_data.extend(data)

    # Write the combined data to the output file
    with open(output_file, 'w') as outfile:
        json.dump(combined_data, outfile, indent=4)

# Example usage:
folder_path = 'C:/Users/joela/Desktop/CDLGame/data/test'  # Change this to the directory containing your JSON files
output_file = 'C:/Users/joela/Desktop/CDLGame/data/jsontest.json'  # Change this to the desired output file path

combine_json_files(folder_path, output_file)

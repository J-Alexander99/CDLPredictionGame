
import json

# Read the text file
file_path = "C:\\Users\\joela\\Desktop\\CDLGame\\data\\predictions.txt"
with open(file_path, "r") as file:
    lines = file.readlines()

# Initialize dictionary to hold predictions
predictions = {}

# Parse each line and add to respective list in dictionary
current_category = None
for line in lines:
    line = line.strip()
    if not line or ':' not in line:
        continue
    if line.endswith("Predictions:"):
        current_category = line.replace(" Predictions:", "")
        predictions[current_category] = []
    else:
        player, prediction = line.split(":")
        player = player.strip()
        prediction = prediction.strip()
        predictions[current_category].append({
            "Player": player,
            "Prediction": prediction
        })

# Print the parsed predictions
print("Parsed predictions:", predictions)

# Write dictionary to JSON file
json_file_path = "C:\\Users\\joela\\Desktop\\CDLGame\\data\\predictions.json"
with open(json_file_path, "w") as json_file:
    json.dump(predictions, json_file, indent=4)

print("JSON file created successfully at:", json_file_path)

import json
import re

# Read the text file
with open('C:\\Users\\joela\\Desktop\\CDLGame\\data\\predictions.txt', 'r') as file:
    lines = file.readlines()

# Initialize dictionaries to store predictions
hardpoint_predictions = {}
search_and_destroy_predictions = {}
control_predictions = {}
most_kills_overall_predictions = {}
least_kills_overall_predictions = {}
most_deaths_overall_predictions = {}
least_deaths_overall_predictions = {}
best_kd_ratio_overall_predictions = {}
worst_kd_ratio_overall_predictions = {}
most_damage_overall_predictions = {}
least_damage_overall_predictions = {}

# Parse the lines and populate the dictionaries
for line in lines:
    if not line.strip():  # Skip empty lines
        continue
    category, *predictions = line.strip().split(':')
    print("Category:", category)
    print("Predictions:", predictions)
    if not predictions:  # Skip if predictions is empty
        continue
    category = category.strip()
    if category == "Hardpoint Predictions":
        for prediction in predictions:
            match = re.match(r'\s*(\S+)\s*-\s*(\S+)\s*', prediction)
            if match:
                player, score = match.groups()
                hardpoint_predictions[player.strip()] = score.strip()
    elif category == "Search and Destroy Predictions":
        for prediction in predictions:
            match = re.match(r'\s*(\S+)\s*-\s*(\S+)\s*', prediction)
            if match:
                player, score = match.groups()
                search_and_destroy_predictions[player.strip()] = score.strip()
    elif category == "Control Predictions":
        control_predictions = {player.strip(): score.strip() for player, score in (prediction.split('-') for prediction in predictions)}
    elif category == "Most Kills Overall Predictions":
        most_kills_overall_predictions = {player.strip(): player2.strip() for player, player2 in (prediction.split(':') for prediction in predictions)}
    elif category == "Least Kills Overall Predictions":
        least_kills_overall_predictions = {player.strip(): player2.strip() for player, player2 in (prediction.split(':') for prediction in predictions)}
    elif category == "Most Deaths Overall Predictions":
        most_deaths_overall_predictions = {player.strip(): player2.strip() for player, player2 in (prediction.split(':') for prediction in predictions)}
    elif category == "Least Deaths Overall Predictions":
        least_deaths_overall_predictions = {player.strip(): player2.strip() for player, player2 in (prediction.split(':') for prediction in predictions)}
    elif category == "Best KD Ratio Overall Predictions":
        best_kd_ratio_overall_predictions = {player.strip(): player2.strip() for player, player2 in (prediction.split(':') for prediction in predictions)}
    elif category == "Worst KD Ratio Overall Predictions":
        worst_kd_ratio_overall_predictions = {player.strip(): player2.strip() for player, player2 in (prediction.split(':') for prediction in predictions)}
    elif category == "Most Damage Overall Predictions":
        most_damage_overall_predictions = {player.strip(): player2.strip() for player, player2 in (prediction.split(':') for prediction in predictions)}
    elif category == "Least Damage Overall Predictions":
        least_damage_overall_predictions = {player.strip(): player2.strip() for player, player2 in (prediction.split(':') for prediction in predictions)}




# Combine all dictionaries into one JSON object
predictions_data = {
    "Hardpoint Predictions": hardpoint_predictions,
    "Search and Destroy Predictions": search_and_destroy_predictions,
    "Control Predictions": control_predictions,
    "Most Kills Overall Predictions": most_kills_overall_predictions,
    "Least Kills Overall Predictions": least_kills_overall_predictions,
    "Most Deaths Overall Predictions": most_deaths_overall_predictions,
    "Least Deaths Overall Predictions": least_deaths_overall_predictions,
    "Best KD Ratio Overall Predictions": best_kd_ratio_overall_predictions,
    "Worst KD Ratio Overall Predictions": worst_kd_ratio_overall_predictions,
    "Most Damage Overall Predictions": most_damage_overall_predictions,
    "Least Damage Overall Predictions": least_damage_overall_predictions
}

# Write the JSON object to a file
with open('C:\\Users\\joela\\Desktop\\CDLGame\\data\\predictions.json', 'w') as json_file:
    json.dump(predictions_data, json_file, indent=4)
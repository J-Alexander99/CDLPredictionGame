import os
import re
def read_data(filename):
    with open(filename, 'r') as file:
        return file.readlines()
    
def parse_tables(data, attribute='kills'):
    tables = {}
    current_table = None
    for line in data:
        line = line.strip()
        if line.startswith('Table'):
            current_table = line
            tables[current_table] = []
        elif line:
            if line.startswith("Player Name"):
                player_name = line.split(":")[1].strip()
            elif "'" in line:
                player_data = line.split(":")[1].strip()
                if attribute == 'kills':
                    value = int(player_data.split(",")[0].strip(" '[]"))  # Parse kills
                elif attribute == 'deaths':
                    value = int(player_data.split(",")[1].strip(" '[]"))  # Parse deaths
                elif attribute == 'kd':
                    value = float(player_data.split(",")[2].strip(" '[]"))  # Parse KD ratio
                elif attribute == 'damage':
                    cutoff = int(player_data.split(",")[4].strip(" '[]"))
                    # Concatenate 5th and 6th elements and parse as int for damage
                    if cutoff > 20:
                        damage_str = player_data.split(",")[4].strip(" '[]") #asim fix
                        print(f" {player_name} with {damage_str} damage")  
                    else:
                        damage_str = player_data.split(",")[4].strip(" '[]") + player_data.split(",")[5].strip(" '[]")
                    value = int(damage_str)
                tables[current_table].append((player_name, value))  # Append player and attribute
    return tables

def find_most(tables, attribute):
    most = {}
    for table_name, players in tables.items():
        max_value = max(players, key=lambda x: x[1])
        most[table_name] = max_value
    return most

def find_least(tables, attribute):
    least = {}
    for table_name, players in tables.items():
        min_value = min(players, key=lambda x: x[1])
        least[table_name] = min_value
    return least

def main():
    filename = "C:\\Users\\joela\\Desktop\\CDLGame\\data\\scraped_data.txt"
    tables_data = read_data(filename)
    
       # Parse for kills, deaths, KD ratio, and damage separately
    tables_kills = parse_tables(tables_data, attribute='kills')
    tables_deaths = parse_tables(tables_data, attribute='deaths')
    tables_kd = parse_tables(tables_data, attribute='kd')
    tables_damage = parse_tables(tables_data, attribute='damage')
    
    # Find players with most and least kills
    most_kills = find_most(tables_kills, attribute='kills')
    least_kills = find_least(tables_kills, attribute='kills')
    
    # Find players with most and least deaths
    most_deaths = find_most(tables_deaths, attribute='deaths')
    least_deaths = find_least(tables_deaths, attribute='deaths')
    
    # Find players with most and least KD ratio
    most_kd = find_most(tables_kd, attribute='kd')
    least_kd = find_least(tables_kd, attribute='kd')
    
    # Find players with most and least damage
    most_damage = find_most(tables_damage, attribute='damage')
    least_damage = find_least(tables_damage, attribute='damage')
    
    print("Player with the most kills in each table:")
    for table_name, (player_name, kills) in most_kills.items():
        print(f"{table_name} {player_name} with {kills} kills")
    
    print("\nPlayer with the least kills in each table:")
    for table_name, (player_name, kills) in least_kills.items():
        print(f"{table_name} {player_name} with {kills} kills")
    
    print("\nPlayer with the most deaths in each table:")
    for table_name, (player_name, deaths) in most_deaths.items():
        print(f"{table_name} {player_name} with {deaths} deaths")

    print("\nPlayer with the least deaths in each table:")
    for table_name, (player_name, deaths) in least_deaths.items():
        print(f"{table_name} {player_name} with {deaths} deaths")
    
    print("\nPlayer with the highest KD ratio in each table:")
    for table_name, (player_name, kd) in most_kd.items():
        print(f"{table_name} {player_name} with {kd:.2f} KD ratio")
    
    print("\nPlayer with the lowest KD ratio in each table:")
    for table_name, (player_name, kd) in least_kd.items():
        print(f"{table_name} {player_name} with {kd:.2f} KD ratio")
    
    print("\nPlayer with the most damage in each table:")
    for table_name, (player_name, damage) in most_damage.items():
        print(f"{table_name} {player_name} with {damage} damage")
    
    print("\nPlayer with the least damage in each table:")
    for table_name, (player_name, damage) in least_damage.items():
        print(f"{table_name} {player_name} with {damage} damage")

     # Read predictions
    filename_predictions = "C:\\Users\\joela\\Desktop\\CDLGame\\data\\predictions.txt"
    with open(filename_predictions, 'r') as predictions_file:
        predictions_lines = predictions_file.readlines()

  # Initialize variables for predictor scores
    predictor_scores = {}
    predicting = False
    for line in predictions_lines:
        if line.strip() == "Most Kills Overall Predictions:":
            predicting = True  # Start recording predictor scores
        elif predicting and ':' in line:
            predictor_name = line.split(':')[0].strip()
            predictor_scores[predictor_name] = 0  # Initialize score to 0 for each predictor
        elif predicting and not line.strip():  # Stop recording predictor scores if an empty line is encountered
            predicting = False

    # Print out the initialized predictor scores
    print("Initialized predictor scores:")
    for predictor, score in predictor_scores.items():
        print(f"{predictor}: {score}")

    # Find the first predictor in the list
    first_predictor = list(predictor_scores.keys())[0]

    # Search for the Most Kills Overall Predictions section and print data for each predictor
    predicting = False
    for line in predictions_lines:
        if line.strip() == "Most Kills Overall Predictions:":
            predicting = True
        elif line.strip() == "Least Kills Overall Predictions:":
            predicting = False  # Stop reading lines after reaching the next section
        elif predicting:
            for predictor, score in predictor_scores.items():
                if predictor in line:
                    data = line.split(':')[1].strip()
                    print(f"Data for {predictor}: {data}")
                    # Compare predictor guess to result and update score if they match
                    for table_name, (player_name, kills) in most_kills.items():
                        if data == player_name:
                            predictor_scores[predictor] += 1  # Update the predictor's score
                    break  # Stop after finding the predictor's data

    # Print out updated predictor scores
    print("\nUpdated predictor scores after Most Kills Predictions:")
    for predictor, score in predictor_scores.items():
        print(f"{predictor}: {score}")
    print("\n")    


    # Search for the Least Kills Overall Predictions section and print data for each predictor
    predicting = False
    for line in predictions_lines:
        if line.strip() == "Least Kills Overall Predictions:":
            predicting = True
        elif line.strip() == "Most Deaths Overall Predictions:":
            predicting = False  # Stop reading lines after reaching the next section
        elif predicting:
            for predictor, score in predictor_scores.items():
                if predictor in line:
                    data = line.split(':')[1].strip()
                    print(f"Data for {predictor}: {data}")
                    # Compare predictor guess to result and update score if they match
                    for table_name, (player_name, kills) in least_kills.items():
                        if data == player_name:
                            predictor_scores[predictor] += 1  # Update the predictor's score
                    break  # Stop after finding the predictor's data

    # Print out updated predictor scores
    print("\nUpdated predictor scores after Least Kills Predictions:")
    for predictor, score in predictor_scores.items():
        print(f"{predictor}: {score}")
    print("\n")    

    
        # Search for the Most Deaths Overall Predictions section and print data for each predictor
    predicting = False
    for line in predictions_lines:
        if line.strip() == "Most Deaths Overall Predictions:":
            predicting = True
        elif line.strip() == "Least Deaths Overall Predictions:":
            predicting = False  # Stop reading lines after reaching the next section
        elif predicting:
            for predictor, score in predictor_scores.items():
                if predictor in line:
                    data = line.split(':')[1].strip()
                    print(f"Data for {predictor}: {data}")
                    # Compare predictor guess to result and update score if they match
                    for table_name, (player_name, kills) in most_deaths.items():
                        if data == player_name:
                            predictor_scores[predictor] += 1  # Update the predictor's score
                    break  # Stop after finding the predictor's data

    # Print out updated predictor scores
    print("\nUpdated predictor scores after Most Deaths Predictions:")
    for predictor, score in predictor_scores.items():
        print(f"{predictor}: {score}")
    print("\n")    

        

        # Search for the Least Deaths Overall Predictions section and print data for each predictor
    predicting = False
    for line in predictions_lines:
        if line.strip() == "Least Deaths Overall Predictions:":
            predicting = True
        elif line.strip() == "Best KD Ratio Overall Predictions:":
            predicting = False  # Stop reading lines after reaching the next section
        elif predicting:
            for predictor, score in predictor_scores.items():
                if predictor in line:
                    data = line.split(':')[1].strip()
                    print(f"Data for {predictor}: {data}")
                    # Compare predictor guess to result and update score if they match
                    for table_name, (player_name, kills) in least_deaths.items():
                        if data == player_name:
                            predictor_scores[predictor] += 1  # Update the predictor's score
                    break  # Stop after finding the predictor's data

    # Print out updated predictor scores
    print("\nUpdated predictor scores after Least Deaths Predictions:")
    for predictor, score in predictor_scores.items():
        print(f"{predictor}: {score}")
    print("\n")    

        
        
        # Search for the Best KD Ratio Overall Predictions section and print data for each predictor
    predicting = False
    for line in predictions_lines:
        if line.strip() == "Best KD Ratio Overall Predictions:":
            predicting = True
        elif line.strip() == "Worst KD Ratio Overall Predictions:":
            predicting = False  # Stop reading lines after reaching the next section
        elif predicting:
            for predictor, score in predictor_scores.items():
                if predictor in line:
                    data = line.split(':')[1].strip()
                    print(f"Data for {predictor}: {data}")
                    # Compare predictor guess to result and update score if they match
                    for table_name, (player_name, kills) in most_kd.items():
                        if data == player_name:
                            predictor_scores[predictor] += 1  # Update the predictor's score
                    break  # Stop after finding the predictor's data

    # Print out updated predictor scores
    print("\nUpdated predictor scores after Best KD Ratio Predictions:")
    for predictor, score in predictor_scores.items():
        print(f"{predictor}: {score}")
    print("\n")    

        
        # Search for the Worst KD Ratio Overall Predictions section and print data for each predictor
    predicting = False
    for line in predictions_lines:
        if line.strip() == "Worst KD Ratio Overall Predictions:":
            predicting = True
        elif line.strip() == "Most Damage Overall Predictions:":
            predicting = False  # Stop reading lines after reaching the next section
        elif predicting:
            for predictor, score in predictor_scores.items():
                if predictor in line:
                    data = line.split(':')[1].strip()
                    print(f"Data for {predictor}: {data}")
                    # Compare predictor guess to result and update score if they match
                    for table_name, (player_name, kills) in least_kd.items():
                        if data == player_name:
                            predictor_scores[predictor] += 1  # Update the predictor's score
                    break  # Stop after finding the predictor's data

    # Print out updated predictor scores
    print("\nUpdated predictor scores after Worst KD Ratio Predictions:")
    for predictor, score in predictor_scores.items():
        print(f"{predictor}: {score}")
    print("\n")    

        
        
        # Search for the Most Damage Overall Predictions section and print data for each predictor
    predicting = False
    for line in predictions_lines:
        if line.strip() == "Most Damage Overall Predictions:":
            predicting = True
        elif line.strip() == "Least Damage Overall Predictions:":
            predicting = False  # Stop reading lines after reaching the next section
        elif predicting:
            for predictor, score in predictor_scores.items():
                if predictor in line:
                    data = line.split(':')[1].strip()
                    print(f"Data for {predictor}: {data}")
                    # Compare predictor guess to result and update score if they match
                    for table_name, (player_name, kills) in most_damage.items():
                        if data == player_name:
                            predictor_scores[predictor] += 1  # Update the predictor's score
                    break  # Stop after finding the predictor's data

    # Print out updated predictor scores
    print("\nUpdated predictor scores after Most Damage Predictions:")
    for predictor, score in predictor_scores.items():
        print(f"{predictor}: {score}")
    print("\n")    

        
        
        # Search for the Least Damage Overall Predictions section and print data for each predictor
    predicting = False
    for line in predictions_lines:
        if line.strip() == "Least Damage Overall Predictions:":
            predicting = True
        elif line.strip() == "":
            predicting = False  # Stop reading lines after reaching the next section
        elif predicting:
            for predictor, score in predictor_scores.items():
                if predictor in line:
                    data = line.split(':')[1].strip()
                    print(f"Data for {predictor}: {data}")
                    # Compare predictor guess to result and update score if they match
                    for table_name, (player_name, kills) in least_damage.items():
                        if data == player_name:
                            predictor_scores[predictor] += 1  # Update the predictor's score
                    break  # Stop after finding the predictor's data

    # Print out updated predictor scores
    print("\nUpdated predictor scores after Least Damage Predictions:")
    for predictor, score in predictor_scores.items():
        print(f"{predictor}: {score}")
    print("\n")    

        
 #SCORE CALCULATIONS ------------------------------------------------------------
     # Read scraped_scoreline.txt
    filename_scoreline = "C:\\Users\\joela\\Desktop\\CDLGame\\data\\scraped_scorelines.txt"
    with open(filename_scoreline, 'r') as scoreline_file:
        scoreline_data = scoreline_file.readlines()       
        
     #Search for the team A Hardpoint Scoreline
    predicting = False
    for line in predictions_lines:
        if line.strip() == "Hardpoint Predictions:":
            predicting = True
        elif line.strip() == "Search and Destroy Predictions:":
            predicting = False  # Stop reading lines after reaching the next section
        elif predicting:
            for predictor, score in predictor_scores.items():
                if predictor in line:
                    temp = line.split(':')[1].strip()
                    data = temp.split('-')[0].strip()
                    print(f"Data for {predictor}: {data}")
                    # Compare predictor guess to result and update score if they match
                    predicting2 = False
                    for line in scoreline_data:
                        if line.strip() == "Hardpoint:":
                            predicting2 = True
                        elif line.strip() == "SnD:":
                            predicting2 = False  # Stop reading lines after reaching the next section
                        elif predicting2:
                            resultData = line.split('-')[0].strip()
                            print(f"Hardpoint Score: {resultData}")
                            realdata = int(data)
                            realResultData = int(resultData)
                            if resultData == 250:
                                if realdata == realResultData:
                                    predictor_scores[predictor] += 1  # Update the predictor's score
                            else:
                                if abs(realdata - realResultData) <= 10:
                                    predictor_scores[predictor] += 1  # Update the predictor's score

                            
                            
                                    
    print("\nUpdated predictor scores after Hardpoint Part 1:")
    for predictor, score in predictor_scores.items():
        print(f"{predictor}: {score}") 
    print("\n")    
   
        
     #Search for the team B Hardpoint Scoreline
    predicting = False
    for line in predictions_lines:
        if line.strip() == "Hardpoint Predictions:":
            predicting = True
        elif line.strip() == "Search and Destroy Predictions:":
            predicting = False  # Stop reading lines after reaching the next section
        elif predicting:
            for predictor, score in predictor_scores.items():
                if predictor in line:
                    temp = line.split(':')[1].strip()
                    data = temp.split('-')[1].strip()
                    print(f"Data for {predictor}: {data}")
                    # Compare predictor guess to result and update score if they match
                    predicting2 = False
                    for line in scoreline_data:
                        if line.strip() == "Hardpoint:":
                            predicting2 = True
                        elif line.strip() == "SnD:":
                            predicting2 = False  # Stop reading lines after reaching the next section
                        elif predicting2:
                            resultData = line.split('-')[1].strip()
                            print(f"Hardpoint Score: {resultData}")
                            realdata = int(data)
                            realResultData = int(resultData)
                            if resultData == 250:
                                if realdata == realResultData:
                                    predictor_scores[predictor] += 1  # Update the predictor's score
                            else:
                                if abs(realdata - realResultData) <= 10:
                                    predictor_scores[predictor] += 1  # Update the predictor's score

                            
                            
    # Compare predictor guess to result and update score if they match
    print("\nUpdated predictor scores after Hardpoint Part 2:")
    for predictor, score in predictor_scores.items():
        print(f"{predictor}: {score}")
    print("\n")    
    

     #Search for the team A Search and Destroy Scoreline
    predicting = False
    for line in predictions_lines:
        if line.strip() == "Search and Destroy Predictions:":
            predicting = True
        elif line.strip() == "Control Predictions:":
            predicting = False  # Stop reading lines after reaching the next section
        elif predicting:
            for predictor, score in predictor_scores.items():
                if predictor in line:
                    temp = line.split(':')[1].strip()
                    data = temp.split('-')[0].strip()
                    print(f"Data for {predictor}: {data}")
                    # Compare predictor guess to result and update score if they match
                    predicting2 = False
                    for line in scoreline_data:
                        if line.strip() == "SnD:":
                            predicting2 = True
                        elif line.strip() == "Control:":
                            predicting2 = False  # Stop reading lines after reaching the next section
                        elif predicting2:
                            resultData = line.split('-')[0].strip()
                            print(f"Search and Destroy Score: {resultData}")
                            if data == resultData:
                                predictor_scores[predictor] += 1  # Update the predictor's score
                            
                            
                                    # Compare predictor guess to result and update score if they match
    print("\nUpdated predictor scores after SnD Part 1:")
    for predictor, score in predictor_scores.items():
        print(f"{predictor}: {score}")
    print("\n")    
    
        
     #Search for the team B Search and Destroy Scoreline
    predicting = False
    for line in predictions_lines:
        if line.strip() == "Search and Destroy Predictions:":
            predicting = True
        elif line.strip() == "Control Predictions:":
            predicting = False  # Stop reading lines after reaching the next section
        elif predicting:
            for predictor, score in predictor_scores.items():
                if predictor in line:
                    temp = line.split(':')[1].strip()
                    data = temp.split('-')[1].strip()
                    print(f"Data for {predictor}: {data}")
                    # Compare predictor guess to result and update score if they match
                    predicting2 = False
                    for line in scoreline_data:
                        if line.strip() == "SnD:":
                            predicting2 = True
                        elif line.strip() == "Control:":
                            predicting2 = False  # Stop reading lines after reaching the next section
                        elif predicting2:
                            resultData = line.split('-')[1].strip()
                            print(f"Search and Destroy Score: {resultData}")
                            if data == resultData:
                                predictor_scores[predictor] += 1  # Update the predictor's score
                            
                            
    # Compare predictor guess to result and update score if they match
    print("\nUpdated predictor scores after SnD Part 2:")
    for predictor, score in predictor_scores.items():
        print(f"{predictor}: {score}") 
    print("\n")    
       

     #Search for the team A Control Scoreline -------------------------------------------------
    predicting = False
    for line in predictions_lines:
        if line.strip() == "Control Predictions:":
            predicting = True
        elif line.strip() == "Most Kills Overall Predictions:":
            predicting = False  # Stop reading lines after reaching the next section
        elif predicting:
            for predictor, score in predictor_scores.items():
                if predictor in line:
                    temp = line.split(':')[1].strip()
                    data = temp.split('-')[0].strip()
                    print(f"Data for {predictor}: {data}")
                    # Compare predictor guess to result and update score if they match
                    predicting2 = False
                    for line in scoreline_data:
                        if line.strip() == "Control:":
                            predicting2 = True
                        elif line.strip() == "":
                            predicting2 = False  # Stop reading lines after reaching the next section
                        elif predicting2:
                            resultData = line.split('-')[0].strip()
                            print(f"Control Score: {resultData}")
                            if data == resultData:
                                predictor_scores[predictor] += 1  # Update the predictor's score
                            
                            
                                    # Compare predictor guess to result and update score if they match
    print("\nUpdated predictor scores after Control Part 1:")
    for predictor, score in predictor_scores.items():
        print(f"{predictor}: {score}")    
    print("\n")    
     #Search for the team B Control Scoreline
    predicting = False
    for line in predictions_lines:
        if line.strip() == "Control Predictions:":
            predicting = True
        elif line.strip() == "Most Kills Overall Predictions:":
            predicting = False  # Stop reading lines after reaching the next section
        elif predicting:
            for predictor, score in predictor_scores.items():
                if predictor in line:
                    temp = line.split(':')[1].strip()
                    data = temp.split('-')[1].strip()
                    print(f"Data for {predictor}: {data}")
                    # Compare predictor guess to result and update score if they match
                    predicting2 = False
                    for line in scoreline_data:
                        if line.strip() == "Control:":
                            predicting2 = True
                        elif line.strip() == "":
                            predicting2 = False  # Stop reading lines after reaching the next section
                        elif predicting2:
                            resultData = line.split('-')[1].strip()
                            print(f"Control Score: {resultData}")
                            if data == resultData:
                                predictor_scores[predictor] += 1  # Update the predictor's score
                            
                            
    # Compare predictor guess to result and update score if they match
    print("\nFinal Scores:")
    for predictor, score in predictor_scores.items():
        print(f"{predictor}: {score}")         
        
        
if __name__ == "__main__":
    main()
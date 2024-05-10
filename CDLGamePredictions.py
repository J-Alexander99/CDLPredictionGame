# MAD = resume at line 485


import tkinter as tk
from tkinter import simpledialog, OptionMenu, messagebox
import random

class Player:
    def __init__(self, name):
        self.name = name

team_a_var = None
team_b_var = None
players = {} #name of the users
player_ids = []
team_rosters = {
    "FaZe": ["Simp", "aBeZy", "Cellium", "Drazah"],
    "Ultra": ["Scrap", "Envoy", "Insight", "CleanX"],
    "Breach": ["Beans", "Priestahh", "Pentagrxm", "Snoopy"],
    "Ravens": ["Clayster", "FelonY", "Gwinn", "TJHaLy"],
    "Guerrillas": ["Flames", "Diamondcon", "Estreal", "Fame"],
    "Thieves": ["JoeDeceives", "Ghosty", "Kremp", "Nastie"],
    "Surge": ["Abuzah", "04", "Breszy", "Huke"],
    "Optic": ["Dashy", "Kenny", "Pred", "Shotzzy"],
    "Legion": ["Attach", "Gio", "Nero", "Johnny"],
    "Heretics": ["ReeaL", "Lucky", "MettalZ", "Vikul"],
    "Rokkr": ["Accuracy", "Lyynnz", "Standy", "Gunless"],
    "Subliners": ["HyDra", "KiSMET", "Sib", "Skyz"]
}

hardpoint_predictions = {}
search_and_destroy_predictions = {}
control_predictions = {}
most_kills_team_predictions = {}
most_kills_overall_predictions = {}
least_kills_team_predictions = {}
least_kills_overall_predictions = {}
most_deaths_team_predictions = {}
most_deaths_overall_predictions = {}
least_deaths_team_predictions = {}
least_deaths_overall_predictions = {}
best_kd_team_predictions = {}
best_kd_overall_predictions = {}
worst_kd_team_predictions = {}
worst_kd_overall_predictions = {}
most_dmg_team_predictions = {}
most_dmg_overall_predictions = {}
least_dmg_team_predictions = {}
least_dmg_overall_predictions = {}
most_kills_team_a_predictions = {}
most_kills_team_b_predictions = {}
least_kills_team_a_predictions = {}
least_kills_team_b_predictions = {}
most_deaths_team_a_predictions = {}
most_deaths_team_b_predictions = {}
least_deaths_team_a_predictions = {}
least_deaths_team_b_predictions = {}
best_kd_team_a_predictions = {}
best_kd_team_b_predictions = {}
worst_kd_team_a_predictions = {}
worst_kd_team_b_predictions = {}
most_dmg_team_a_predictions = {}
most_dmg_team_b_predictions = {}
least_dmg_team_a_predictions = {}
least_dmg_team_b_predictions = {}


def misc():
    global colour_fore, colour_back, colour_Puple, colour_black, app_Width, app_Height, custom_height_over, bg_colour_main

    colour_fore = '#C1C2C5'
    colour_back = '#1A1B1E'
    colour_Puple = '#7b38ab'
    colour_black = '#000000'

    app_Width = 700
    app_Height = 250

     # need custom height for some 
    custom_height_over = 400

    bg_colour_main = '#1A1B1E'






def get_players():
    global players, player_ids
    num_players = simpledialog.askinteger("Number of Players", "Enter the number of players:")
    players.clear()
    player_ids.clear()
    for i in range(num_players):
        name = simpledialog.askstring("Player Name", f"Enter name for Player {i+1}:")
        player = Player(name)
        players[i+1] = player
        player_ids.append(i+1)
    show_game_settings()

def show_game_settings():
    def begin_game():
        selected_team_a = team_a_var.get()
        selected_team_b = team_b_var.get()
        messagebox.showinfo("Game Begins", f"Game begins! Team A: {selected_team_a}, Team B: {selected_team_b}")
        game_settings_window.destroy()  # Close the game settings window
        spin_wheel()

    global game_settings_window
     # This is for all the tkinker forms ------
    game_settings_window = tk.Toplevel(app)
    game_settings_window.config(bg= bg_colour_main)
    game_settings_window.minsize(app_Width, custom_height_over)
    screen_Width = app.winfo_screenwidth()
    screen_Height = app.winfo_screenheight()
    x = (screen_Width / 2) - (app_Width / 2)
    y = (screen_Height / 1.5) - (app_Height / 2)
    game_settings_window.geometry(f'{app_Width}x{app_Height}+{int(x)}+{int(y)}')
    # -----------------------------------------------------------

    teams = ["FaZe", "Ultra", "Breach", "Ravens", "Guerrillas", "Thieves", "Surge", "Optic", "Legion", "Heretics", "Rokkr", "Subliners"]

    team_a_label = tk.Label(game_settings_window, 
                            text="Select Team A:", 
                            width="20", 
                            height="2", 
                            font="8",
                            background=colour_fore,
                            foreground=colour_black,
                            activebackground=colour_Puple,
                            activeforeground=colour_Puple,
                            highlightthickness=2,
                            highlightbackground=colour_Puple,
                            highlightcolor='WHITE',
                            border=10,
                            cursor='hand2')
    team_a_label.pack(pady=10)
    global team_a_var
    team_a_var = tk.StringVar(game_settings_window)
    team_a_var.set(teams[0])
    team_a_dropdown = OptionMenu(game_settings_window, team_a_var, *teams,)
    team_a_dropdown_submenu = game_settings_window.nametowidget(team_a_dropdown.menuname)
    team_a_dropdown.config(font=[15])
    team_a_dropdown_submenu.config(font=[30])
    team_a_dropdown.pack(pady=10)

    team_b_label = tk.Label(game_settings_window, 
                            text="Select Team B:", 
                            width="20", 
                            height="2", 
                            font="8",
                            background=colour_fore,
                            foreground=colour_black,
                            activebackground=colour_Puple,
                            activeforeground=colour_Puple,
                            highlightthickness=2,
                            highlightbackground=colour_Puple,
                            highlightcolor='WHITE',
                            border=10,
                            cursor='hand2')
    team_b_label.pack(pady=10)
    global team_b_var
    team_b_var = tk.StringVar(game_settings_window)
    team_b_var.set(teams[1])
    team_b_dropdown = OptionMenu(game_settings_window, team_b_var, *teams)
    team_b_dropdown_submenu = game_settings_window.nametowidget(team_b_dropdown.menuname)
    team_b_dropdown.config(font=[15])
    team_b_dropdown_submenu.config(font=[30])
    team_b_dropdown.pack(pady=10)

    begin_game_button = tk.Button(game_settings_window, 
                                  text="Begin Game", 
                                  command=begin_game, 
                                  width="20", 
                                  height="2", 
                                  font="20",
                                  background=colour_Puple,
                                  foreground=colour_black,
                                  activebackground=colour_Puple,
                                  activeforeground=colour_Puple,
                                  highlightthickness=2,
                                  highlightbackground=colour_Puple,
                                  highlightcolor='WHITE',
                                  border=10,
                                  cursor='hand2')
    begin_game_button.pack(pady=10)

def spin_wheel():
    if players:
        random.shuffle(player_ids)
        show_hardpoint_prediction()

def show_hardpoint_prediction():
    player_id = player_ids.pop(0)
    selected_player = players[player_id]

  
    hardpoint_window = tk.Toplevel()
    hardpoint_window.title("Hardpoint Prediction")
    hardpoint_window.config(bg= bg_colour_main)
    # This is for all the tkinker forms ------
    hardpoint_window.minsize(app_Width, custom_height_over)
    screen_Width = app.winfo_screenwidth()
    screen_Height = app.winfo_screenheight()
    x = (screen_Width / 2) - (app_Width / 2)
    y = (screen_Height / 1.5) - (app_Height / 2)
    hardpoint_window.geometry(f'{app_Width}x{app_Height}+{int(x)}+{int(y)}')
    # -----------------------------------------------------------

    selected_player_label = tk.Label(hardpoint_window, text=f"{selected_player.name}, Please enter your prediction for the Hardpoint Result:",
                                     width="60", 
                                     height="3", 
                                     font="8",
                                     background=colour_fore,
                                     foreground=colour_black,
                                     activebackground=colour_Puple,
                                     activeforeground=colour_Puple,
                                     highlightthickness=2,
                                     highlightbackground=colour_Puple,
                                     highlightcolor='WHITE',
                                     border=10,)
    selected_player_label.pack(pady=10)

    team_a_label = tk.Label(hardpoint_window, text=f"{team_a_var.get()}", 
                            width="30",
                            font="5", 
                            background=colour_fore,
                            foreground=colour_black,
                            activebackground=colour_Puple,
                            activeforeground=colour_Puple,
                            highlightthickness=2,
                            highlightbackground=colour_Puple,
                            highlightcolor='WHITE',
                            border=10,)
    team_a_label.pack(pady=5)
    team_a_entry = tk.Entry(hardpoint_window)
    team_a_entry.pack(pady=20)

    team_b_label = tk.Label(hardpoint_window, text=f"{team_b_var.get()}",
                            width="30",
                            font="5", 
                            background=colour_fore,
                            foreground=colour_black,
                            activebackground=colour_Puple,
                            activeforeground=colour_Puple,
                            highlightthickness=2,
                            highlightbackground=colour_Puple,
                            highlightcolor='WHITE',
                            border=10,                          )
    team_b_label.pack(pady=5)
    team_b_entry = tk.Entry(hardpoint_window)
    team_b_entry.pack(pady=20)

    def save_prediction():
        team_a_prediction = team_a_entry.get()
        team_b_prediction = team_b_entry.get()
        prediction = f"{team_a_prediction}-{team_b_prediction}"
        messagebox.showinfo("Prediction Saved", f"Prediction saved! Prediction: {prediction}")
        hardpoint_predictions[selected_player.name] = prediction
        hardpoint_window.destroy()  # Close the current hardpoint window
        if player_ids:
            spin_wheel()  # Spin the wheel for the next player
        else:
            print_hardpoint_predictions()
            reset_player_ids()  # Reset player IDs for Search and Destroy predictions
            spin_wheel_snd()  # Proceed to Search and Destroy predictions

    save_button = tk.Button(hardpoint_window, text="Decision Made", command=save_prediction,
                            width="20", 
                            height="2", 
                            font="15",
                            background=colour_Puple,
                            foreground=colour_black,
                            activebackground=colour_Puple,
                            activeforeground=colour_Puple,
                            highlightthickness=2,
                            highlightbackground=colour_Puple,
                            highlightcolor='WHITE',
                            border=5,
                            cursor='hand2')
    save_button.pack(pady=5)

def reset_player_ids():
    global player_ids
    player_ids = list(players.keys())  # Reset player IDs to contain all player IDs

def spin_wheel_snd():
    if players:
        random.shuffle(player_ids)
        show_search_and_destroy_prediction()

def show_search_and_destroy_prediction():
    player_id = player_ids.pop(0)
    selected_player = players[player_id]

    sad_window = tk.Toplevel(app)
    sad_window.title("Search and Destroy Prediction")
    sad_window.config(bg= bg_colour_main)
    #This is for all the tkinker forms ------
    sad_window.minsize(app_Width, custom_height_over)
    screen_Width = app.winfo_screenwidth()
    screen_Height = app.winfo_screenheight()
    x = (screen_Width / 2) - (app_Width / 2)
    y = (screen_Height / 1.5) - (app_Height / 2)
    sad_window.geometry(f'{app_Width}x{app_Height}+{int(x)}+{int(y)}')
    # -----------------------------------------------------------

    selected_player_label = tk.Label(sad_window, text=f"{selected_player.name}, Please enter your prediction for the Search and Destroy Result:",
                                    width="60", 
                                     height="3", 
                                     font="8",
                                     background=colour_fore,
                                     foreground=colour_black,
                                     activebackground=colour_Puple,
                                     activeforeground=colour_Puple,
                                     highlightthickness=2,
                                     highlightbackground=colour_Puple,
                                     highlightcolor='WHITE',
                                     border=10,)
    selected_player_label.pack(pady=10)

    team_a_label = tk.Label(sad_window, text=f"Team A: {team_a_var.get()}",
                            width="30",
                            font="5", 
                            background=colour_fore,
                            foreground=colour_black,
                            activebackground=colour_Puple,
                            activeforeground=colour_Puple,
                            highlightthickness=2,
                            highlightbackground=colour_Puple,
                            highlightcolor='WHITE',
                            border=10,)
    team_a_label.pack(pady=5)
    team_a_entry = tk.Entry(sad_window)
    team_a_entry.pack(pady=20)

    team_b_label = tk.Label(sad_window, text=f"Team B: {team_b_var.get()}",
                            width="30",
                            font="5", 
                            background=colour_fore,
                            foreground=colour_black,
                            activebackground=colour_Puple,
                            activeforeground=colour_Puple,
                            highlightthickness=2,
                            highlightbackground=colour_Puple,
                            highlightcolor='WHITE',
                            border=10,)
    team_b_label.pack(pady=5)
    team_b_entry = tk.Entry(sad_window)
    team_b_entry.pack(pady=20)

    def save_prediction():
        team_a_prediction = team_a_entry.get()
        team_b_prediction = team_b_entry.get()
        prediction = f"{team_a_prediction}-{team_b_prediction}"
        messagebox.showinfo("Prediction Saved", f"Prediction saved! Prediction: {prediction}")
        search_and_destroy_predictions[selected_player.name] = prediction
        sad_window.destroy()  # Close the current Search and Destroy window
        if player_ids:
            spin_wheel_snd()  # Spin the wheel for the next player
        else:
            print_search_and_destroy_predictions()
            reset_player_ids()  # Reset player IDs for Control predictions
            spin_wheel_control()  # Proceed to Control predictions

    decision_made_button = tk.Button(sad_window, text="Decision Made", command=save_prediction,
                                     width="20", 
                                     height="2", 
                                     font="15",
                                     background=colour_Puple,
                                     foreground=colour_black,
                                     activebackground=colour_Puple,
                                     activeforeground=colour_Puple,
                                     highlightthickness=2,
                                     highlightbackground=colour_Puple,
                                     highlightcolor='WHITE',
                                     border=5,
                                     cursor='hand2')
    decision_made_button.pack(pady=5)

def spin_wheel_control():
    if players:
        random.shuffle(player_ids)
        show_control_prediction()

def show_control_prediction():
    player_id = player_ids.pop(0)
    selected_player = players[player_id]

    control_window = tk.Toplevel(app)
    control_window.title("Control Prediction")
    control_window.config(bg= bg_colour_main)
     # This is for all the tkinker forms ------
    control_window.minsize(app_Width, custom_height_over)
    screen_Width = app.winfo_screenwidth()
    screen_Height = app.winfo_screenheight()
    x = (screen_Width / 2) - (app_Width / 2)
    y = (screen_Height / 1.5) - (app_Height / 2)
    control_window.geometry(f'{app_Width}x{app_Height}+{int(x)}+{int(y)}')
    # -----------------------------------------------------------

    selected_player_label = tk.Label(control_window, text=f"{selected_player.name}, Please enter your prediction for the Control Result:",
                                     width="60", 
                                     height="3", 
                                     font="8",
                                     background=colour_fore,
                                     foreground=colour_black,
                                     activebackground=colour_Puple,
                                     activeforeground=colour_Puple,
                                     highlightthickness=2,
                                     highlightbackground=colour_Puple,
                                     highlightcolor='WHITE',
                                     border=10,)
    selected_player_label.pack(pady=10)

    team_a_label = tk.Label(control_window, text=f"Team A: {team_a_var.get()}",
                            width="30",
                            font="5", 
                            background=colour_fore,
                            foreground=colour_black,
                            activebackground=colour_Puple,
                            activeforeground=colour_Puple,
                            highlightthickness=2,
                            highlightbackground=colour_Puple,
                            highlightcolor='WHITE',
                            border=10,)
    team_a_label.pack(pady=5)
    team_a_entry = tk.Entry(control_window)
    team_a_entry.pack(pady=20)

    team_b_label = tk.Label(control_window, text=f"Team B: {team_b_var.get()}",
                            width="30",
                            font="5", 
                            background=colour_fore,
                            foreground=colour_black,
                            activebackground=colour_Puple,
                            activeforeground=colour_Puple,
                            highlightthickness=2,
                            highlightbackground=colour_Puple,
                            highlightcolor='WHITE',
                            border=10,)
    team_b_label.pack(pady=5)
    team_b_entry = tk.Entry(control_window)
    team_b_entry.pack(pady=20)

    def save_prediction():
        team_a_prediction = team_a_entry.get()
        team_b_prediction = team_b_entry.get()
        prediction = f"{team_a_prediction}-{team_b_prediction}"
        messagebox.showinfo("Prediction Saved", f"Prediction saved! Prediction: {prediction}")
        control_predictions[selected_player.name] = prediction
        control_window.destroy()  # Close the current Control window
        if player_ids:
            spin_wheel_control()  # Spin the wheel for the next player
        else:
            print_control_predictions()
            reset_player_ids()  # Reset player IDs for Most Kills predictions
            spin_wheel_most_kills_predictions()

    decision_made_button = tk.Button(control_window, text="Decision Made", command=save_prediction,
                                     width="20", 
                                     height="2", 
                                     font="15",
                                     background=colour_Puple,
                                     foreground=colour_black,
                                     activebackground=colour_Puple,
                                     activeforeground=colour_Puple,
                                     highlightthickness=2,
                                     highlightbackground=colour_Puple,
                                     highlightcolor='WHITE',
                                     border=5,
                                     cursor='hand2')
    decision_made_button.pack(pady=5)
    
    
def spin_wheel_most_kills_predictions():
    if players:
        random.shuffle(player_ids)
        predict_most_kills()

def predict_most_kills():
    player_id = player_ids.pop(0)
    selected_player = players[player_id]

# !!!resume here!!!

    most_kills_window = tk.Toplevel(app)
    most_kills_window.title("Most Kills Prediction")
    most_kills_window.config(bg= bg_colour_main)
     # This is for all the tkinker forms ------
    app.minsize(app_Width, app_Height)
    screen_Width = app.winfo_screenwidth()
    screen_Height = app.winfo_screenheight()
    x = (screen_Width / 2) - (app_Width / 2)
    y = (screen_Height / 1.5) - (app_Height / 2)
    most_kills_window.geometry(f'{app_Width}x{app_Height}+{int(x)}+{int(y)}')
    # -----------------------------------------------------------

    selected_player_label = tk.Label(most_kills_window, text=f"{selected_player.name}, Please select the player you predict to have the most kills:")
    selected_player_label.pack()
    team_a_players = team_rosters[team_a_var.get()]
    team_b_players = team_rosters[team_b_var.get()]
    all_players = team_a_players + team_b_players

    selected_player_var = tk.StringVar(most_kills_window)
    selected_player_var.set(all_players[0])
    selected_player_dropdown = OptionMenu(most_kills_window, selected_player_var, *all_players)
    selected_player_dropdown.pack()

    def save_prediction():
        prediction = selected_player_var.get()
        messagebox.showinfo("Prediction Saved", f"Prediction saved! Selected Player: {prediction}")
        most_kills_overall_predictions[selected_player.name] = prediction
        print(f"{selected_player.name}: {prediction}")  # Print the prediction to console
        most_kills_window.destroy()  # Close the current Most Kills window
        if player_ids:
            predict_most_kills()  # Spin the wheel for the next player
        else:
            print_most_kills_overall_predictions()  # Print overall most kills predictions
            reset_player_ids()  # Reset player IDs for next predictions
            spin_wheel_least_kills_predictions()  # Proceed to other predictions

    decision_made_button = tk.Button(most_kills_window, text="Decision Made", command=save_prediction)
    decision_made_button.pack()

    
def spin_wheel_least_kills_predictions():
    if players:
        random.shuffle(player_ids)
        predict_least_kills()

def predict_least_kills():
    player_id = player_ids.pop(0)
    selected_player = players[player_id]

    least_kills_window = tk.Toplevel(app)
    least_kills_window.title("Least Kills Prediction")
    least_kills_window.config(bg= bg_colour_main)
     # This is for all the tkinker forms ------
    app.minsize(app_Width, app_Height)
    screen_Width = app.winfo_screenwidth()
    screen_Height = app.winfo_screenheight()
    x = (screen_Width / 2) - (app_Width / 2)
    y = (screen_Height / 1.5) - (app_Height / 2)
    least_kills_window.geometry(f'{app_Width}x{app_Height}+{int(x)}+{int(y)}')
    # -----------------------------------------------------------

    selected_player_label = tk.Label(least_kills_window, text=f"{selected_player.name}, Please select the player you predict to have the least kills:")
    selected_player_label.pack()
    team_a_players = team_rosters[team_a_var.get()]
    team_b_players = team_rosters[team_b_var.get()]
    all_players = team_a_players + team_b_players

    selected_player_var = tk.StringVar(least_kills_window)
    selected_player_var.set(all_players[0])
    selected_player_dropdown = OptionMenu(least_kills_window, selected_player_var, *all_players)
    selected_player_dropdown.pack()

    def save_prediction():
        prediction = selected_player_var.get()
        messagebox.showinfo("Prediction Saved", f"Prediction saved! Selected Player: {prediction}")
        least_kills_overall_predictions[selected_player.name] = prediction
        print(f"{selected_player.name}: {prediction}")  # Print the prediction to console
        least_kills_window.destroy()  # Close the current Least Kills window
        if player_ids:
            predict_least_kills()  # Spin the wheel for the next player

        else:
            print_least_kills_overall_predictions()  # Print overall least kills predictions
            reset_player_ids()  # Reset player IDs for next predictions
            spin_wheel_predict_most_deaths_overall()# Proceed to other predictions

    decision_made_button = tk.Button(least_kills_window, text="Decision Made", command=save_prediction)
    decision_made_button.pack()
    
    
def challenge_methods():
    # Define a list of method names (placeholders)
    method_names = [
        "predict_most_kills_team_a",
        "predict_most_kills_team_b",
        "predict_least_kills_team_a",
        "predict_least_kills_team_b",
        "predict_most_deaths_team_a",
        "predict_most_deaths_team_b",
        "predict_most_deaths_overall",
        "predict_least_deaths_team_a",
        "predict_least_deaths_team_b",
        "predict_least_deaths_overall",
        "predict_best_kd_team_a",
        "predict_best_kd_team_b",
        "predict_best_kd_overall",
        "predict_worst_kd_team_a",
        "predict_worst_kd_team_b",
        "predict_worst_kd_overall",
        "predict_most_dmg_team_a",
        "predict_most_dmg_team_b",
        "predict_most_dmg_overall",
        "predict_least_dmg_team_a",
        "predict_least_dmg_team_b",
        "predict_least_dmg_overall"
    ]

    # Shuffle the list of method names
    random.shuffle(method_names)

    # Select one method name randomly
    selected_method = random.choice(method_names)

    # Call the selected method
    globals()[selected_method]()

# Placeholder methods
def predict_most_kills_team_a():
    player_id = player_ids.pop(0)
    selected_player = players[player_id]

    most_kills_team_a_window = tk.Toplevel(app)
    most_kills_team_a_window.title("Most Kills on Team A Prediction")
    most_kills_team_a_window.config(bg= bg_colour_main)
     # This is for all the tkinker forms ------
    app.minsize(app_Width, app_Height)
    screen_Width = app.winfo_screenwidth()
    screen_Height = app.winfo_screenheight()
    x = (screen_Width / 2) - (app_Width / 2)
    y = (screen_Height / 1.5) - (app_Height / 2)
    most_kills_team_a_window.geometry(f'{app_Width}x{app_Height}+{int(x)}+{int(y)}')
    # -----------------------------------------------------------

    selected_player_label = tk.Label(most_kills_team_a_window, text=f"{selected_player.name}, Please select the player you predict to have the most kills on Team A:")
    selected_player_label.pack()
    team_a_players = team_rosters[team_a_var.get()]

    selected_player_var = tk.StringVar(most_kills_team_a_window)
    selected_player_var.set(team_a_players[0])
    selected_player_dropdown = OptionMenu(most_kills_team_a_window, selected_player_var, *team_a_players)
    selected_player_dropdown.pack()

    def save_prediction():
        prediction = selected_player_var.get()
        messagebox.showinfo("Prediction Saved", f"Prediction saved! Selected Player: {prediction}")
        most_kills_team_a_predictions[selected_player.name] = prediction
        print(f"Most Kills on Team A Prediction for {selected_player.name}: {prediction}")  # Print the prediction to console
        most_kills_team_a_window.destroy()  # Close the current window
        if player_ids:
            predict_most_kills_team_a()  # Spin the wheel for the next player
        else:
            #print_most_kills_team_a_predictions()  # Print overall predictions
            print("Resetting...")
            #reset_player_ids()  # Reset player IDs for next predictions
            # Proceed to other predictions

    decision_made_button = tk.Button(most_kills_team_a_window, text="Decision Made", command=save_prediction)
    decision_made_button.pack()

    
def predict_most_kills_team_b():
    player_id = player_ids.pop(0)
    selected_player = players[player_id]

    most_kills_team_b_window = tk.Toplevel(app)
    most_kills_team_b_window.title("Most Kills on Team B Prediction")
    most_kills_team_b_window.config(bg= bg_colour_main)
     # This is for all the tkinker forms ------
    app.minsize(app_Width, app_Height)
    screen_Width = app.winfo_screenwidth()
    screen_Height = app.winfo_screenheight()
    x = (screen_Width / 2) - (app_Width / 2)
    y = (screen_Height / 1.5) - (app_Height / 2)
    most_kills_team_b_window.geometry(f'{app_Width}x{app_Height}+{int(x)}+{int(y)}')
    # -----------------------------------------------------------

    selected_player_label = tk.Label(most_kills_team_b_window, text=f"{selected_player.name}, Please select the player you predict to have the most kills on Team B:")
    selected_player_label.pack()
    team_b_players = team_rosters[team_b_var.get()]

    selected_player_var = tk.StringVar(most_kills_team_b_window)
    selected_player_var.set(team_b_players[0])
    selected_player_dropdown = OptionMenu(most_kills_team_b_window, selected_player_var, *team_b_players)
    selected_player_dropdown.pack()

    def save_prediction():
        prediction = selected_player_var.get()
        messagebox.showinfo("Prediction Saved", f"Prediction saved! Selected Player: {prediction}")
        most_kills_team_b_predictions[selected_player.name] = prediction
        print(f"Most Kills on Team B Prediction for {selected_player.name}: {prediction}")  # Print the prediction to console
        most_kills_team_b_window.destroy()  # Close the current window
        if player_ids:
            predict_most_kills_team_b()  # Spin the wheel for the next player
        else:
            #print_most_kills_team_b_predictions()  # Print overall predictions
            print("Resetting...")
            #reset_player_ids()  # Reset player IDs for next predictions
            # Proceed to other predictions

    decision_made_button = tk.Button(most_kills_team_b_window, text="Decision Made", command=save_prediction)
    decision_made_button.pack()


def predict_least_kills_team_a():
    player_id = player_ids.pop(0)
    selected_player = players[player_id]

    least_kills_team_a_window = tk.Toplevel(app)
    least_kills_team_a_window.title("Least Kills on Team A Prediction")
    least_kills_team_a_window.config(bg= bg_colour_main)
     # This is for all the tkinker forms ------
    app.minsize(app_Width, app_Height)
    screen_Width = app.winfo_screenwidth()
    screen_Height = app.winfo_screenheight()
    x = (screen_Width / 2) - (app_Width / 2)
    y = (screen_Height / 1.5) - (app_Height / 2)
    least_kills_team_a_window.geometry(f'{app_Width}x{app_Height}+{int(x)}+{int(y)}')
    # -----------------------------------------------------------

    selected_player_label = tk.Label(least_kills_team_a_window, text=f"{selected_player.name}, Please select the player you predict to have the least kills on Team A:")
    selected_player_label.pack()
    team_a_players = team_rosters[team_a_var.get()]

    selected_player_var = tk.StringVar(least_kills_team_a_window)
    selected_player_var.set(team_a_players[0])
    selected_player_dropdown = OptionMenu(least_kills_team_a_window, selected_player_var, *team_a_players)
    selected_player_dropdown.pack()

    def save_prediction():
        prediction = selected_player_var.get()
        messagebox.showinfo("Prediction Saved", f"Prediction saved! Selected Player: {prediction}")
        least_kills_team_a_predictions[selected_player.name] = prediction
        print(f"Least Kills on Team A Prediction for {selected_player.name}: {prediction}")  # Print the prediction to console
        least_kills_team_a_window.destroy()  # Close the current window
        if player_ids:
            predict_least_kills_team_a()  # Spin the wheel for the next player
        else:
            #print_least_kills_team_a_predictions()  # Print overall predictions
            print("Resetting...")
            #reset_player_ids()  # Reset player IDs for next predictions
            # Proceed to other predictions

    decision_made_button = tk.Button(least_kills_team_a_window, text="Decision Made", command=save_prediction)
    decision_made_button.pack()

def predict_least_kills_team_b():
    player_id = player_ids.pop(0)
    selected_player = players[player_id]

    least_kills_team_b_window = tk.Toplevel(app)
    least_kills_team_b_window.title("Least Kills on Team B Prediction")
    least_kills_team_b_window.config(bg= bg_colour_main)
     # This is for all the tkinker forms ------
    app.minsize(app_Width, app_Height)
    screen_Width = app.winfo_screenwidth()
    screen_Height = app.winfo_screenheight()
    x = (screen_Width / 2) - (app_Width / 2)
    y = (screen_Height / 1.5) - (app_Height / 2)
    least_kills_team_b_window.geometry(f'{app_Width}x{app_Height}+{int(x)}+{int(y)}')
    # -----------------------------------------------------------

    selected_player_label = tk.Label(least_kills_team_b_window, text=f"{selected_player.name}, Please select the player you predict to have the least kills on Team B:")
    selected_player_label.pack()
    team_b_players = team_rosters[team_b_var.get()]

    selected_player_var = tk.StringVar(least_kills_team_b_window)
    selected_player_var.set(team_b_players[0])
    selected_player_dropdown = OptionMenu(least_kills_team_b_window, selected_player_var, *team_b_players)
    selected_player_dropdown.pack()

    def save_prediction():
        prediction = selected_player_var.get()
        messagebox.showinfo("Prediction Saved", f"Prediction saved! Selected Player: {prediction}")
        least_kills_team_b_predictions[selected_player.name] = prediction
        print(f"Least Kills on Team B Prediction for {selected_player.name}: {prediction}")  # Print the prediction to console
        least_kills_team_b_window.destroy()  # Close the current window
        if player_ids:
            predict_least_kills_team_b()  # Spin the wheel for the next player
        else:
            #print_least_kills_team_b_predictions()  # Print overall predictions
            print("Resetting...")
            #reset_player_ids()  # Reset player IDs for next predictions
            # Proceed to other predictions

    decision_made_button = tk.Button(least_kills_team_b_window, text="Decision Made", command=save_prediction)
    decision_made_button.pack()


def predict_most_deaths_team_a():
    player_id = player_ids.pop(0)
    selected_player = players[player_id]

    most_deaths_team_a_window = tk.Toplevel(app)
    most_deaths_team_a_window.title("Most Deaths on Team A Prediction")
    most_deaths_team_a_window.config(bg= bg_colour_main)
     # This is for all the tkinker forms ------
    app.minsize(app_Width, app_Height)
    screen_Width = app.winfo_screenwidth()
    screen_Height = app.winfo_screenheight()
    x = (screen_Width / 2) - (app_Width / 2)
    y = (screen_Height / 1.5) - (app_Height / 2)
    most_deaths_team_a_window.geometry(f'{app_Width}x{app_Height}+{int(x)}+{int(y)}')
    # -----------------------------------------------------------

    selected_player_label = tk.Label(most_deaths_team_a_window, text=f"{selected_player.name}, Please select the player you predict to have the most deaths on Team A:")
    selected_player_label.pack()
    team_a_players = team_rosters[team_a_var.get()]

    selected_player_var = tk.StringVar(most_deaths_team_a_window)
    selected_player_var.set(team_a_players[0])
    selected_player_dropdown = OptionMenu(most_deaths_team_a_window, selected_player_var, *team_a_players)
    selected_player_dropdown.pack()

    def save_prediction():
        prediction = selected_player_var.get()
        messagebox.showinfo("Prediction Saved", f"Prediction saved! Selected Player: {prediction}")
        most_deaths_team_a_predictions[selected_player.name] = prediction
        print(f"Most Deaths on Team A Prediction for {selected_player.name}: {prediction}")  # Print the prediction to console
        most_deaths_team_a_window.destroy()  # Close the current window
        if player_ids:
            predict_most_deaths_team_a()  # Spin the wheel for the next player
        else:
            #print_most_deaths_team_a_predictions()  # Print overall predictions
            print("Resetting...")
            #reset_player_ids()  # Reset player IDs for next predictions
            # Proceed to other predictions

    decision_made_button = tk.Button(most_deaths_team_a_window, text="Decision Made", command=save_prediction)
    decision_made_button.pack()

def predict_most_deaths_team_b():
    player_id = player_ids.pop(0)
    selected_player = players[player_id]

    most_deaths_team_b_window = tk.Toplevel(app)
    most_deaths_team_b_window.title("Most Deaths on Team B Prediction")
    most_deaths_team_b_window.config(bg= bg_colour_main)
     # This is for all the tkinker forms ------
    app.minsize(app_Width, app_Height)
    screen_Width = app.winfo_screenwidth()
    screen_Height = app.winfo_screenheight()
    x = (screen_Width / 2) - (app_Width / 2)
    y = (screen_Height / 1.5) - (app_Height / 2)
    most_deaths_team_b_window.geometry(f'{app_Width}x{app_Height}+{int(x)}+{int(y)}')
    # -----------------------------------------------------------

    selected_player_label = tk.Label(most_deaths_team_b_window, text=f"{selected_player.name}, Please select the player you predict to have the most deaths on Team B:")
    selected_player_label.pack()
    team_b_players = team_rosters[team_b_var.get()]

    selected_player_var = tk.StringVar(most_deaths_team_b_window)
    selected_player_var.set(team_b_players[0])
    selected_player_dropdown = OptionMenu(most_deaths_team_b_window, selected_player_var, *team_b_players)
    selected_player_dropdown.pack()

    def save_prediction():
        prediction = selected_player_var.get()
        messagebox.showinfo("Prediction Saved", f"Prediction saved! Selected Player: {prediction}")
        most_deaths_team_b_predictions[selected_player.name] = prediction
        print(f"Most Deaths on Team B Prediction for {selected_player.name}: {prediction}")  # Print the prediction to console
        most_deaths_team_b_window.destroy()  # Close the current window
        if player_ids:
            predict_most_deaths_team_b()  # Spin the wheel for the next player
        else:
            #print_most_deaths_team_b_predictions()  # Print overall predictions
            print("Resetting...")
            #reset_player_ids()  # Reset player IDs for next predictions
            # Proceed to other predictions

    decision_made_button = tk.Button(most_deaths_team_b_window, text="Decision Made", command=save_prediction)
    decision_made_button.pack()

def spin_wheel_predict_most_deaths_overall():
    if players:
        random.shuffle(player_ids)
        predict_most_deaths_overall()
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
def predict_most_deaths_overall():
    player_id = player_ids.pop(0)
    selected_player = players[player_id]

    most_deaths_window = tk.Toplevel(app)
    most_deaths_window.title("Most Deaths Prediction")
    most_deaths_window.config(bg= bg_colour_main)
     # This is for all the tkinker forms ------
    app.minsize(app_Width, app_Height)
    screen_Width = app.winfo_screenwidth()
    screen_Height = app.winfo_screenheight()
    x = (screen_Width / 2) - (app_Width / 2)
    y = (screen_Height / 1.5) - (app_Height / 2)
    most_deaths_window.geometry(f'{app_Width}x{app_Height}+{int(x)}+{int(y)}')
    # -----------------------------------------------------------

    selected_player_label = tk.Label(most_deaths_window, text=f"{selected_player.name}, Please select the player you predict to have the most deaths:")
    selected_player_label.pack()
    team_a_players = team_rosters[team_a_var.get()]
    team_b_players = team_rosters[team_b_var.get()]
    all_players = team_a_players + team_b_players

    selected_player_var = tk.StringVar(most_deaths_window)
    selected_player_var.set(all_players[0])
    selected_player_dropdown = OptionMenu(most_deaths_window, selected_player_var, *all_players)
    selected_player_dropdown.pack()

    def save_prediction():
        prediction = selected_player_var.get()
        messagebox.showinfo("Prediction Saved", f"Prediction saved! Selected Player: {prediction}")
        most_deaths_overall_predictions[selected_player.name] = prediction
        print(f"Most Deaths Prediction for {selected_player.name}: {prediction}")  # Print the prediction to console
        most_deaths_window.destroy()  # Close the current Most Deaths window
        if player_ids:
            predict_most_deaths_overall()  # Spin the wheel for the next player
        else:
            #print_most_deaths_overall_predictions()  # Print overall most deaths predictions
            print("Resetting...")
            reset_player_ids()  # Reset player IDs for next predictions
            spin_wheel_predict_least_deaths_overall()
            # Proceed to other predictions

    decision_made_button = tk.Button(most_deaths_window, text="Decision Made", command=save_prediction)
    decision_made_button.pack()

def predict_least_deaths_team_a():
    player_id = player_ids.pop(0)
    selected_player = players[player_id]

    least_deaths_team_a_window = tk.Toplevel(app)
    least_deaths_team_a_window.title("Least Deaths on Team A Prediction")
    least_deaths_team_a_window.config(bg= bg_colour_main)
     # This is for all the tkinker forms ------
    app.minsize(app_Width, app_Height)
    screen_Width = app.winfo_screenwidth()
    screen_Height = app.winfo_screenheight()
    x = (screen_Width / 2) - (app_Width / 2)
    y = (screen_Height / 1.5) - (app_Height / 2)
    least_deaths_team_a_window.geometry(f'{app_Width}x{app_Height}+{int(x)}+{int(y)}')
    # -----------------------------------------------------------

    selected_player_label = tk.Label(least_deaths_team_a_window, text=f"{selected_player.name}, Please select the player you predict to have the least deaths on Team A:")
    selected_player_label.pack()
    team_a_players = team_rosters[team_a_var.get()]

    selected_player_var = tk.StringVar(least_deaths_team_a_window)
    selected_player_var.set(team_a_players[0])
    selected_player_dropdown = OptionMenu(least_deaths_team_a_window, selected_player_var, *team_a_players)
    selected_player_dropdown.pack()

    def save_prediction():
        prediction = selected_player_var.get()
        messagebox.showinfo("Prediction Saved", f"Prediction saved! Selected Player: {prediction}")
        least_deaths_team_a_predictions[selected_player.name] = prediction
        print(f"Least Deaths on Team A Prediction for {selected_player.name}: {prediction}")  # Print the prediction to console
        least_deaths_team_a_window.destroy()  # Close the current window
        if player_ids:
            predict_least_deaths_team_a()  # Spin the wheel for the next player
        else:
            #print_least_deaths_team_a_predictions()  # Print overall predictions
            print("Resetting...")
            #reset_player_ids()  # Reset player IDs for next predictions
            # Proceed to other predictions

    decision_made_button = tk.Button(least_deaths_team_a_window, text="Decision Made", command=save_prediction)
    decision_made_button.pack()

def predict_least_deaths_team_b():
    player_id = player_ids.pop(0)
    selected_player = players[player_id]

    least_deaths_team_b_window = tk.Toplevel(app)
    least_deaths_team_b_window.title("Least Deaths on Team B Prediction")
    least_deaths_team_b_window.config(bg= bg_colour_main)
     # This is for all the tkinker forms ------
    app.minsize(app_Width, app_Height)
    screen_Width = app.winfo_screenwidth()
    screen_Height = app.winfo_screenheight()
    x = (screen_Width / 2) - (app_Width / 2)
    y = (screen_Height / 1.5) - (app_Height / 2)
    least_deaths_team_b_window.geometry(f'{app_Width}x{app_Height}+{int(x)}+{int(y)}')
    # -----------------------------------------------------------

    selected_player_label = tk.Label(least_deaths_team_b_window, text=f"{selected_player.name}, Please select the player you predict to have the least deaths on Team B:")
    selected_player_label.pack()
    team_b_players = team_rosters[team_b_var.get()]

    selected_player_var = tk.StringVar(least_deaths_team_b_window)
    selected_player_var.set(team_b_players[0])
    selected_player_dropdown = OptionMenu(least_deaths_team_b_window, selected_player_var, *team_b_players)
    selected_player_dropdown.pack()

    def save_prediction():
        prediction = selected_player_var.get()
        messagebox.showinfo("Prediction Saved", f"Prediction saved! Selected Player: {prediction}")
        least_deaths_team_b_predictions[selected_player.name] = prediction
        print(f"Least Deaths on Team B Prediction for {selected_player.name}: {prediction}")  # Print the prediction to console
        least_deaths_team_b_window.destroy()  # Close the current window
        if player_ids:
            predict_least_deaths_team_b()  # Spin the wheel for the next player
        else:
            #print_least_deaths_team_b_predictions()  # Print overall predictions
            print("Resetting...")
            #reset_player_ids()  # Reset player IDs for next predictions
            # Proceed to other predictions

    decision_made_button = tk.Button(least_deaths_team_b_window, text="Decision Made", command=save_prediction)
    decision_made_button.pack()

def spin_wheel_predict_least_deaths_overall():
    if players:
        random.shuffle(player_ids)
        predict_least_deaths_overall()

#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
def predict_least_deaths_overall():
    player_id = player_ids.pop(0)
    selected_player = players[player_id]

    least_deaths_window = tk.Toplevel(app)
    least_deaths_window.title("Least Deaths Prediction")
    least_deaths_window.config(bg= bg_colour_main)
     # This is for all the tkinker forms ------
    app.minsize(app_Width, app_Height)
    screen_Width = app.winfo_screenwidth()
    screen_Height = app.winfo_screenheight()
    x = (screen_Width / 2) - (app_Width / 2)
    y = (screen_Height / 1.5) - (app_Height / 2)
    least_deaths_window.geometry(f'{app_Width}x{app_Height}+{int(x)}+{int(y)}')
    # -----------------------------------------------------------

    selected_player_label = tk.Label(least_deaths_window, text=f"{selected_player.name}, Please select the player you predict to have the least deaths:")
    selected_player_label.pack()
    team_a_players = team_rosters[team_a_var.get()]
    team_b_players = team_rosters[team_b_var.get()]
    all_players = team_a_players + team_b_players

    selected_player_var = tk.StringVar(least_deaths_window)
    selected_player_var.set(all_players[0])
    selected_player_dropdown = OptionMenu(least_deaths_window, selected_player_var, *all_players)
    selected_player_dropdown.pack()

    def save_prediction():
        prediction = selected_player_var.get()
        messagebox.showinfo("Prediction Saved", f"Prediction saved! Selected Player: {prediction}")
        least_deaths_overall_predictions[selected_player.name] = prediction
        print(f"Least Deaths Prediction for {selected_player.name}: {prediction}")  # Print the prediction to console
        least_deaths_window.destroy()  # Close the current Least Deaths window
        if player_ids:
            predict_least_deaths_overall()  # Spin the wheel for the next player
        else:
            #print_least_deaths_overall_predictions()  # Print overall least deaths predictions
            print("Resetting...")
            reset_player_ids()  # Reset player IDs for next predictions
            spin_wheel_predict_best_kd_overall()
            # Proceed to other predictions

    decision_made_button = tk.Button(least_deaths_window, text="Decision Made", command=save_prediction)
    decision_made_button.pack()


def predict_best_kd_team_a():
    player_id = player_ids.pop(0)
    selected_player = players[player_id]

    best_kd_team_a_window = tk.Toplevel(app)
    best_kd_team_a_window.title("Best KD Ratio on Team A Prediction")
    best_kd_team_a_window.config(bg= bg_colour_main)
     # This is for all the tkinker forms ------
    app.minsize(app_Width, app_Height)
    screen_Width = app.winfo_screenwidth()
    screen_Height = app.winfo_screenheight()
    x = (screen_Width / 2) - (app_Width / 2)
    y = (screen_Height / 1.5) - (app_Height / 2)
    best_kd_team_a_window.geometry(f'{app_Width}x{app_Height}+{int(x)}+{int(y)}')
    # -----------------------------------------------------------

    selected_player_label = tk.Label(best_kd_team_a_window, text=f"{selected_player.name}, Please select the player you predict to have the best KD ratio on Team A:")
    selected_player_label.pack()
    team_a_players = team_rosters[team_a_var.get()]

    selected_player_var = tk.StringVar(best_kd_team_a_window)
    selected_player_var.set(team_a_players[0])
    selected_player_dropdown = OptionMenu(best_kd_team_a_window, selected_player_var, *team_a_players)
    selected_player_dropdown.pack()

    def save_prediction():
        prediction = selected_player_var.get()
        messagebox.showinfo("Prediction Saved", f"Prediction saved! Selected Player: {prediction}")
        best_kd_team_a_predictions[selected_player.name] = prediction
        print(f"Best KD Ratio on Team A Prediction for {selected_player.name}: {prediction}")  # Print the prediction to console
        best_kd_team_a_window.destroy()  # Close the current window
        if player_ids:
            predict_best_kd_team_a()  # Spin the wheel for the next player
        else:
            #print_best_kd_team_a_predictions()  # Print overall predictions
            print("Resetting...")
            #reset_player_ids()  # Reset player IDs for next predictions
            # Proceed to other predictions

    decision_made_button = tk.Button(best_kd_team_a_window, text="Decision Made", command=save_prediction)
    decision_made_button.pack()

def predict_best_kd_team_b():
    player_id = player_ids.pop(0)
    selected_player = players[player_id]

    best_kd_team_b_window = tk.Toplevel(app)
    best_kd_team_b_window.title("Best KD Ratio on Team B Prediction")
    best_kd_team_b_window.config(bg= bg_colour_main)
     # This is for all the tkinker forms ------
    app.minsize(app_Width, app_Height)
    screen_Width = app.winfo_screenwidth()
    screen_Height = app.winfo_screenheight()
    x = (screen_Width / 2) - (app_Width / 2)
    y = (screen_Height / 1.5) - (app_Height / 2)
    best_kd_team_b_window.geometry(f'{app_Width}x{app_Height}+{int(x)}+{int(y)}')
    # -----------------------------------------------------------

    selected_player_label = tk.Label(best_kd_team_b_window, text=f"{selected_player.name}, Please select the player you predict to have the best KD ratio on Team B:")
    selected_player_label.pack()
    team_b_players = team_rosters[team_b_var.get()]

    selected_player_var = tk.StringVar(best_kd_team_b_window)
    selected_player_var.set(team_b_players[0])
    selected_player_dropdown = OptionMenu(best_kd_team_b_window, selected_player_var, *team_b_players)
    selected_player_dropdown.pack()

    def save_prediction():
        prediction = selected_player_var.get()
        messagebox.showinfo("Prediction Saved", f"Prediction saved! Selected Player: {prediction}")
        best_kd_team_b_predictions[selected_player.name] = prediction
        print(f"Best KD Ratio on Team B Prediction for {selected_player.name}: {prediction}")  # Print the prediction to console
        best_kd_team_b_window.destroy()  # Close the current window
        if player_ids:
            predict_best_kd_team_b()  # Spin the wheel for the next player
        else:
            #print_best_kd_team_b_predictions()  # Print overall predictions
            print("Resetting...")
            #reset_player_ids()  # Reset player IDs for next predictions
            # Proceed to other predictions

    decision_made_button = tk.Button(best_kd_team_b_window, text="Decision Made", command=save_prediction)
    decision_made_button.pack()

def spin_wheel_predict_best_kd_overall():
    if players:
        random.shuffle(player_ids)
        predict_best_kd_overall()

#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
def predict_best_kd_overall():
    player_id = player_ids.pop(0)
    selected_player = players[player_id]

    best_kd_window = tk.Toplevel(app)
    best_kd_window.title("Best KD Prediction")
    best_kd_window.config(bg= bg_colour_main)
     # This is for all the tkinker forms ------
    app.minsize(app_Width, app_Height)
    screen_Width = app.winfo_screenwidth()
    screen_Height = app.winfo_screenheight()
    x = (screen_Width / 2) - (app_Width / 2)
    y = (screen_Height / 1.5) - (app_Height / 2)
    best_kd_window.geometry(f'{app_Width}x{app_Height}+{int(x)}+{int(y)}')
    # -----------------------------------------------------------

    selected_player_label = tk.Label(best_kd_window, text=f"{selected_player.name}, Please select the player you predict to have the best KD ratio:")
    selected_player_label.pack()
    team_a_players = team_rosters[team_a_var.get()]
    team_b_players = team_rosters[team_b_var.get()]
    all_players = team_a_players + team_b_players

    selected_player_var = tk.StringVar(best_kd_window)
    selected_player_var.set(all_players[0])
    selected_player_dropdown = OptionMenu(best_kd_window, selected_player_var, *all_players)
    selected_player_dropdown.pack()

    def save_prediction():
        prediction = selected_player_var.get()
        messagebox.showinfo("Prediction Saved", f"Prediction saved! Selected Player: {prediction}")
        best_kd_overall_predictions[selected_player.name] = prediction
        print(f"Best KD Prediction for {selected_player.name}: {prediction}")  # Print the prediction to console
        best_kd_window.destroy()  # Close the current Best KD window
        if player_ids:
            predict_best_kd_overall()  # Spin the wheel for the next player
        else:
           # print_best_kd_overall_predictions()  # Print overall best KD predictions
            print("Resetting...")
            reset_player_ids()  # Reset player IDs for next predictions
            spin_wheel_predict_worst_kd_overall()
            # Proceed to other predictions

    decision_made_button = tk.Button(best_kd_window, text="Decision Made", command=save_prediction)
    decision_made_button.pack()


def predict_worst_kd_team_a():
    player_id = player_ids.pop(0)
    selected_player = players[player_id]

    worst_kd_team_a_window = tk.Toplevel(app)
    worst_kd_team_a_window.title("Worst KD Ratio on Team A Prediction")
    worst_kd_team_a_window.config(bg= bg_colour_main)
     # This is for all the tkinker forms ------
    app.minsize(app_Width, app_Height)
    screen_Width = app.winfo_screenwidth()
    screen_Height = app.winfo_screenheight()
    x = (screen_Width / 2) - (app_Width / 2)
    y = (screen_Height / 1.5) - (app_Height / 2)
    worst_kd_team_a_window.geometry(f'{app_Width}x{app_Height}+{int(x)}+{int(y)}')
    # -----------------------------------------------------------

    selected_player_label = tk.Label(worst_kd_team_a_window, text=f"{selected_player.name}, Please select the player you predict to have the worst KD ratio on Team A:")
    selected_player_label.pack()
    team_a_players = team_rosters[team_a_var.get()]

    selected_player_var = tk.StringVar(worst_kd_team_a_window)
    selected_player_var.set(team_a_players[0])
    selected_player_dropdown = OptionMenu(worst_kd_team_a_window, selected_player_var, *team_a_players)
    selected_player_dropdown.pack()

    def save_prediction():
        prediction = selected_player_var.get()
        messagebox.showinfo("Prediction Saved", f"Prediction saved! Selected Player: {prediction}")
        worst_kd_team_a_predictions[selected_player.name] = prediction
        print(f"Worst KD Ratio on Team A Prediction for {selected_player.name}: {prediction}")  # Print the prediction to console
        worst_kd_team_a_window.destroy()  # Close the current window
        if player_ids:
            predict_worst_kd_team_a()  # Spin the wheel for the next player
        else:
            #print_worst_kd_team_a_predictions()  # Print overall predictions
            print("Resetting...")
            #reset_player_ids()  # Reset player IDs for next predictions
            # Proceed to other predictions

    decision_made_button = tk.Button(worst_kd_team_a_window, text="Decision Made", command=save_prediction)
    decision_made_button.pack()


def predict_worst_kd_team_b():
    player_id = player_ids.pop(0)
    selected_player = players[player_id]

    worst_kd_team_b_window = tk.Toplevel(app)
    worst_kd_team_b_window.title("Worst KD Ratio on Team B Prediction")
    worst_kd_team_b_window.config(bg= bg_colour_main)
     # This is for all the tkinker forms ------
    app.minsize(app_Width, app_Height)
    screen_Width = app.winfo_screenwidth()
    screen_Height = app.winfo_screenheight()
    x = (screen_Width / 2) - (app_Width / 2)
    y = (screen_Height / 1.5) - (app_Height / 2)
    worst_kd_team_b_window.geometry(f'{app_Width}x{app_Height}+{int(x)}+{int(y)}')
    # -----------------------------------------------------------

    selected_player_label = tk.Label(worst_kd_team_b_window, text=f"{selected_player.name}, Please select the player you predict to have the worst KD ratio on Team B:")
    selected_player_label.pack()
    team_b_players = team_rosters[team_b_var.get()]

    selected_player_var = tk.StringVar(worst_kd_team_b_window)
    selected_player_var.set(team_b_players[0])
    selected_player_dropdown = OptionMenu(worst_kd_team_b_window, selected_player_var, *team_b_players)
    selected_player_dropdown.pack()

    def save_prediction():
        prediction = selected_player_var.get()
        messagebox.showinfo("Prediction Saved", f"Prediction saved! Selected Player: {prediction}")
        worst_kd_team_b_predictions[selected_player.name] = prediction
        print(f"Worst KD Ratio on Team B Prediction for {selected_player.name}: {prediction}")  # Print the prediction to console
        worst_kd_team_b_window.destroy()  # Close the current window
        if player_ids:
            predict_worst_kd_team_b()  # Spin the wheel for the next player
        else:
            #print_worst_kd_team_b_predictions()  # Print overall predictions
            print("Resetting...")
            #reset_player_ids()  # Reset player IDs for next predictions
            # Proceed to other predictions

    decision_made_button = tk.Button(worst_kd_team_b_window, text="Decision Made", command=save_prediction)
    decision_made_button.pack()
    
def spin_wheel_predict_worst_kd_overall():
    if players:
        random.shuffle(player_ids)
        predict_worst_kd_overall()
    
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
def predict_worst_kd_overall():
    player_id = player_ids.pop(0)
    selected_player = players[player_id]

    worst_kd_window = tk.Toplevel(app)
    worst_kd_window.title("Worst KD Prediction")
    worst_kd_window.config(bg= bg_colour_main)
     # This is for all the tkinker forms ------
    app.minsize(app_Width, app_Height)
    screen_Width = app.winfo_screenwidth()
    screen_Height = app.winfo_screenheight()
    x = (screen_Width / 2) - (app_Width / 2)
    y = (screen_Height / 1.5) - (app_Height / 2)
    worst_kd_window.geometry(f'{app_Width}x{app_Height}+{int(x)}+{int(y)}')
    # -----------------------------------------------------------

    selected_player_label = tk.Label(worst_kd_window, text=f"{selected_player.name}, Please select the player you predict to have the worst KD ratio:")
    selected_player_label.pack()
    team_a_players = team_rosters[team_a_var.get()]
    team_b_players = team_rosters[team_b_var.get()]
    all_players = team_a_players + team_b_players

    selected_player_var = tk.StringVar(worst_kd_window)
    selected_player_var.set(all_players[0])
    selected_player_dropdown = OptionMenu(worst_kd_window, selected_player_var, *all_players)
    selected_player_dropdown.pack()

    def save_prediction():
        prediction = selected_player_var.get()
        messagebox.showinfo("Prediction Saved", f"Prediction saved! Selected Player: {prediction}")
        worst_kd_overall_predictions[selected_player.name] = prediction
        print(f"Worst KD Prediction for {selected_player.name}: {prediction}")  # Print the prediction to console
        worst_kd_window.destroy()  # Close the current Worst KD window
        if player_ids:
            predict_worst_kd_overall()  # Spin the wheel for the next player
        else:
            #print_worst_kd_overall_predictions()  # Print overall worst KD predictions
            print("Resetting...")
            reset_player_ids()  # Reset player IDs for next predictions
            spin_wheel_predict_most_dmg_overall()
            # Proceed to other predictions

    decision_made_button = tk.Button(worst_kd_window, text="Decision Made", command=save_prediction)
    decision_made_button.pack()


def predict_most_dmg_team_a():
    player_id = player_ids.pop(0)
    selected_player = players[player_id]

    most_dmg_team_a_window = tk.Toplevel(app)
    most_dmg_team_a_window.title("Most Damage on Team A Prediction")
    most_dmg_team_a_window.config(bg= bg_colour_main)
     # This is for all the tkinker forms ------
    app.minsize(app_Width, app_Height)
    screen_Width = app.winfo_screenwidth()
    screen_Height = app.winfo_screenheight()
    x = (screen_Width / 2) - (app_Width / 2)
    y = (screen_Height / 1.5) - (app_Height / 2)
    most_dmg_team_a_window.geometry(f'{app_Width}x{app_Height}+{int(x)}+{int(y)}')
    # -----------------------------------------------------------

    selected_player_label = tk.Label(most_dmg_team_a_window, text=f"{selected_player.name}, Please select the player you predict to deal the most damage on Team A:")
    selected_player_label.pack()
    team_a_players = team_rosters[team_a_var.get()]

    selected_player_var = tk.StringVar(most_dmg_team_a_window)
    selected_player_var.set(team_a_players[0])
    selected_player_dropdown = OptionMenu(most_dmg_team_a_window, selected_player_var, *team_a_players)
    selected_player_dropdown.pack()

    def save_prediction():
        prediction = selected_player_var.get()
        messagebox.showinfo("Prediction Saved", f"Prediction saved! Selected Player: {prediction}")
        most_dmg_team_a_predictions[selected_player.name] = prediction
        print(f"Most Damage on Team A Prediction for {selected_player.name}: {prediction}")  # Print the prediction to console
        most_dmg_team_a_window.destroy()  # Close the current window
        if player_ids:
            predict_most_dmg_team_a()  # Spin the wheel for the next player
        else:
            #print_most_dmg_team_a_predictions()  # Print overall predictions
            print("Resetting...")
            #reset_player_ids()  # Reset player IDs for next predictions
            # Proceed to other predictions

    decision_made_button = tk.Button(most_dmg_team_a_window, text="Decision Made", command=save_prediction)
    decision_made_button.pack()

def predict_most_dmg_team_b():
    player_id = player_ids.pop(0)
    selected_player = players[player_id]

    most_dmg_team_b_window = tk.Toplevel(app)
    most_dmg_team_b_window.title("Most Damage on Team B Prediction")
    most_dmg_team_b_window.config(bg= bg_colour_main)
     # This is for all the tkinker forms ------
    app.minsize(app_Width, app_Height)
    screen_Width = app.winfo_screenwidth()
    screen_Height = app.winfo_screenheight()
    x = (screen_Width / 2) - (app_Width / 2)
    y = (screen_Height / 1.5) - (app_Height / 2)
    most_dmg_team_b_window.geometry(f'{app_Width}x{app_Height}+{int(x)}+{int(y)}')
    # -----------------------------------------------------------

    selected_player_label = tk.Label(most_dmg_team_b_window, text=f"{selected_player.name}, Please select the player you predict to deal the most damage on Team B:")
    selected_player_label.pack()
    team_b_players = team_rosters[team_b_var.get()]

    selected_player_var = tk.StringVar(most_dmg_team_b_window)
    selected_player_var.set(team_b_players[0])
    selected_player_dropdown = OptionMenu(most_dmg_team_b_window, selected_player_var, *team_b_players)
    selected_player_dropdown.pack()

    def save_prediction():
        prediction = selected_player_var.get()
        messagebox.showinfo("Prediction Saved", f"Prediction saved! Selected Player: {prediction}")
        most_dmg_team_b_predictions[selected_player.name] = prediction
        print(f"Most Damage on Team B Prediction for {selected_player.name}: {prediction}")  # Print the prediction to console
        most_dmg_team_b_window.destroy()  # Close the current window
        if player_ids:
            predict_most_dmg_team_b()  # Spin the wheel for the next player
        else:
            #print_most_dmg_team_b_predictions()  # Print overall predictions
            print("Resetting...")
            #reset_player_ids()  # Reset player IDs for next predictions
            # Proceed to other predictions

    decision_made_button = tk.Button(most_dmg_team_b_window, text="Decision Made", command=save_prediction)
    decision_made_button.pack()


def spin_wheel_predict_most_dmg_overall():
    if players:
        random.shuffle(player_ids)
        predict_most_dmg_overall()
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
def predict_most_dmg_overall():
    player_id = player_ids.pop(0)
    selected_player = players[player_id]

    most_dmg_window = tk.Toplevel(app)
    most_dmg_window.title("Most Damage Prediction")
    most_dmg_window.config(bg= bg_colour_main)
     # This is for all the tkinker forms ------
    app.minsize(app_Width, app_Height)
    screen_Width = app.winfo_screenwidth()
    screen_Height = app.winfo_screenheight()
    x = (screen_Width / 2) - (app_Width / 2)
    y = (screen_Height / 1.5) - (app_Height / 2)
    most_dmg_window.geometry(f'{app_Width}x{app_Height}+{int(x)}+{int(y)}')
    # -----------------------------------------------------------

    selected_player_label = tk.Label(most_dmg_window, text=f"{selected_player.name}, Please select the player you predict to have dealt the most damage:")
    selected_player_label.pack()
    team_a_players = team_rosters[team_a_var.get()]
    team_b_players = team_rosters[team_b_var.get()]
    all_players = team_a_players + team_b_players

    selected_player_var = tk.StringVar(most_dmg_window)
    selected_player_var.set(all_players[0])
    selected_player_dropdown = OptionMenu(most_dmg_window, selected_player_var, *all_players)
    selected_player_dropdown.pack()

    def save_prediction():
        prediction = selected_player_var.get()
        messagebox.showinfo("Prediction Saved", f"Prediction saved! Selected Player: {prediction}")
        most_dmg_overall_predictions[selected_player.name] = prediction
        print(f"Most Damage Prediction for {selected_player.name}: {prediction}")  # Print the prediction to console
        most_dmg_window.destroy()  # Close the current Most Damage window
        if player_ids:
            predict_most_dmg_overall()  # Spin the wheel for the next player
        else:
            #print_most_dmg_overall_predictions()  # Print overall most damage predictions
            print("Resetting...")
            reset_player_ids()  # Reset player IDs for next predictions
            spin_wheel_predict_least_dmg_overall()
            # Proceed to other predictions

    decision_made_button = tk.Button(most_dmg_window, text="Decision Made", command=save_prediction)
    decision_made_button.pack()


def predict_least_dmg_team_a():
    player_id = player_ids.pop(0)
    selected_player = players[player_id]

    least_dmg_team_a_window = tk.Toplevel(app)
    least_dmg_team_a_window.title("Least Damage on Team A Prediction")
    least_dmg_team_a_window.config(bg= bg_colour_main)
     # This is for all the tkinker forms ------
    app.minsize(app_Width, app_Height)
    screen_Width = app.winfo_screenwidth()
    screen_Height = app.winfo_screenheight()
    x = (screen_Width / 2) - (app_Width / 2)
    y = (screen_Height / 1.5) - (app_Height / 2)
    least_dmg_team_a_window.geometry(f'{app_Width}x{app_Height}+{int(x)}+{int(y)}')
    # -----------------------------------------------------------

    selected_player_label = tk.Label(least_dmg_team_a_window, text=f"{selected_player.name}, Please select the player you predict to deal the least damage on Team A:")
    selected_player_label.pack()
    team_a_players = team_rosters[team_a_var.get()]

    selected_player_var = tk.StringVar(least_dmg_team_a_window)
    selected_player_var.set(team_a_players[0])
    selected_player_dropdown = OptionMenu(least_dmg_team_a_window, selected_player_var, *team_a_players)
    selected_player_dropdown.pack()

    def save_prediction():
        prediction = selected_player_var.get()
        messagebox.showinfo("Prediction Saved", f"Prediction saved! Selected Player: {prediction}")
        least_dmg_team_a_predictions[selected_player.name] = prediction
        print(f"Least Damage on Team A Prediction for {selected_player.name}: {prediction}")  # Print the prediction to console
        least_dmg_team_a_window.destroy()  # Close the current window
        if player_ids:
            predict_least_dmg_team_a()  # Spin the wheel for the next player
        else:
            #print_least_dmg_team_a_predictions()  # Print overall predictions
            print("Resetting...")
            #reset_player_ids()  # Reset player IDs for next predictions
            # Proceed to other predictions

    decision_made_button = tk.Button(least_dmg_team_a_window, text="Decision Made", command=save_prediction)
    decision_made_button.pack()
    
def predict_least_dmg_team_b():
    player_id = player_ids.pop(0)
    selected_player = players[player_id]

    least_dmg_team_b_window = tk.Toplevel(app)
    least_dmg_team_b_window.title("Least Damage on Team B Prediction")
    least_dmg_team_b_window.config(bg= bg_colour_main)
     # This is for all the tkinker forms ------
    app.minsize(app_Width, app_Height)
    screen_Width = app.winfo_screenwidth()
    screen_Height = app.winfo_screenheight()
    x = (screen_Width / 2) - (app_Width / 2)
    y = (screen_Height / 1.5) - (app_Height / 2)
    least_dmg_team_b_window.geometry(f'{app_Width}x{app_Height}+{int(x)}+{int(y)}')
    # -----------------------------------------------------------

    selected_player_label = tk.Label(least_dmg_team_b_window, text=f"{selected_player.name}, Please select the player you predict to deal the least damage on Team B:")
    selected_player_label.pack()
    team_b_players = team_rosters[team_b_var.get()]

    selected_player_var = tk.StringVar(least_dmg_team_b_window)
    selected_player_var.set(team_b_players[0])
    selected_player_dropdown = OptionMenu(least_dmg_team_b_window, selected_player_var, *team_b_players)
    selected_player_dropdown.pack()

    def save_prediction():
        prediction = selected_player_var.get()
        messagebox.showinfo("Prediction Saved", f"Prediction saved! Selected Player: {prediction}")
        least_dmg_team_b_predictions[selected_player.name] = prediction
        print(f"Least Damage on Team B Prediction for {selected_player.name}: {prediction}")  # Print the prediction to console
        least_dmg_team_b_window.destroy()  # Close the current window
        if player_ids:
            predict_least_dmg_team_b()  # Spin the wheel for the next player
        else:
            #print_least_dmg_team_b_predictions()  # Print overall predictions
            print("Resetting...")
            #reset_player_ids()  # Reset player IDs for next predictions
            # Proceed to other predictions

    decision_made_button = tk.Button(least_dmg_team_b_window, text="Decision Made", command=save_prediction)
    decision_made_button.pack()


def spin_wheel_predict_least_dmg_overall():
    if players:
        random.shuffle(player_ids)
        predict_least_dmg_overall()

#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
def predict_least_dmg_overall():
    player_id = player_ids.pop(0)
    selected_player = players[player_id]

    
    least_dmg_window = tk.Toplevel(app)
    least_dmg_window.title("Least Damage Prediction")
    least_dmg_window.config(bg= bg_colour_main)
     # This is for all the tkinker forms ------
    app.minsize(app_Width, app_Height)
    screen_Width = app.winfo_screenwidth()
    screen_Height = app.winfo_screenheight()
    x = (screen_Width / 2) - (app_Width / 2)
    y = (screen_Height / 1.5) - (app_Height / 2)
    least_dmg_window.geometry(f'{app_Width}x{app_Height}+{int(x)}+{int(y)}')
    # -----------------------------------------------------------

    selected_player_label = tk.Label(least_dmg_window, text=f"{selected_player.name}, Please select the player you predict to have dealt the least damage:")
    selected_player_label.pack()
    team_a_players = team_rosters[team_a_var.get()]
    team_b_players = team_rosters[team_b_var.get()]
    all_players = team_a_players + team_b_players

    selected_player_var = tk.StringVar(least_dmg_window)
    selected_player_var.set(all_players[0])
    selected_player_dropdown = OptionMenu(least_dmg_window, selected_player_var, *all_players)
    selected_player_dropdown.pack()

    def save_prediction():
        prediction = selected_player_var.get()
        messagebox.showinfo("Prediction Saved", f"Prediction saved! Selected Player: {prediction}")
        least_dmg_overall_predictions[selected_player.name] = prediction
        print(f"Least Damage Prediction for {selected_player.name}: {prediction}")  # Print the prediction to console
        least_dmg_window.destroy()  # Close the current Least Damage window
        if player_ids:
            predict_least_dmg_overall()  # Spin the wheel for the next player
        else:
            #print_least_dmg_overall_predictions()  # Print overall least damage predictions
            print("Resetting...")
            #reset_player_ids()  # Reset player IDs for next predictions
            # Proceed to other predictions

    decision_made_button = tk.Button(least_dmg_window, text="Decision Made", command=save_prediction)
    decision_made_button.pack()




# Example usage:
# Call predict_most_kills() when appropriate in your program flow to open the window for predictions


def print_hardpoint_predictions():
    print("Hardpoint Predictions:")
    for player, prediction in hardpoint_predictions.items():
        print(f"{player}: Prediction {prediction}")

def print_search_and_destroy_predictions():
    print("Search and Destroy Predictions:")
    for player, prediction in search_and_destroy_predictions.items():
        print(f"{player}: Prediction {prediction}")

def print_control_predictions():
    print("Control Predictions:")
    for player, prediction in control_predictions.items():
        print(f"{player}: Prediction {prediction}")
        
def print_most_kills_overall_predictions():
    print("Most Kills Overall Predictions:")
    for player_name, member in most_kills_overall_predictions.items():
        print(f"{player_name}: {member}")
        
def print_least_kills_overall_predictions():
    print("Least Kills Overall Predictions:")
    for player_name, member in least_kills_overall_predictions.items():
        print(f"{player_name}: {member}")

def save_predictions_to_file():
    with open("C:\\Users\\joela\\Desktop\\CDLGame\\data\\predictions.txt", "w") as file:
        if hardpoint_predictions:
            file.write("Hardpoint Predictions:\n")
            for player, prediction in hardpoint_predictions.items():
                file.write(f"{player}: {prediction}\n")

        if search_and_destroy_predictions:
            file.write("\nSearch and Destroy Predictions:\n")
            for player, prediction in search_and_destroy_predictions.items():
                file.write(f"{player}: {prediction}\n")

        if control_predictions:
            file.write("\nControl Predictions:\n")
            for player, prediction in control_predictions.items():
                file.write(f"{player}: {prediction}\n")

        if most_kills_overall_predictions:
            file.write("\nMost Kills Overall Predictions:\n")
            for player, prediction in most_kills_overall_predictions.items():
                file.write(f"{player}: {prediction}\n")

        if least_kills_overall_predictions:
            file.write("\nLeast Kills Overall Predictions:\n")
            for player, prediction in least_kills_overall_predictions.items():
                file.write(f"{player}: {prediction}\n")

        if most_deaths_overall_predictions:
            file.write("\nMost Deaths Overall Predictions:\n")
            for player, prediction in most_deaths_overall_predictions.items():
                file.write(f"{player}: {prediction}\n")

        if least_deaths_overall_predictions:
            file.write("\nLeast Deaths Overall Predictions:\n")
            for player, prediction in least_deaths_overall_predictions.items():
                file.write(f"{player}: {prediction}\n")

        if best_kd_overall_predictions:
            file.write("\nBest KD Ratio Overall Predictions:\n")
            for player, prediction in best_kd_overall_predictions.items():
                file.write(f"{player}: {prediction}\n")

        if worst_kd_overall_predictions:
            file.write("\nWorst KD Ratio Overall Predictions:\n")
            for player, prediction in worst_kd_overall_predictions.items():
                file.write(f"{player}: {prediction}\n")

        if most_dmg_overall_predictions:
            file.write("\nMost Damage Overall Predictions:\n")
            for player, prediction in most_dmg_overall_predictions.items():
                file.write(f"{player}: {prediction}\n")

        if least_dmg_overall_predictions:
            file.write("\nLeast Damage Overall Predictions:\n")
            for player, prediction in least_dmg_overall_predictions.items():
                file.write(f"{player}: {prediction}\n")

        if most_kills_team_a_predictions:
            file.write("\nMost Kills Team A Predictions:\n")
            for player, prediction in most_kills_team_a_predictions.items():
                file.write(f"{player}: {prediction}\n")

        if most_kills_team_b_predictions:
            file.write("\nMost Kills Team B Predictions:\n")
            for player, prediction in most_kills_team_b_predictions.items():
                file.write(f"{player}: {prediction}\n")

        if least_kills_team_a_predictions:
            file.write("\nLeast Kills Team A Predictions:\n")
            for player, prediction in least_kills_team_a_predictions.items():
                file.write(f"{player}: {prediction}\n")

        if least_kills_team_b_predictions:
            file.write("\nLeast Kills Team B Predictions:\n")
            for player, prediction in least_kills_team_b_predictions.items():
                file.write(f"{player}: {prediction}\n")

        if most_deaths_team_a_predictions:
            file.write("\nMost Deaths Team A Predictions:\n")
            for player, prediction in most_deaths_team_a_predictions.items():
                file.write(f"{player}: {prediction}\n")

        if most_deaths_team_b_predictions:
            file.write("\nMost Deaths Team B Predictions:\n")
            for player, prediction in most_deaths_team_b_predictions.items():
                file.write(f"{player}: {prediction}\n")

        if least_deaths_team_a_predictions:
            file.write("\nLeast Deaths Team A Predictions:\n")
            for player, prediction in least_deaths_team_a_predictions.items():
                file.write(f"{player}: {prediction}\n")

        if least_deaths_team_b_predictions:
            file.write("\nLeast Deaths Team B Predictions:\n")
            for player, prediction in least_deaths_team_b_predictions.items():
                file.write(f"{player}: {prediction}\n")

        if best_kd_team_a_predictions:
            file.write("\nBest KD Ratio Team A Predictions:\n")
            for player, prediction in best_kd_team_a_predictions.items():
                file.write(f"{player}: {prediction}\n")

        if best_kd_team_b_predictions:
            file.write("\nBest KD Ratio Team B Predictions:\n")
            for player, prediction in best_kd_team_b_predictions.items():
                file.write(f"{player}: {prediction}\n")

        if worst_kd_team_a_predictions:
            file.write("\nWorst KD Ratio Team A Predictions:\n")
            for player, prediction in worst_kd_team_a_predictions.items():
                file.write(f"{player}: {prediction}\n")

        if worst_kd_team_b_predictions:
            file.write("\nWorst KD Ratio Team B Predictions:\n")
            for player, prediction in worst_kd_team_b_predictions.items():
                file.write(f"{player}: {prediction}\n")

        if most_dmg_team_a_predictions:
            file.write("\nMost Damage Team A Predictions:\n")
            for player, prediction in most_dmg_team_a_predictions.items():
                file.write(f"{player}: {prediction}\n")

        if most_dmg_team_b_predictions:
            file.write("\nMost Damage Team B Predictions:\n")
            for player, prediction in most_dmg_team_b_predictions.items():
                file.write(f"{player}: {prediction}\n")

        if least_dmg_team_a_predictions:
            file.write("\nLeast Damage Team A Predictions:\n")
            for player, prediction in least_dmg_team_a_predictions.items():
                file.write(f"{player}: {prediction}\n")

        if least_dmg_team_b_predictions:
            file.write("\nLeast Damage Team B Predictions:\n")
            for player, prediction in least_dmg_team_b_predictions.items():
                file.write(f"{player}: {prediction}\n")


# Create the main application window
# CHRIS COMM - need to change app width and length as [app_Width = 750] and [app_Height = 270] .geometry(f'{app_Width}x{app_Height}) 

app = tk.Tk()
# loads some default misc items program found (line:65)
misc()
app.title("Player Selection App")
app.config(bg= bg_colour_main)




# This is for all the tkinker forms ------
app.minsize(app_Width, app_Height)
screen_Width = app.winfo_screenwidth()
screen_Height = app.winfo_screenheight()
x = (screen_Width / 2) - (app_Width / 2)
y = (screen_Height / 3) - (app_Height / 1)
app.geometry(f'{app_Width}x{app_Height}+{int(x)}+{int(y)}')
# -----------------------------------------------------------

# Create a button widget to get players
get_players_button = tk.Button(app, 
                               text="Get Players", 
                               command=get_players, 
                               width="35", 
                               height="5", 
                               font="35", 
                               background=colour_fore,
                               foreground=colour_black,
                               activebackground=colour_Puple,
                               activeforeground=colour_Puple,
                               highlightthickness=2,
                               highlightbackground=colour_Puple,
                               highlightcolor='WHITE',
                               border=20,
                               cursor='hand2')
get_players_button.grid(column=0, row=0)                              
get_players_button.pack(pady=10)

# Create a button widget to save predictions
save_button = tk.Button(app, 
                        text="Save Predictions", 
                        command=save_predictions_to_file, 
                        width="20", 
                        height="40", 
                        font="30",
                        background=colour_Puple,
                        foreground=colour_black,
                        activebackground=colour_Puple,
                        activeforeground=colour_Puple,
                        highlightthickness=2,
                        highlightbackground=colour_Puple,
                        highlightcolor='WHITE',
                        border=10,
                        cursor='hand2')
save_button.pack(pady=10)

# Start the main event loop
app.mainloop()
print("Beginning Print")
save_predictions_to_file("predictions.txt")
print("Print Done")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 20:09:52 2021
This file contains the GUI
We use Tkinter
@author: jackbrietzke
"""
import tkinter as tk
from PIL import ImageTk, Image
import stats as sts
import Hitter
QUERIES = []
PIRATE_GOLD = "#FDB827"
PIRATE_BLACK = '#27251F'

def start_tkinter(df):
    print('Starting Tkinter GUI')
    HEIGHT = 700
    WIDTH = 900
    window = tk.Tk()
    window.title("Pirates Hitting Analysis App")
    
    canvas = tk.Canvas(window, height=HEIGHT, width=WIDTH, bg=PIRATE_GOLD)
    canvas.pack()
    
    frame = tk.Frame(window, bg=PIRATE_BLACK, bd=5)
    frame.place(relx=0.5, rely=0.5, relwidth=0.9, relheight=0.9, anchor='c')

#   Creating Query Filters
    pitcher_team, hitter_team = create_team_menu(df, frame)
    player = create_player_menu(df, frame)
    start, end = create_inning_menu(df, frame)
    balls, strikes = create_count_menu(df, frame)
    margin, choice = create_margin_menu(df, frame)
    pitcher, hand = create_pitcher_menu(df, frame)
    first, second, third = create_runner_menu(df, frame)
    rbis, rbi_choice = create_rbi_menu(df, frame)
    event = create_event_menu(df, frame)
    s_month, s_day, s_year = create_start_date_menu(df, frame)
    e_month, e_day, e_year = create_end_date_menu(df, frame)
    
    query_options = {
        'pitcher_teams': pitcher_team,
        'hitter_teams': hitter_team,
        'player': player,
        'start_inning': start,
        'end_inning': end,
        'balls': balls,
        'strikes': strikes,
        'margin': margin,
        'choice': choice,
        'pitcher': pitcher,
        'hand': hand,
        'first': first,
        'second': second,
        'third': third,
        'rbis': rbis,
        'rbi_choice': rbi_choice,
        'event': event,
        's_month': s_month,
        's_day': s_day,
        's_year': s_year,
        'e_month': e_month,
        'e_day': e_day,
        'e_year': e_year
    }
    
    # Submit Button to create Dataframe Analysis
    submit_button = tk.Button(frame,
                              text='Analyze',
                              command= lambda: analyze(df, query_options, window))
    submit_button.place(relx=0.2, rely=0, relwidth=0.1)
    
    # Reset button
    reset_button = tk.Button(frame, text='Reset', command=reset)
    reset_button.place(relx=0.3, rely=0, relwidth=0.1)
    
    add_logo()
    add_note(frame)
    
    # Keeps application running
    window.mainloop() 
    
# Creating separate window to show stats
def analyze(df, query_options, window):
    print('Analyzing')
    # Setting the value selected
    for key, item in query_options.items():
        query_options[key] = item.get()
    stats_df = sts.get_search_criteria(df, query_options)
    # Updating Global queries
    QUERIES.append(sts.get_stats(stats_df).get_stats())
    # Creating new window
    newWindow = tk.Toplevel(window)
    newWindow.geometry('400x300')
    profile_frame = tk.Frame(newWindow, bg=PIRATE_BLACK)
    profile_frame.place(relheight=1, relwidth=1)
    # Displaying the stats in the newly created window
    q_counter = 0
    num_stats = len(QUERIES[0].items()) + 1
    num_queries = len(QUERIES) + 1
    for stats in QUERIES:
        s_counter = 0
        for key, value in stats.items():
            if(q_counter == 0):
                tk.Label(profile_frame, text=f'{key}: ', anchor='w').place(relx=(0.0), rely=(s_counter/num_stats), relwidth=0.2)
            tk.Label(profile_frame, text=f'{value}', anchor='w').place(relx=(0.2 + (q_counter*0.7/num_queries)), rely=(s_counter/num_stats), relwidth=0.7/num_queries)
            s_counter += 1
        q_counter += 1

# Adding note at bottom of Tkinter App
def add_note(frame):
    # Notes on the Operatiosn
    note = '''
    This program is meant to aid exploratory analysis of MLB player data.
    It has play-by-play data from 2016-2019.
    '-1' in the search menus evaluates to any/all values.
    Players are identified by first four letters of last name followed by first name initial
    and three numeric values (Adam Frazier == fraza001).
    '''
    note_label = tk.Label(frame, text=note, bg=PIRATE_GOLD, anchor='w', bd=0)
    note_label.place(relx=0.0, rely=0.8, relwidth=1)



# Adding Pirates Logo
def add_logo():
        print('Adding Logo')
        path = 'pirates.jpg'
        image1 = Image.open(path)
        image1 = image1.resize((250, 200))
        test = ImageTk.PhotoImage(image1)
        label1 = tk.Label(image=test)
        label1.image = test
        label1.place(relx=0.7, rely=0.1, relheight=0.26, relwidth=0.2)
        
# Resetting the queries run and displayed
def reset():
    print('Resetting')
    global QUERIES
    QUERIES = []
    
# Team Options Portion
def create_team_menu(df, frame):
    pitcher_team_options = df['Pitcher_Team'].unique().tolist()
    pitcher_team_options.sort()
    pitcher_team_options.append('ANY')
    pitcher_team_options_clicked = tk.StringVar()
    pitcher_team_options_clicked.set(pitcher_team_options[-1])
    pitcher_team_label = tk.Label(frame, text='Pitcher Team', bg=PIRATE_GOLD)
    pitcher_team_label.place(relx=0.1, rely=0.05, relwidth=0.1)
    pitcher_team_drop = tk.OptionMenu(frame, pitcher_team_options_clicked, *pitcher_team_options)
    pitcher_team_drop.place(relx=0.2, rely=0.05, relwidth=0.1)
    
    hitter_team_options = df['Hitter_Team'].unique().tolist()
    hitter_team_options.sort()
    hitter_team_options.append('ANY')
    hitter_team_options_clicked = tk.StringVar()
    hitter_team_options_clicked.set(hitter_team_options[-1])
    hitter_team_label = tk.Label(frame, text='Hitter Team', bg=PIRATE_GOLD)
    hitter_team_label.place(relx=0.3, rely=0.05, relwidth=0.1)
    hitter_team_drop = tk.OptionMenu(frame, hitter_team_options_clicked, *hitter_team_options)
    hitter_team_drop.place(relx=0.4, rely=0.05, relwidth=0.1)
    
    return pitcher_team_options_clicked, hitter_team_options_clicked

 # Player Names Portion
def create_player_menu(df, frame):
    player_options = df['Batter'].unique().tolist()
    player_options.sort()
    player_options.append('ANY')
    player_options_clicked = tk.StringVar()
    player_options_clicked.set(player_options[0])
    team_label = tk.Label(frame, text='Player', bg=PIRATE_GOLD)
    team_label.place(relx=0.1, rely=0.1, relwidth=0.1)
    player_drop = tk.OptionMenu(frame, player_options_clicked, *player_options)
    player_drop.place(relx=0.2, rely=0.1, relwidth=0.15)
    return player_options_clicked

# Inning Portion
def create_inning_menu(df, frame):
    max_innings = df['Inning'].max()
    innings_options = list(range(1,max_innings+1))
    
    start_innings_clicked = tk.IntVar()
    end_innings_clicked = tk.IntVar()
    start_innings_clicked.set(innings_options[0])
    end_innings_clicked.set(innings_options[-1])
    
    start_inning_label = tk.Label(frame, text='Start Inning', bg=PIRATE_GOLD)
    start_inning_label.place(relx=0.1, rely=0.15, relwidth=0.1)
    start_inning_drop = tk.OptionMenu(frame, start_innings_clicked, *innings_options)
    start_inning_drop.place(relx=0.2, rely=0.15, relwidth=0.1)
    
    end_inning_label = tk.Label(frame, text='End Inning', bg=PIRATE_GOLD)
    end_inning_label.place(relx=0.3, rely=0.15, relwidth=0.1)
    end_inning_drop = tk.OptionMenu(frame, end_innings_clicked, *innings_options)
    end_inning_drop.place(relx=0.4, rely=0.15, relwidth=0.1)
    
    return start_innings_clicked, end_innings_clicked

 # Count Portion
def create_count_menu(df, frame):
    ball_options = [-1] + list(range(0,4))
    strike_options = [-1] + list(range(0,3))
    balls_clicked = tk.IntVar()
    strikes_clicked = tk.IntVar()
    balls_clicked.set(ball_options[0])
    strikes_clicked.set(strike_options[0])

    balls_label = tk.Label(frame, text='Balls', bg=PIRATE_GOLD)
    balls_label.place(relx=0.1, rely=0.2, relwidth=0.1)
    balls_drop = tk.OptionMenu(frame, balls_clicked, *ball_options)
    balls_drop.place(relx=0.2, rely=0.2, relwidth=0.1)
    
    strikes_label = tk.Label(frame, text='Strikes', bg=PIRATE_GOLD)
    strikes_label.place(relx=0.3, rely=0.20, relwidth=0.1)
    strikes_drop = tk.OptionMenu(frame, strikes_clicked, *strike_options)
    strikes_drop.place(relx=0.4, rely=0.20, relwidth=0.1)
    
    return balls_clicked, strikes_clicked

 # Score Portion
def create_margin_menu(df, frame):
    margin_options = list(range(-1, 6))
    choice_options = ['ANY', 'Less', 'Greater']
    margin_clicked = tk.IntVar()
    choice_clicked = tk.StringVar()
    margin_clicked.set(margin_options[0])
    choice_clicked.set(choice_options[0])

    margin_label = tk.Label(frame, text='Margin', bg=PIRATE_GOLD)
    margin_label.place(relx=0.1, rely=0.25, relwidth=0.1)
    margin_drop = tk.OptionMenu(frame, margin_clicked, *margin_options)
    margin_drop.place(relx=0.2, rely=0.25, relwidth=0.1)
    
    choice_label = tk.Label(frame, text='Choice', bg=PIRATE_GOLD)
    choice_label.place(relx=0.3, rely=0.25, relwidth=0.1)
    choice_drop = tk.OptionMenu(frame, choice_clicked, *choice_options)
    choice_drop.place(relx=0.4, rely=0.25, relwidth=0.1)
    
    return margin_clicked, choice_clicked

 # Pitcher Portion
def create_pitcher_menu(df, frame):
    pitcher_options = df['Pitcher'].unique().tolist()
    pitcher_options.sort()
    pitcher_options.append('ANY')
    hand_options = ['ANY', 'R', 'L']
    
    pitcher_options_clicked = tk.StringVar()
    hand_options_clicked = tk.StringVar()
    
    pitcher_options_clicked.set(pitcher_options[-1])
    hand_options_clicked.set(hand_options[0])
    
    pitcher_label = tk.Label(frame, text='Pitcher', bg=PIRATE_GOLD)
    pitcher_label.place(relx=0.1, rely=0.3, relwidth=0.1)
    hand_label = tk.Label(frame, text='Hand', bg=PIRATE_GOLD)
    hand_label.place(relx=0.3, rely=0.3, relwidth=0.1)
    
    pitcher_drop = tk.OptionMenu(frame, pitcher_options_clicked, *pitcher_options)
    pitcher_drop.place(relx=0.2, rely=0.3, relwidth=0.1)
    hand_drop = tk.OptionMenu(frame, hand_options_clicked, *hand_options)
    hand_drop.place(relx=0.4, rely=0.3, relwidth=0.1)
   
    return pitcher_options_clicked, hand_options_clicked

# Runners portion
def create_runner_menu(df, frame):
    runner_options = ['ANY', 'On', 'Off']
    
    first_runner_clicked = tk.StringVar()
    second_runner_clicked = tk.StringVar()
    third_runner_clicked = tk.StringVar()
    
    first_runner_clicked.set(runner_options[0])
    second_runner_clicked.set(runner_options[0])
    third_runner_clicked.set(runner_options[0])
    
    first_runner_label = tk.Label(frame, text='Runner 1st', bg=PIRATE_GOLD)
    first_runner_label.place(relx=0.1, rely=0.35, relwidth=0.1)
    second_runner_label = tk.Label(frame, text='Runner 2nd', bg=PIRATE_GOLD)
    second_runner_label.place(relx=0.3, rely=0.35, relwidth=0.1)
    third_runner_label = tk.Label(frame, text='Runner 3rd', bg=PIRATE_GOLD)
    third_runner_label.place(relx=0.5, rely=0.35, relwidth=0.1)
    
    first_drop = tk.OptionMenu(frame, first_runner_clicked, *runner_options)
    first_drop.place(relx=0.2, rely=0.35, relwidth=0.1)
    second_drop = tk.OptionMenu(frame, second_runner_clicked, *runner_options)
    second_drop.place(relx=0.4, rely=0.35, relwidth=0.1)
    third_drop = tk.OptionMenu(frame, third_runner_clicked, *runner_options)
    third_drop.place(relx=0.6, rely=0.35, relwidth=0.1)
   
    return first_runner_clicked, second_runner_clicked, third_runner_clicked

# RBI portion
def create_rbi_menu(df, frame):
    margin_options = list(range(-1, 5))
    choice_options = ['ANY', 'Less', 'Greater']
    margin_clicked = tk.IntVar()
    choice_clicked = tk.StringVar()
    margin_clicked.set(margin_options[0])
    choice_clicked.set(choice_options[0])

    margin_label = tk.Label(frame, text='RBIs', bg=PIRATE_GOLD)
    margin_label.place(relx=0.1, rely=0.4, relwidth=0.1)
    margin_drop = tk.OptionMenu(frame, margin_clicked, *margin_options)
    margin_drop.place(relx=0.2, rely=0.4, relwidth=0.1)
    
    choice_label = tk.Label(frame, text='Choice', bg=PIRATE_GOLD)
    choice_label.place(relx=0.3, rely=0.4, relwidth=0.1)
    choice_drop = tk.OptionMenu(frame, choice_clicked, *choice_options)
    choice_drop.place(relx=0.4, rely=0.4, relwidth=0.1)
    
    return margin_clicked, choice_clicked

 # Event Types Portion
def create_event_menu(df, frame):
    event_options = [
        'ANY', 'Strikeout', 'Walk', 'Single',
        'Double', 'Triple', 'Homerun'
    ]
    event_options.sort()
    event_options.append('ALL')
    event_options_clicked = tk.StringVar()
    event_options_clicked.set(event_options[0])
    event_label = tk.Label(frame, text='Event', bg=PIRATE_GOLD)
    event_label.place(relx=0.1, rely=0.45, relwidth=0.1)
    event_drop = tk.OptionMenu(frame, event_options_clicked, *event_options)
    event_drop.place(relx=0.2, rely=0.45, relwidth=0.1)
    
    return event_options_clicked

# Adding Start Date Portion
def create_start_date_menu(df, frame):
    month_options = list(range(3,11))
    day_options = list(range(0,32))
    year_options = [2016, 2017, 2018, 2019]
    
    month_clicked = tk.IntVar()
    day_clicked = tk.IntVar()
    year_clicked = tk.IntVar()
    
    month_clicked.set(month_options[0])
    day_clicked.set(day_options[0])
    year_clicked.set(year_options[0])
    
    month_label = tk.Label(frame, text='Month', bg=PIRATE_GOLD)
    month_label.place(relx=0.1, rely=0.5, relwidth=0.1)
    day_label = tk.Label(frame, text='Day', bg=PIRATE_GOLD)
    day_label.place(relx=0.3, rely=0.5, relwidth=0.1)
    year_label = tk.Label(frame, text='Year', bg=PIRATE_GOLD)
    year_label.place(relx=0.5, rely=0.5, relwidth=0.1)
    
    
    first_drop = tk.OptionMenu(frame, month_clicked, *month_options)
    first_drop.place(relx=0.2, rely=0.5, relwidth=0.1)
    second_drop = tk.OptionMenu(frame, day_clicked, *day_options)
    second_drop.place(relx=0.4, rely=0.5, relwidth=0.1)
    third_drop = tk.OptionMenu(frame, year_clicked, *year_options)
    third_drop.place(relx=0.6, rely=0.5, relwidth=0.1)
   
    return month_clicked, day_clicked, year_clicked

 # End Date Portion
def create_end_date_menu(df, frame):
    month_options = list(range(3,11))
    day_options = list(range(1,32))
    year_options = [2016, 2017, 2018, 2019]
    
    month_clicked = tk.IntVar()
    day_clicked = tk.IntVar()
    year_clicked = tk.IntVar()
    
    month_clicked.set(month_options[-1])
    day_clicked.set(day_options[-1])
    year_clicked.set(year_options[-1])
    
    month_label = tk.Label(frame, text='Month', bg=PIRATE_GOLD)
    month_label.place(relx=0.1, rely=0.55, relwidth=0.1)
    day_label = tk.Label(frame, text='Day', bg=PIRATE_GOLD)
    day_label.place(relx=0.3, rely=0.55, relwidth=0.1)
    year_label = tk.Label(frame, text='Year', bg=PIRATE_GOLD)
    year_label.place(relx=0.5, rely=0.55, relwidth=0.1)
    
    
    first_drop = tk.OptionMenu(frame, month_clicked, *month_options)
    first_drop.place(relx=0.2, rely=0.55, relwidth=0.1)
    second_drop = tk.OptionMenu(frame, day_clicked, *day_options)
    second_drop.place(relx=0.4, rely=0.55, relwidth=0.1)
    third_drop = tk.OptionMenu(frame, year_clicked, *year_options)
    third_drop.place(relx=0.6, rely=0.55, relwidth=0.1)
   
    return month_clicked, day_clicked, year_clicked
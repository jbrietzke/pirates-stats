# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np
import tkinter as tk

def main():
    print('Beginning Program')
    pirates_csv = './master.csv'
    # pirates_hitter = './pirates_hitters.csv'
    # Read in Data to DF
    df = pd.read_csv(pirates_csv)
    # df.to_csv('master2.csv')
    start_tkinter(df)
  

    
def start_tkinter(df):
    print('Starting Tkinter GUI')
    HEIGHT = 700
    WIDTH = 900
    PIRATE_GOLD = "#FDB827"
    PIRATE_BLACK = '#27251F'
    window = tk.Tk()
    window.title("Pirates Hitting Analysis App")
    QUERIES = []
    MAX_ROWS = 15
    def analyze():
        print('Analyzing')
        query_options = {
            'pitcher_teams': pitcher_team.get(),
            'hitter_teams': hitter_team.get(),
            'player': player.get(),
            'start_inning': start.get(),
            'end_inning': end.get(),
            'balls': balls.get(),
            'strikes': strikes.get(),
            'margin': margin.get(),
            'choice': choice.get(),
            'pitcher': pitcher.get(),
            'hand': hand.get(),
            'first': first.get(),
            'second': second.get(),
            'third': third.get(),
            'rbis': rbis.get(),
            'rbi_choice': rbi_choice.get(),
            'event': event.get(),
            's_month': s_month.get(),
            's_day': s_day.get(),
            's_year': s_year.get(),
            'e_month': e_month.get(),
            'e_day': e_day.get(),
            'e_year': e_year.get()
        }
        stats_df = get_search_criteria(df, query_options)
        QUERIES.append(get_stats(stats_df).get_stats())
        newWindow = tk.Toplevel(window)
        newWindow.title = f'{player.get()} Analysis'
        newWindow.geometry('400x300')
        profile_frame = tk.Frame(newWindow, bg=PIRATE_BLACK)
        profile_frame.place(relheight=1, relwidth=1)
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
            
        
    
    canvas = tk.Canvas(window, height=HEIGHT, width=WIDTH, bg=PIRATE_GOLD)
    canvas.pack()
    
    frame = tk.Frame(window, bg=PIRATE_BLACK, bd=5)
    frame.place(relx=0.5, rely=0.5, relwidth=0.9, relheight=0.9, anchor='c')
    
   
    # Team Options Portion
    def create_team_menu():
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
    pitcher_team, hitter_team = create_team_menu()
   
    # Player Names Portion
    def create_player_menu():
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
    player = create_player_menu()
    
    # Innings Portion
    def create_inning_menu():
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
    start, end = create_inning_menu()
    
    # Count Portion
    def create_count_menu():
        ball_options = [-1] + list(range(0,4))
        strike_options = [-1] + list(range(0,3))
        balls_clicked = tk.IntVar()
        strikes_clicked = tk.IntVar()
        balls_clicked.set(ball_options[0])
        strikes_clicked.set(strike_options[0])
    
        balls_label = tk.Label(frame, text='Balls', bg=PIRATE_GOLD)
        balls_label.place(relx=0.1, rely=0.25, relwidth=0.1)
        balls_drop = tk.OptionMenu(frame, balls_clicked, *ball_options)
        balls_drop.place(relx=0.2, rely=0.25, relwidth=0.1)
        
        strikes_label = tk.Label(frame, text='Strikes', bg=PIRATE_GOLD)
        strikes_label.place(relx=0.3, rely=0.25, relwidth=0.1)
        strikes_drop = tk.OptionMenu(frame, strikes_clicked, *strike_options)
        strikes_drop.place(relx=0.4, rely=0.25, relwidth=0.1)
        
        return balls_clicked, strikes_clicked
    balls, strikes = create_count_menu()
    
    # Score Portion
    def create_margin_menu():
        margin_options = list(range(-1, 6))
        choice_options = ['ANY', 'Less', 'Greater']
        margin_clicked = tk.IntVar()
        choice_clicked = tk.StringVar()
        margin_clicked.set(margin_options[0])
        choice_clicked.set(choice_options[0])
    
        margin_label = tk.Label(frame, text='Margin', bg=PIRATE_GOLD)
        margin_label.place(relx=0.1, rely=0.35, relwidth=0.1)
        margin_drop = tk.OptionMenu(frame, margin_clicked, *margin_options)
        margin_drop.place(relx=0.2, rely=0.35, relwidth=0.1)
        
        choice_label = tk.Label(frame, text='Choice', bg=PIRATE_GOLD)
        choice_label.place(relx=0.3, rely=0.35, relwidth=0.1)
        choice_drop = tk.OptionMenu(frame, choice_clicked, *choice_options)
        choice_drop.place(relx=0.4, rely=0.35, relwidth=0.1)
        
        return margin_clicked, choice_clicked
    margin, choice = create_margin_menu()
    
    # Pitcher Portion
    def create_pitcher_menu():
        pitcher_options = df['Pitcher'].unique().tolist()
        pitcher_options.sort()
        pitcher_options.append('ANY')
        hand_options = ['ANY', 'R', 'L']
        
        pitcher_options_clicked = tk.StringVar()
        hand_options_clicked = tk.StringVar()
        
        pitcher_options_clicked.set(pitcher_options[-1])
        hand_options_clicked.set(hand_options[0])
        
        pitcher_label = tk.Label(frame, text='Pitcher', bg=PIRATE_GOLD)
        pitcher_label.place(relx=0.1, rely=0.4, relwidth=0.1)
        hand_label = tk.Label(frame, text='Hand', bg=PIRATE_GOLD)
        hand_label.place(relx=0.3, rely=0.4, relwidth=0.1)
        
        
        
        pitcher_drop = tk.OptionMenu(frame, pitcher_options_clicked, *pitcher_options)
        pitcher_drop.place(relx=0.2, rely=0.4, relwidth=0.1)
        hand_drop = tk.OptionMenu(frame, hand_options_clicked, *hand_options)
        hand_drop.place(relx=0.4, rely=0.4, relwidth=0.1)
       
        return pitcher_options_clicked, hand_options_clicked
    pitcher, hand = create_pitcher_menu()
    
    # Runners portion
    def create_runner_menu():
        runner_options = ['ANY', 'On', 'Off']
        
        first_runner_clicked = tk.StringVar()
        second_runner_clicked = tk.StringVar()
        third_runner_clicked = tk.StringVar()
        
        first_runner_clicked.set(runner_options[0])
        second_runner_clicked.set(runner_options[0])
        third_runner_clicked.set(runner_options[0])
        
        first_runner_label = tk.Label(frame, text='Runner 1st', bg=PIRATE_GOLD)
        first_runner_label.place(relx=0.1, rely=0.45, relwidth=0.1)
        second_runner_label = tk.Label(frame, text='Runner 2nd', bg=PIRATE_GOLD)
        second_runner_label.place(relx=0.3, rely=0.45, relwidth=0.1)
        third_runner_label = tk.Label(frame, text='Runner 3rd', bg=PIRATE_GOLD)
        third_runner_label.place(relx=0.5, rely=0.45, relwidth=0.1)
        
        
        first_drop = tk.OptionMenu(frame, first_runner_clicked, *runner_options)
        first_drop.place(relx=0.2, rely=0.45, relwidth=0.1)
        second_drop = tk.OptionMenu(frame, second_runner_clicked, *runner_options)
        second_drop.place(relx=0.4, rely=0.45, relwidth=0.1)
        third_drop = tk.OptionMenu(frame, third_runner_clicked, *runner_options)
        third_drop.place(relx=0.6, rely=0.45, relwidth=0.1)
       
        return first_runner_clicked, second_runner_clicked, third_runner_clicked
    first, second, third = create_runner_menu()
    
    # RBI portion
    def create_rbi_menu():
        margin_options = list(range(-1, 5))
        choice_options = ['ANY', 'Less', 'Greater']
        margin_clicked = tk.IntVar()
        choice_clicked = tk.StringVar()
        margin_clicked.set(margin_options[0])
        choice_clicked.set(choice_options[0])
    
        margin_label = tk.Label(frame, text='RBIs', bg=PIRATE_GOLD)
        margin_label.place(relx=0.1, rely=0.5, relwidth=0.1)
        margin_drop = tk.OptionMenu(frame, margin_clicked, *margin_options)
        margin_drop.place(relx=0.2, rely=0.5, relwidth=0.1)
        
        choice_label = tk.Label(frame, text='Choice', bg=PIRATE_GOLD)
        choice_label.place(relx=0.3, rely=0.5, relwidth=0.1)
        choice_drop = tk.OptionMenu(frame, choice_clicked, *choice_options)
        choice_drop.place(relx=0.4, rely=0.5, relwidth=0.1)
        
        return margin_clicked, choice_clicked
    rbis, rbi_choice = create_rbi_menu()
    
    # Event Types Portion
    def create_event_menu():
        event_options = [
            'ANY', 'Strikeout', 'Walk', 'Single',
            'Double', 'Triple', 'Homerun'
        ]
        event_options.sort()
        event_options.append('ALL')
        event_options_clicked = tk.StringVar()
        event_options_clicked.set(event_options[0])
        event_label = tk.Label(frame, text='Event', bg=PIRATE_GOLD)
        event_label.place(relx=0.1, rely=0.55, relwidth=0.1)
        event_drop = tk.OptionMenu(frame, event_options_clicked, *event_options)
        event_drop.place(relx=0.2, rely=0.55, relwidth=0.1)
        return event_options_clicked
    event = create_event_menu()
    
    
    # Adding Start Date Portion
    def create_start_date_menu():
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
        month_label.place(relx=0.1, rely=0.6, relwidth=0.1)
        day_label = tk.Label(frame, text='Day', bg=PIRATE_GOLD)
        day_label.place(relx=0.3, rely=0.6, relwidth=0.1)
        year_label = tk.Label(frame, text='Year', bg=PIRATE_GOLD)
        year_label.place(relx=0.5, rely=0.6, relwidth=0.1)
        
        
        first_drop = tk.OptionMenu(frame, month_clicked, *month_options)
        first_drop.place(relx=0.2, rely=0.6, relwidth=0.1)
        second_drop = tk.OptionMenu(frame, day_clicked, *day_options)
        second_drop.place(relx=0.4, rely=0.6, relwidth=0.1)
        third_drop = tk.OptionMenu(frame, year_clicked, *year_options)
        third_drop.place(relx=0.6, rely=0.6, relwidth=0.1)
       
        return month_clicked, day_clicked, year_clicked
    s_month, s_day, s_year = create_start_date_menu()
    
    # End Date Portion
    def create_end_date_menu():
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
        month_label.place(relx=0.1, rely=0.65, relwidth=0.1)
        day_label = tk.Label(frame, text='Day', bg=PIRATE_GOLD)
        day_label.place(relx=0.3, rely=0.65, relwidth=0.1)
        year_label = tk.Label(frame, text='Year', bg=PIRATE_GOLD)
        year_label.place(relx=0.5, rely=0.65, relwidth=0.1)
        
        
        first_drop = tk.OptionMenu(frame, month_clicked, *month_options)
        first_drop.place(relx=0.2, rely=0.65, relwidth=0.1)
        second_drop = tk.OptionMenu(frame, day_clicked, *day_options)
        second_drop.place(relx=0.4, rely=0.65, relwidth=0.1)
        third_drop = tk.OptionMenu(frame, year_clicked, *year_options)
        third_drop.place(relx=0.6, rely=0.65, relwidth=0.1)
       
        return month_clicked, day_clicked, year_clicked
    e_month, e_day, e_year = create_end_date_menu()
    # Submit Button to create Dataframe Analysis
    submit_button = tk.Button(frame, text='Analyze', command=analyze, bg='blue')
    submit_button.place(relx=0.2, rely=0)

    
    window.mainloop() 
    
    
    
    
# Sacrifice plays need to be handled
def get_stats(df):
    print('Getting Stats')
    # df = get_search_criteria(df)
    hitter = Hitter()
    for i, j in df.iterrows():
        if(j['Sac_Fly'] == 'T' or j['Sac_Hit'] == 'T'):
            pass
        elif(j['Event_Type'] in [2,3,18,19,20,21,22,23]):
            hitter.add_at_bats(1)
        if(j['Event_Type'] in [2,19]):
            hitter.add_outs(1)
        elif(j['Event_Type'] == 3):
            hitter.add_strikeouts(1)
        elif(j['Event_Type'] in [14,15,16]):
            hitter.add_walks(1)
        elif(j['Event_Type'] == 18):
            hitter.add_errors(1)
        elif(j['Event_Type'] == 20):
            hitter.add_singles(1)
        elif(j['Event_Type'] == 21):
            hitter.add_doubles(1)
        elif(j['Event_Type'] == 22):
            hitter.add_triples(1)
        elif(j['Event_Type'] == 23):
            hitter.add_homeruns(1)
    return hitter
    


def get_search_criteria(df, options):
    print('Get search Criteria')
    df = constraint_players(df, options['player'])
    df = constraint_team(df, options['pitcher_teams'], options['hitter_teams'])
    df = constraint_innings(df, options['start_inning'], options['end_inning'])
    df = constraint_count(df, options['balls'], options['strikes'])
    df = constraint_score(df, options['margin'], options['choice'])
    df = constraint_pitchers(df, options['pitcher'], options['hand'])
    df = constraint_runners(df, options['first'], options['second'], options['third'])
    df = constraint_rbis(df, options['rbis'], options['rbi_choice'])
    df = constraint_events(df, options['event'])
    df = constraint_dates(df, options['s_month'], options['s_day'], options['s_year'],
                          options['e_month'], options['e_day'], options['s_year'])
    return df

def constraint_dates(df, s_month, s_day, s_year,
                     e_month, e_day, e_year):
    print('Dates Constraint')
    df = df[(df['Year'] >= s_year) & (df['Year'] <= e_year)]
    df = df[(df['Month'] >= s_month) & (df['Month'] <= e_month)]
    df = df[(df['Day'] >= s_day) & (df['Day'] <= e_day)]
    return df

def constraint_players(df, player):
    print('Player constraint')
    # Needs to customize
    if(player == 'ANY'):
        pass
    else:
        df = df[df.Batter == player]    
    return df
  
def constraint_team(df, pitcher, hitter):
    print('Get Team Search')
    # This needs to be customized
    if(pitcher != 'ANY'):
        df = df[df['Pitcher_Team'] == pitcher]
    if(hitter != 'ANY'):
        df = df[df['Hitter_Team'] == hitter]
   
    return df
    
def constraint_innings(df, start, end):
    print('Get innings')
    # This needs to be custmoized
    df = df[(df['Inning'] >= start) & (df['Inning'] <= end)]
    return df

def constraint_count(df, balls, strikes):
    # Think of a better system than negative one
    print('Getting count')
    if(balls == -1):
        pass
    else:
        df = df[df['Balls'] == balls]
    if(strikes == -1):
        pass
    else:
        df = df[df['Strikes'] == strikes]
    return df
    
def constraint_score(df, margin, choice):
    print('Score Constraint')
    # Needs to be customized
    if(margin == -1):
        pass
    else:
        if(choice == 'ANY'):
            pass
        elif(choice == 'Less'):
            df = df[abs(df['Vis_Score'] - df['Home_Score']) <= margin]
        elif(choice == 'Greater'):
            df = df[abs(df['Vis_Score'] - df['Home_Score']) >= margin]
    return df

def constraint_pitchers(df, pitcher, hand):
    print('Pitcher constraint')
    # Need to customize
    if(pitcher == 'ANY'):
        if(hand == 'ANY'):
            print("This is being hit")
            pass
        else:
            df = df[df['Pitcher_Hand'] == hand]
    else:
        df = df[df['Pitcher'] == pitcher]
    
    return df

def constraint_runners(df, first, second, third):
    print('Runners Constraint')
    if(first == 'ANY'):
        pass
    elif(first == 'On'):
        df = df[df['First_Runner'].notnull()]
    elif(first == 'Off'):
        df = df[df['First_Runner'].isnull()]
    
    if(second == 'ANY'):
        pass
    elif(second == 'On'):
        df = df[df['Second_Runner'].notnull()]
    elif(second == 'Off'):
        df = df[df['Second_Runner'].isnull()]
        
    if(third == 'ANY'):
        pass
    elif(third == 'On'):
        df = df[df['Third_Runner'].notnull()]
    elif(first == 'Off'):
        df = df[df['Third_Runner'].isnull()]
    
    return df

def constraint_rbis(df, rbis, choice):
    print('Contraint rbis')
    # Needs to be customized
    if(rbis == -1):
        print('This Hits')
        pass
    else:
        if(choice == 'Less'):
            df = df[df['RBI'] <= rbis]
        elif(choice == 'Greater'):
            df = df[df['RBI'] >= rbis]
    
    return df

def constraint_events(df, event):
    print('Constraint Event')
    if(event == 'ANY'):
        pass
    elif(event == 'Strikeout'):
        df = df[df['Event_Type'] == 3]
    elif(event == 'Walk'):
        df = df[df['Event_Type'].isin([14,15,16])]
    elif(event == 'Single'):
        df = df[df['Event_Type'] == 20]
    elif(event == 'Double'):
        df = df[df['Event_Type'] == 21]
    elif(event == 'Triple'):
        df = df[df['Event_Type'] == 22]
    elif(event == 'Homerun'):
        df = df[df['Event_Type'] == 23]
    
    return df

class Hitter:
    def __init__(self, player_id='John Doe'):
        self.name = player_id
        self.at_bats = self.walks = self.strikeouts = self.outs = 0
        self.errors = self.singles = self.doubles = 0
        self.triples = self.homeruns = 0
    
    def get_avg(self):
        try:
            return round(
                ((self.singles + self.doubles + self.triples + self.homeruns) / self.at_bats)
                , 3)
        except Exception as e:
            print(e)
            return 0
    
    def get_slg(self):
        try:
            return round((((self.singles) + (self.doubles * 2) + 
                           (self.triples * 3) + (self.homeruns * 4)) / self.at_bats)
                         , 3)
        except Exception as e:
            print(e)
            return 0
        
    def get_obp(self):
        try:
            return round(((self.singles + self.doubles + self.triples + 
                           self.homeruns + self.walks) / (self.at_bats + self.walks))
                         , 3)
        except Exception as e:
            print(e)
            return 0
        
    def get_ops(self):
        return round(self.get_obp() + self.get_slg(), 3)
    
    def get_stats(self):
        return {
            'at_bats': self.at_bats,
            'walks': self.walks,
            'strikeouts': self.strikeouts,
            'outs': self.outs,
            'singles': self.singles,
            'doubles': self.doubles,
            'triples': self.triples,
            'homeruns': self.homeruns,
            'avg': self.get_avg(),
            'obp': self.get_obp(),
            'slg': self.get_slg(),
            'ops': self.get_ops()
        }
    
    def add_at_bats(self, num):
        self.at_bats += num
    
    def add_walks(self, num):
        self.walks += num
        
    def add_strikeouts(self, num):
        self.strikeouts += num
    
    def add_singles(self, num):
        self.singles += num
    
    def add_doubles(self, num):
        self.doubles += num
    
    def add_triples(self, num):
        self.triples += num
    
    def add_homeruns(self, num):
        self.homeruns += num
        
    def add_outs(self, num):
        self.outs += num
        
    def add_errors(self, num):
        self.errors += num
        


# event_action = {
#     1}

# 0    Unknown event
#           1    No event
#           2    Generic out
#           3    Strikeout
#           4    Stolen base
#           5    Defensive indifference
#           6    Caught stealing
#           7    Pickoff error
#           8    Pickoff
#           9    Wild pitch
#           10   Passed ball
#           11   Balk
#           12   Other advance
#           13   Foul error
#           14   Walk
#           15   Intentional walk
#           16   Hit by pitch
#           17   Interference
#           18   Error
#           19   Fielders choice
#           20   Single
#           21   Double
#           22   Triple
#           23   Home run
#           24   Missing play
    
main()
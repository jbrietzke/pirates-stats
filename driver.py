# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import tkinter as tk

def main():
    print('Beginning Program')
    pirates_csv = './bevent.csv'
    # pirates_hitter = './pirates_hitters.csv'
    # Read in Data to DF
    df = pd.read_csv(pirates_csv)
    # print(df)
    # Dropping Vis team hitting stats
    df = df[df.Batting == 1]
    # df1 = df.Vis_Score - df.Home_Score > 0
    # df2 = df[df['Vis_Score'] - df['Home_Score'] > 0]
    # print(df2)
    # # print(df)
    # df.to_csv(pirates_hitter)
    # df = df[df.Event_Type == 23]
    # df = df[df.Batter == "bellj005"]
    # get_search_criteria(df)
    # print('PIT Stats', df)
    start_tkinter(df)
  

    
def start_tkinter(df):
    print('Starting Tkinter GUI')
    HEIGHT = 700
    WIDTH = 800
    window = tk.Tk()
    window.title("Pirates Hitting Analysis App")
    
    def analyze():
        print('Analyzing')
        query_options = {
            'vis_teams': vis_team_options_clicked.get(),
            'player': player_options_clicked.get()
        }
        cleaned_df = get_search_criteria(df, query_options)
        print(cleaned_df)
        
    
    canvas = tk.Canvas(window, height=HEIGHT, width=WIDTH)
    canvas.pack()
    
    frame = tk.Frame(window, bg='yellow', bd=5)
    frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
    
   
    # Team Options Portion
    team_options = df['Vis_Team'].unique().tolist()
    team_options.sort()
    team_options.append('ALL')
    vis_team_options_clicked = tk.StringVar()
    vis_team_options_clicked.set(team_options[-1])
    team_label = tk.Label(frame, text='Vis Team')
    team_label.place(relx=0.4, rely=0.1, relwidth=0.1)
    team_drop = tk.OptionMenu(frame, vis_team_options_clicked, *team_options)
    team_drop.place(relx=0.5, rely=0.1, relwidth=0.1)
    
    # Player Names Portion
    player_options = df['Batter'].unique().tolist()
    player_options.sort()
    player_options.append('ALL')
    player_options_clicked = tk.StringVar()
    player_options_clicked.set(player_options[-1])
    team_label = tk.Label(frame, text='Player')
    team_label.place(relx=0.4, rely=0.2, relwidth=0.1)
    player_drop = tk.OptionMenu(frame, player_options_clicked, *player_options)
    player_drop.place(relx=0.5, rely=0.2, relwidth=0.1)
    
    
    # Innings Portion
    submit_button = tk.Button(frame, text='Analyze', command=analyze)
    submit_button.place(relx=0.5, rely=0.9)

    
    window.mainloop() 
    
    
    
    
# Sacrifice plays need to be handled
def get_stats(df):
    print('Getting Stats')
    df = get_search_criteria(df)
    hitter = Hitter()
    for i, j in df.iterrows():
        if(j['Event_Text'][0] == 'SH'):
            print('Sacrifice')
            print(j['Event_Text'])
       
        if(j['Event_Type'] in [2,3,18,19,20,21,22,23]):
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
    


def get_search_criteria(df, query_options):
    print('Get search Criteria')
    df = constraint_players(df, query_options['player'])
    df = constraint_team(df, query_options['vis_teams'])
    # df = constraint_innings(df, query_options)
    # df = constraint_count(df, query_options)
    # df = constraint_score(df, query_options)
    # df = constraint_pitchers(df, query_options)
    # df = constraint_runners(df, query_options)
    # df = constraint_rbis(df, query_options)
    # df = constraint_events(df, query_options)
    return df
  
def constraint_players(df, player):
    print('Player constraint')
    # Needs to customize
    if(player == 'ALL'):
        pass
    else:
        df = df[df.Batter == player]    
    return df
  
def constraint_team(df, vis_teams):
    print('Get Team Search')
    # This needs to be customized
    if(vis_teams == 'ALL'):
        pass
    else:
        df = df[df['Vis_Team'].isin(teams)]
    return df
    
def constraint_innings(df, query_options):
    print('Get innings')
    # This needs to be custmoized
    inning = 1
    inning_begin = 1
    inning_end = 30
    df = df[df['Inning'] >= inning]
    return df

def constraint_count(df, query_options):
    print('Getting count')
    balls = 0
    strikes = 0
    df = df[df['Balls'] == balls]
    df = df[df['Strikes'] == strikes]
    return df
    
def constraint_score(df, query_options):
    print('Score Constraint')
    # Needs to be customized
    vis_score = 0
    home_score = 0
    df = df[df['Vis_Score'] >= vis_score]
    df = df[df['Home_Score'] >= home_score]
    return df

def constraint_pitchers(df, query_options):
    print('Pitcher constraint')
    # Need to customize
    pitcher_hand = 'L'
    pitcher = ''
    df = df[df['Pitcher_Hand'] == pitcher_hand]
    return df

def constraint_runners(df, query_options):
    print('Runners Constraint')
    # Need to modify
    first_runner = True
    second_runner = True
    third_runner = True
    # Isnull works too
    df = df[df['First_Runner'].notnull()]
    df = df[df['Second_Runner'].notnull()]
    df = df[df['Third_Runner'].notnull()]
    return df

def constraint_rbis(df, query_options):
    print('Contraint rbis')
    # Needs to be customized
    rbis = 0
    df = df[df['RBI'] >= rbis]
    return df

def constraint_events(df, query_options):
    print('Constraint Event')
    events = [20]
    df = df[df['Event_Type'].isin(events)]
    return df

class Hitter:
    def __init__(self, player_id='John Doe'):
        self.name = player_id
        self.at_bats = self.walks = self.strikeouts = self.outs = 0
        self.errors = self.singles = self.doubles = 0
        self.triples = self.homeruns = 0
    
    def get_avg(self):
        return round(
            ((self.singles + self.doubles + self.triples + self.homeruns) / self.at_bats)
            , 3)
    
    def get_slg(self):
        return round((((self.singles) + (self.doubles * 2) + 
                       (self.triples * 3) + (self.homeruns * 4)) / self.at_bats)
                     , 3)
    
    def get_obp(self):
        return round(((self.singles + self.doubles + self.triples + 
                       self.homeruns + self.walks) / (self.at_bats + self.walks))
                     , 3)
    
    def get_ops(self):
        return self.get_obp() + self.get_slg()
    
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
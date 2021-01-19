# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd

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
    get_search_criteria(df)
    get_player_stats(df, 'fraza001')
    # print('PIT Stats', df)
    
# Sacrifice plays need to be handled
def get_player_stats(df, name):
    print(f'Getting {name} Stats')
    df = df[df.Batter == name]
    player = Hitter(name)
    for i, j in df.iterrows():
        if(j['Event_Text'][0] == 'SH'):
            print('Sacrifice')
            print(j['Event_Text'])
       
        if(j['Event_Type'] in [2,3,18,19,20,21,22,23]):
            player.add_at_bats(1)
        if(j['Event_Type'] in [2,19]):
            player.add_outs(1)
        elif(j['Event_Type'] == 3):
            player.add_strikeouts(1)
        elif(j['Event_Type'] in [14,15,16]):
            player.add_walks(1)
        elif(j['Event_Type'] == 18):
            player.add_errors(1)
        elif(j['Event_Type'] == 20):
            player.add_singles(1)
        elif(j['Event_Type'] == 21):
            player.add_doubles(1)
        elif(j['Event_Type'] == 22):
            player.add_triples(1)
        elif(j['Event_Type'] == 23):
            player.add_homeruns(1)
    return player
    

def get_search_criteria(df):
    print('Get search Criteria')
    get_teams(df)
    get_innings(df)
    
def get_teams(df):
    print('Get Team Search')
    # This needs to be customized
    teams = ['SLN']
    df = df[df['Vis_Team'].isin(teams)]
    return df
    
def get_innings(df):
    print('Get innings')
    # This needs to be custmoized
    inning = 1
    inning_begin = 1
    inning_end = 30
    df = df[df['Inning'] >= inning]
    return df
    
class Hitter:
    def __init__(self, player_id):
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
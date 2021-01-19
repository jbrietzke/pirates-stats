# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd

def main():
    print('Beginning Program')
    pirates_csv = './bevent.csv'
    pirates_hitter = './pirates_hitters.csv'
    # Read in Data to DF
    df = pd.read_csv(pirates_csv)
    # print(df)
    # Dropping Vis team hitting stats
    df = df[df.Batting == 1]
    # print(df)
    # df.to_csv(pirates_hitter)
    # df = df[df.Event_Type == 23]
    # df = df[df.Batter == "bellj005"]
    print(get_player_stats(df, 'fraza001'))
    # print('PIT Stats', df)
    
# Sacrifice plays need to be handled
def get_player_stats(df, name):
    print(f'Getting {name} Stats')
    df = df[df.Batter == name]
    at_bats = walks = strikeouts = outs = errors = singles = doubles = triples = homeruns = 0
    for i, j in df.iterrows():
        if(j['Event_Text'][0] == 'SH'):
            print('Sacrifice')
            print(j['Event_Text'])
       
        if(j['Event_Type'] in [2,3,18,19,20,21,22,23]):
            at_bats += 1
        if(j['Event_Type'] in [2,19]):
            outs += 1
        elif(j['Event_Type'] == 3):
            strikeouts += 1
        elif(j['Event_Type'] in [14,15,16]):
            walks += 1
        elif(j['Event_Type'] == 18):
            errors += 1
        elif(j['Event_Type'] == 20):
            singles += 1
        elif(j['Event_Type'] == 21):
            doubles += 1
        elif(j['Event_Type'] == 22):
            triples += 1
        elif(j['Event_Type'] == 23):
            homeruns += 1
    avg = (singles + doubles + triples + homeruns) / at_bats
    slg = ((singles) + (doubles * 2) + (triples * 3) + (homeruns * 4)) / at_bats
    obp = (singles + doubles + triples + homeruns + walks) / (at_bats + walks)
    ops = obp + slg
    hitter_profile = {
        'name': name,
        'singles': singles,
        'doubles': doubles,
        'triples': triples,
        'homeruns': homeruns,
        'walks': walks,
        'strikeouts': strikeouts,
        'avg': round(avg, 3),
        'obp': round(obp, 3),
        'slg': round(slg, 3),
        'ops': round(ops, 3),
        'at_bats': at_bats
    }
    return hitter_profile
    
def get_average(df):
    print('Getting Average')
    avg = 0
    return avg



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
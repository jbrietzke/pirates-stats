#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 20:13:17 2021
This is the stats file
This file contains different queries and filters to get stats
@author: jackbrietzke
"""
import Hitter
# Sacrifice plays need to be handled
def get_stats(df):
    print('Getting Stats')
    # df = get_search_criteria(df)
    hitter = Hitter.Hitter()
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
                          options['e_month'], options['e_day'], options['e_year'])
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
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 20:14:29 2021

@author: jackbrietzke
"""

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
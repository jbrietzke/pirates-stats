# -*- coding: utf-8 -*-
"""
Spyder Editor
This is the driver file for the Pirates Stats Query Tool
"""

import pandas as pd
import gui


def main():
    print('Beginning Program')
    pirates_csv = './main.csv'
    df = pd.read_csv(pirates_csv)
    gui.start_tkinter(df)
  

main()
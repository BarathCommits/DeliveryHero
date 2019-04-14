#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 12:53:32 2019

@author: barat243
"""
import sys
import pandas as pd 

class ImportData:
        
    @staticmethod
    def csv_to_df(inputFile):
        try:
            pd.set_option('precision',10)
            print('***<-- Importing data frame from input file : ' + inputFile +" -->***")
            input_df = pd.read_csv(inputFile)
            return input_df
        except IOError:
            print('Error reading file')
            sys.exit(2)
    
    def read_from_parquet(input_file):
        
        print('Not Implemented Yet')
        
    def read_from_mysql(jdbc,database,table,credentials):
        
        print('Yet to be implemented')
        
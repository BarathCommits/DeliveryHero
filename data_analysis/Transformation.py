#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 12:53:01 2019

@author: barat243
"""

import pandas as pd 

class Transformation:
    
    @staticmethod
    def inner_join_df(input_df,map_df):
        
        pd.set_option('precision',10)
        join_df = input_df.set_index('DOLocationID').join(map_df.set_index('LocationID'))
        
        return join_df
    
    @staticmethod
    def transform_datatype(join_df,col_name,new_datatype):
        
        join_df[col_name] = join_df[col_name].astype(new_datatype)
        
        return join_df
    
    def outer_join_df(input_df,map_df):
        
        print('Yet to be implemented')
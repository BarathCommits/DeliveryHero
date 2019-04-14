#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 12:53:54 2019

@author: barat243
"""

class SaveData:
    
    @staticmethod
    def df_to_csv(out_df,output_path):
        
        out_df.to_csv(output_path, sep=',', index=False)
        
    def df_to_parquet(out_df,output_path):
        
        print('yet to be Implemented')
    
    def df_to_mysql(out_df,jdbc_url,database,table):
        
        print('yet to be Implemented')
       
        
        
        
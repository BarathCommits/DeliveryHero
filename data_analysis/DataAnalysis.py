#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 12:07:58 2019

@author: barat243
"""

import argparse
from ImportData import ImportData as read
from SaveData import SaveData as save
from Transformation import Transformation as transform


"""
Data Analysis is the main module is build with the functionalities 
for injecting, transforming and calculating the desired result.

"""
class DataAnalysis:
    
    
    def import_data(self,input_file):
        
       
        input_df = read.csv_to_df(input_file)
        
        return input_df
        
        
    def transform_data(self,input_df,mapping_file,precession,column,new_datatype):
        
        
        map_df = read.csv_to_df(mapping_file)
        
        join_df = transform.inner_join_df(input_df,map_df)
        
        transformed_df = transform.transform_datatype(join_df,column,new_datatype)

        
        return transformed_df
        
    def calculate_top_tipping(self,transformed_df):
        
        
        top_tiping_df  = transformed_df.groupby(['Borough','Zone'])['tip_amount'].sum().sort_values(ascending=False).reset_index(name="total_tip_amount")
        
        return top_tiping_df.head(5)
    
    
    def calculate_longest_trip(self,transformed_df):
        
        list_of_values = ['2018/01/01','2018/01/02','2018/01/03','2018/01/04','2018/01/05','2018/01/06','2018/01/07']
        transformed_df['dropoff_date'] = transformed_df['tpep_dropoff_datetime'].dt.strftime('%Y/%m/%d')
        longest_df = transformed_df[['dropoff_date','tpep_dropoff_datetime','Borough','Zone','trip_distance']].dropna()
        longest_trip_filtered = longest_df[longest_df['dropoff_date'].isin(list_of_values)]
        longest_trip_df = longest_trip_filtered.sort_values(['dropoff_date','trip_distance'],ascending = [True,False]).groupby('dropoff_date').head(5)
        
        return longest_trip_df
    
    def save_output(self,out_df,output_path):
        
        save.df_to_csv(out_df,output_path)
        
    def visualize_data(input_df):
        
        print('***<-- Yet to be Implemented -->***')
        
        pass
    
def driver():
   
        
    parser = argparse.ArgumentParser(description='***<-- Pass Input Arguments -->***')
    parser.add_argument('--input', metavar='path', required=True, help='Input File path')
    parser.add_argument('--output', metavar='path', required=True, help='Output File Path')
    args = parser.parse_args()
    input_file = args.input
    output_path = args.output
    mapping_file = '../input/taxi+_zone_lookup.csv'
    
    print("***<-- Starting DataAnalysis -->***")
    da = DataAnalysis()
    print('***<-- Step 1 : Importing data from Input file -->***')
    input_df = da.import_data(input_file)
    #display(input_df.head(5))
    
    print('***<-- Succesfully completed importing data to data frame -->***')
    print('***<-- Step 2 : Transforming the data for Analysing -->***')
    
    transformed_df = da.transform_data(input_df,mapping_file,10,'tpep_dropoff_datetime','datetime64[ns]')
    #display(transformed_df.head(5))
    print('***<-- Succesfully completed transforming the data for Analysing -->***')
    print('***<-- Step 3 : Calculating the top tipping based on drop zones-->***')
    
    top_tipping_zones = da.calculate_top_tipping(transformed_df) 
    #display(top_tipping_zones)
    print('***<-- Succesfully completed calculating the top tipping based on drop zones -->***')
    print('***<-- Step 4 : Calculating longest trips for 1st week of jan 2018 -->***')
    
    longest_trips_per_day = da.calculate_longest_trip(transformed_df)
    #display(longest_trips_per_day)
    print('***<-- Succesfully completed calculating longest trips for 1st week of jan 2018 -->***')
    
    print('***<-- Step 5 : Save Output -->***')
    
    longest_output_path = output_path + 'longest_trips_per_day'
    da.save_output(longest_trips_per_day,longest_output_path)
    tipping_output_path = output_path + 'top_tipping_zones'
    da.save_output(top_tipping_zones,tipping_output_path)
    print('***<-- Succesfully saved the data frame to output file -->***')
    

if __name__ == '__main__': driver()

    

    
    
    
    
    
    
    
Deliver Hero - Data Analysis

Introduction :

The Purpose of this project is to analyse the taxi data for the month of January
2018 to calculate the longest rides for the first week of January and to calculate
the top tipping drop zones.

Execution  :

The input file location and the output location's are given as arguments to the 
python script DataAnalysis.py

The python scripts takes the input files from the location and reads it as dataframes 
and performs the desired transformations and writes the output files to the 
output path location mentioned in the arguments.

For mac/linux :

Clone the git repository to the local and execute the DataAnalysis.py script in the package
as below 

python DataAnalysis.py --input '../input/yellow_tripdata_2018-01.csv' --output '../output/'
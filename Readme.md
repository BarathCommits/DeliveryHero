Data Analysis

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

Please follow the below mentioned steps 

1. mkdir DeliveryHero

2. cd DeliveryHero

3. git init

4. git clone https://github.com/BarathCommits/DeliveryHero.git

5. cd DeliveryHero/data_analysis/

6. mkdir -p ../output

7. Download the required data set from the below mentioned website to ../input :
   https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page

8 . Execute the below mentioned command : 
    python DataAnalysis.py --input '../input/yellow_tripdata_2018-01.csv' --output '../output/'
    
After executing this command the desired output will be available in the ../output directory.

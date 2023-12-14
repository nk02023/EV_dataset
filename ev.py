# import required package 
import numpy as np
import pandas as pd

# read the dataset 
ev_df = pd.read_csv('Electric_Vehicle_Population_Data.csv') 
print(ev_df)

# studying dataset 

print(ev_df.info())
print(ev_df.describe())

# decided new data 

final_ev_df = ev_df[['VIN (1-10)','County','State','Model Year','Model','Base MSRP']]
print(final_ev_df)
County = final_ev_df['County'].unique()
State = final_ev_df['State'].unique()
Year = final_ev_df['Model Year'].unique()
Model = final_ev_df['Model'].unique()

print(County)
print(State)
print(Year)
print(Model)

# task create table in which columns county , state , years and model , find number of unique 



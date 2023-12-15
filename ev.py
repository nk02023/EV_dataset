# import required package 
import numpy as np
import pandas as pd

# read the dataset 
ev_df = pd.read_csv('Electric_Vehicle_Population_Data.csv') 
# print(ev_df)

# studying dataset 

# print(ev_df.info())
# print(ev_df.describe())

# decided new data 

final_ev_df = ev_df[['VIN (1-10)','County','State','Model Year','Model','Base MSRP']]
# ne= final_ev_df.drop(final_ev_df['VIN (1-10)'],axis=1)
County = final_ev_df['County'].unique()
State = final_ev_df['State'].unique()
Year = final_ev_df['Model Year'].unique()
Model = final_ev_df['Model'].unique()

# print(ne)
# print(County)
# print(State)
print(Year)
# print(Model)

# task create table in which columns county , state , years and model , find number of unique 
next_ev_df = ev_df[['County','State','Model Year','Model']]
State_count = len(next_ev_df['State'].unique())
County_count = len(next_ev_df['County'].unique())
Model_Y_count = len(next_ev_df['Model Year'].unique())
Model_count = len(next_ev_df['Model'].unique())
# print(next_ev_df)

# ---------------------------------------------------------------
#---- county ------ state ------ model year----

#  pd.DataFrame([{}])
table1 = pd.DataFrame([{'State':State_count,'County':County_count,'Model_year':Model_Y_count,'Model':Model_count}])
print(table1)

print(next_ev_df['Model Year'].describe())


# task
# Model year	Model
# 2023	12
# 2022	34
# 2021	51
# 2018	12
# 2017	82
# 2015	2

import pandas as pd

# read the dataset 
ev_df = pd.read_csv('Electric_Vehicle_Population_Data.csv') 
print(ev_df)

print(ev_df.info())


ev_df.dropna(inplace=True) # // delete who rows have missing value 
# ev_df['County'].fillna('Yakima') # //   
print(ev_df.info())
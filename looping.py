%%timeit

import pandas as pd
import numpy as np

# Define a basic Haversine distance formula
def haversine(lat1, lon1, lat2, lon2):
    MILES = 3959
    lat1, lon1, lat2, lon2 = map(np.deg2rad, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1 
    dlon = lon2 - lon1 
    a = np.sin(dlat/2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon/2)**2
    c = 2 * np.arcsin(np.sqrt(a)) 
    total_miles = MILES * c
    return total_miles

# Define a function to manually loop over all rows and return a series of distances
def haversine_crude_looping(df):
    distance_list = []
    for i in range(0, len(df)):
        d = haversine(40.671, -73.985, df.iloc[i]['latitude'], df.iloc[i]['longitude'])
        distance_list.append(d)
    return distance_list

def haversine_iterrows_looping(df):
    haversine_series = []
    for index, row in df.iterrows():
        haversine_series.append(haversine(40.671, -73.985, row['latitude'], row['longitude']))
    df['distance'] = haversine_series

def haversine_apply_looping(df):
    df['distance'] = df.apply(lambda row: haversine(40.671, -73.985, row['latitude'], row['longitude']), axis=1)


df = pd.read_csv('new_york_hotels.csv', encoding='cp1252')
#haversine_crude_looping(df)
#df['distance'] = haversine_iterrows_looping(df)
haversine_apply_looping(df)

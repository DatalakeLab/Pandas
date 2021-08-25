#space 1
%load_ext Cython
%timeit 

#space 2
%%cython -a
# Haversine cythonized
from libc.math cimport sin, cos, acos, asin, sqrt
import pandas as pd

cdef deg2rad_cy(float deg):
    cdef float rad
    rad = 0.01745329252*deg
    return rad
    
cpdef haversine_cy_dtyped(float lat1, float lon1, float lat2, float lon2):
    cdef: 
        float dlon
        float dlat
        float a
        float c
        float mi
    
    lat1, lon1, lat2, lon2 = map(deg2rad_cy, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1 
    dlon = lon2 - lon1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    mi = 3959 * c
    return mi

df = pd.read_csv('sample_data/new_york_hotels.csv', encoding='cp1252')
df.apply(lambda row: haversine_cy_dtyped(40.671, -73.985,\
                              row['latitude'], row['longitude']), axis=1)
print (df.size)

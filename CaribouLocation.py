import pandas as pd
from haversine import gcd
from row_calculate import row_calc
import math
import numpy as np


df = pd.read_csv('locations.csv')

df['lat_rads'] = df['latitude'].apply(lambda x: x*(math.pi)/180)
df['long_rads'] = df['longitude'].apply(lambda x: x*(math.pi)/180)
df['timestamp'] = pd.to_datetime(df.timestamp)

df = row_calc(df)
df.dist.isna().sum()
df.head()

avg_dist = df.groupby('animal_id')['dist'].mean().copy()
avg_dist.plot(kind = 'hist', bins = 20)

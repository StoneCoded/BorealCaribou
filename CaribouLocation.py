import pandas as pd
from haversine import gcd
from row_calculate import row_calc
import math
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('locations.csv')

df['lat_rads'] = df['latitude'].apply(lambda x: x*(math.pi)/180)
df['long_rads'] = df['longitude'].apply(lambda x: x*(math.pi)/180)
df['timestamp'] = pd.to_datetime(df.timestamp)

df = row_calc(df)
avg_dist = df.groupby('animal_id')['dist'].sum().copy()

df.groupby('animal_id')['dist'].sum().index
#
# fig, ax = plt.subplots()
# ax.scatter(df.groupby('animal_id')['dist'].sum().index, df.groupby('animal_id')['dist'].sum().values)
# plt.show()

df['month'] = df.timestamp.apply(lambda x: x.month)
def season(x):
    if x in [3,4,5]:
        return 'spring'
    elif x in [6,7,8]:
        return 'summer'
    elif x in [9,10,11]:
        return 'autumn'
    elif x in [12,1,2]:
        return 'winter'
df['season'] = df.month.apply(lambda x: season(x))

season_df = pd.DataFrame(columns = ['animal_id', 'spring', 'summer', 'autumn', 'winter'])

animals = df.animal_id.unique().tolist()
for anim in animals:
    temp = df[df['animal_id'] == anim].copy()
    temp1 = temp.groupby('season')['dist'].sum().to_frame().T.reset_index(drop=True)
    temp1['animal_id'] = anim
    season_df = season_df.append(temp1)


season_df.dropna(inplace = True)
sl = [season_df.spring.sum(), season_df.summer.sum(), season_df.autumn.sum(), season_df.winter.sum()]

fig, ax = plt.subplots()
ax.bar(['Spring', 'Summer', 'Autumn', 'Winter'], sl)
plt.show()

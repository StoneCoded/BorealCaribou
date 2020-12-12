
def row_calc(df):
    """
    ARGS: df: pandas DataFrame

    Returns: distance column added onto the orignal DataFrame.

    Calulates between two gps coordinates in a DataFrame with multiple
    moving objects and then adds them to a DataFrame. Needs haversine function
    to work properly. Also pretty specific to my needs for now.


    """
    import pandas as pd
    from haversine import gcd

    animals = (df.animal_id.unique().tolist())
    df_dist = pd.DataFrame({})
    #empty dataframe to add distances into

    for x in animals:
        ani_df = df[df['animal_id'] == x].copy()
        #creates a dataframe for each animal to calucalte on

        ani_df['dist'] = gcd(ani_df['lat_rads'].shift(), \
        ani_df['long_rads'].shift(), ani_df.loc[1:, 'lat_rads'], \
        ani_df.loc[1:, 'long_rads'])
        #applys haversine formula to animals coordinates to work out distance
        if len(ani_df) > 1:
            ani_df['dist'] = ani_df['dist'].fillna(value = ani_df.dist.mean())
        else:
            ani_df['dist'] = 0

        df_dist = pd.concat([df_dist, ani_df], ignore_index=True)
        #adds each animal to full distance dataframe
    df_dist = df_dist[['event_id', 'dist']]

    #removes extra columns
    return pd.merge(df, df_dist, on='event_id', how='left')
    #merges distances with main dataframe

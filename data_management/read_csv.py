import pandas
import numpy as np
import os
for i in range(1,61):
    str1 = str(i)
    path = str1.zfill(2) + '_tracks'
    print(path)
    pathname= 'E:/21_10_Control Transition/data/' + path + '.csv'
    print(pathname)
    df = pandas.read_csv(pathname)
    #get the columns of df
    cols = [
        'frame','id','x','y','width','height','xVelocity',
        'yVelocity','xAcceleration','yAcceleration','frontSightDistance',
        'backSightDistance','dhw','thw','ttc','precedingXVelocity',
        'precedingId','followingId','leftPrecedingId','leftAlongsideId',
        'leftFollowingId','rightPrecedingId','rightAlongsideId','rightFollowingId','laneId'
    ]

    for id in df['id'].unique():
        sub_df = df[df['id'] == id][cols]
        csvname = path + '_' + f'{id}'
        sub_df.to_csv(r'E:/21_10_Control Transition/data_management/data_tracks/' + f'{csvname}_data.csv',index=0)

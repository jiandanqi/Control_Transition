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
    df.columns=['frame','id','x','y','width','height','xVelocity',
            'yVelocity','xAcceleration','yAcceleration','frontSightDistance',
            'backSightDistance','dhw','thw','ttc','precedingXVelocity',
            'precedingId','followingId','leftPrecedingId','leftAlongsideId',
            'leftFollowingId','rightPrecedingId','rightAlongsideId','rightFollowingId','laneId'
            ]
    c=list(df.columns)
    print(path)
    print(c[1:2])
    group=df.groupby(c[1:2])
    for key, df in group:
        print(key)
        print(df)
    print(group)
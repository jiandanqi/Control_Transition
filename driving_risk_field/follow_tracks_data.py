import pandas as pd
import os
import numpy as np
import re
'''
此文件是将车辆在记录过程中，没有执行过变道行为，且全程前方50m内有车的情况记录为跟车数据，
当某一车辆在被数据集记录的行驶范围内未执行换道行为，且在行驶过程中，其所在车道前方 50 m 
范围内始终有其他车辆时，则以该车为主车的驾驶片段是一条跟车片段。单条跟车行为所包含的数据
内容为：主车及主车周围（主车所在车道及相邻车道的前、后 150m 范围内）其他车辆的时序的坐标、
速度、加速度信息，以及上述所有车辆的驾驶环境信息（道路类型和车道信息）。
'''

# 读取文件夹follow_tracks里1042条csv文件
path_data_follow_tracks = r'E:\21_10_Control Transition\driving_risk_field\follow_tracks'
path_data_follow_tracks_list = os.listdir(path_data_follow_tracks)  # 将csv文件名存储在列表里
for i in range(len(path_data_follow_tracks_list)):
    path_data_follow_tracks_name = 'E:/21_10_Control Transition/driving_risk_field/follow_tracks/' + path_data_follow_tracks_list[i]
    rules = re.compile(r'(.*?)_data.csv')  # 正则表达式，提取文件名片段
    old_follow_Filename = path_data_follow_tracks_list[i]
    new_follow_Filename = re.findall(rules, str(old_follow_Filename))[0]  # 生成新文件夹名
    print(new_follow_Filename)
    new_follow_group_Path = 'E:/21_10_Control Transition/driving_risk_field/follow_tracks_data/' + new_follow_Filename + '/'
    os.makedirs(new_follow_group_Path)
    print(new_follow_group_Path)
    data_follow_tracks_name = pd.read_csv(path_data_follow_tracks_name)
    data_follow_tracks_new = data_follow_tracks_name.loc[:, ['frame', 'id', 'x', 'y', 'xVelocity', 'yVelocity', 'xAcceleration', 'yAcceleration', 'laneId']]
    new_follow_group_name = new_follow_group_Path + 'main_' + new_follow_Filename + '.csv'  # 这个文件储存每组全程跟车行为数据

    #data_follow_tracks_new.to_csv(f'{new_follow_group_name}')

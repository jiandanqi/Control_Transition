import pandas as pd
import os
import numpy as np
import shutil

# 此文件统计跟车行为以及统计周边数据信息
num_lane_follow = 0  # 与前车最小距离小于等于50且无变道的车辆数量
num_follow = 0  # 全程跟车无换道的车辆数量
num_follow1 = 0
meta_follow_lane = []  # 存储tracksMeta文件名称的列表
# 判断与前车最小距离小于等于50且无变道的车辆数量
for i in range(1, 61):
    str_path = str(i)
    path_tracksMeta = str_path.zfill(2) + '_tracksMeta'
    meta_follow_lane.append(path_tracksMeta)
    pathname_tracksMeta = 'E:/21_10_Control Transition/data/' + path_tracksMeta + '.csv'
    follow_tracks = pd.read_csv(pathname_tracksMeta)
    follow_tracks_distance = follow_tracks['minDHW']  # 与前车最小距离
    follow_tracks_distance_list = follow_tracks_distance.values.tolist()  # 将minDHW数据存储在列表里
    judge_tracks_change = follow_tracks['numLaneChanges']  # 是否有变道，车道变化次数
    judge_tracks_change_list = judge_tracks_change.values.tolist()  # 将numLaneChanges数据存储在列表里
    for k in range(len(follow_tracks_distance_list)):
        if 0 < follow_tracks_distance_list[k] <= 50 and judge_tracks_change_list[k] == 0:  # 当与前车距离属于(0，50]之间且无变道行为判断为跟车
            num_lane_follow = num_lane_follow + 1
print(num_lane_follow)
# 判断
path_data_tracks = r'E:\21_10_Control Transition\data_management\data_tracks'
path_data_tracks_list = os.listdir(path_data_tracks)  # 将csv文件名存储在列表里
for i in range(len(path_data_tracks_list)):
    path_data_tracks_name = 'E:/21_10_Control Transition/data_management/data_tracks/' + path_data_tracks_list[i]
    data_tracks_name = pd.read_csv(path_data_tracks_name)
    data_tracks_lane = data_tracks_name['laneId']  # 车行走的道
    data_tracks_lane_list = data_tracks_lane.values.tolist()  # 将laneId列中的数据保存在列表里
    set_tracks_lane = set(data_tracks_lane_list)  # set集合中不允许重复元素出现，可以判断是否换道
    data_tracks_follow = data_tracks_name['dhw']  # 与前车距离，前车不存在为0
    data_tracks_follow_list = data_tracks_follow.values.tolist()  # 将dhw列中的数据保存在列表里
    data_tracks_follow_array = np.array(data_tracks_follow_list)
    DRF_follow_path = "E:/21_10_Control Transition/driving_risk_field/follow_tracks"  # DRF == driving_risk_field
    if 0 < data_tracks_follow_array.all() <= 50 and len(set_tracks_lane) == 1:
        num_follow = num_follow + 1
        shutil.copy(path_data_tracks_name, DRF_follow_path)  # 将这里的跟车文件复制到新文件夹
    if 0 <= data_tracks_follow_array.all() <= 50 and len(set_tracks_lane) == 1:
        num_follow1 = num_follow1 + 1
        if data_tracks_follow_array.all() == 0:
            num_follow1 = num_follow1 - 1
print(num_follow)
print(num_follow1)

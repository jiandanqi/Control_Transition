import numpy as np
import math
import sys
import pandas as pd

# 上车道换道判断

# 上车道中线坐标
for k in range(1, 61):
    str2 = str(k)
    path_recordingMeta1 = str2.zfill(2) + '_recordingMeta'
    print(path_recordingMeta1)
    pathname_recordingMeta1 = 'E:/21_10_Control Transition/data/' + path_recordingMeta1 + '.csv'
    # print(pathname_recordingMeta)
    data_recordingMeta1 = pd.read_csv(pathname_recordingMeta1)
    #print(data_recordingMeta1)
    locals()['col_' + path_recordingMeta1] = data_recordingMeta1["upperLaneMarkings"]
    #print(locals()['col_' + path_recordingMeta1])
    locals()['data_' + path_recordingMeta1] = np.array(locals()['col_' + path_recordingMeta1])
    #print(locals()['data_' + path_recordingMeta1])
    str1 = str(locals()['data_' + path_recordingMeta1])[1:-1]
    str1_1 = str1.strip('\'')
    #print(str1_1)
    list1 = str1_1.split(";")
    num1 = len(list1)
    if num1 == 3:
        list_down_lane1 = ['up_l1', 'up_l2', 'up_l3']
        dict_up_lane1 = {}
        for i in range(len(list_down_lane1)):
            dict_up_lane1[list_down_lane1[i]] = list1[i]
        #print(type(dict_up_lane1))
        print(dict_up_lane1)
    else:
        list_up_lane2 = ['up_l1', 'up_l2', 'up_l3', 'up_l4']
        dict_up_lane2 = {}
        for i in range(len(list_up_lane2)):
            dict_up_lane2[list_up_lane2[i]] = list1[i]
        #print(type(dict_up_lane2))
        print(dict_up_lane2)


# 下车道车道线坐标
for j in range(1, 61):
    str3 = str(j)
    path_recordingMeta2 = str3.zfill(2) + '_recordingMeta'
    print(path_recordingMeta2)
    pathname_recordingMeta2 = 'E:/21_10_Control Transition/data/' + path_recordingMeta2 + '.csv'
    data_recordingMeta2 = pd.read_csv(pathname_recordingMeta2)
    locals()['col_' + path_recordingMeta2] = data_recordingMeta2["lowerLaneMarkings"]
    locals()['data_' + path_recordingMeta2] = np.array(locals()['col_' + path_recordingMeta2])
    print(locals()['data_' + path_recordingMeta2])
    str2 = str(locals()['data_' + path_recordingMeta2])[1:-1]
    str2_1 = str2.strip('\'')
    list2 = str2_1.split(";")
    num2 = len(list2)
    if num2 == 3:
        list_down_lane1 = ['down_l1', 'down_l2', 'down_l3']
        dict_down_lane1 = {}
        for i in range(len(list_down_lane1)):
            dict_down_lane1[list_down_lane1[i]] = list2[i]
        print(dict_down_lane1)
    else:
        list_down_lane2 = ['down_l1', 'down_l2', 'down_l3', 'down_l4']
        dict_down_lane2 = {}
        for i in range(len(list_down_lane2)):
            dict_down_lane2[list_down_lane2[i]] = list2[i]
        print(dict_down_lane2)
# 跨道点判断：判断车辆轨迹是否与车道线相交


# 汽车航向角
#def f(x, y):  # 车辆航向角计算
    #return ((y + height / 2) ** t - (y + height / 2) ** (t - 3)) / ((x + width) ** t - (x + width) ** (t - 3))



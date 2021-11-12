import numpy as np
import math
import sys
import pandas as pd

# 上车道中线坐标
# 1为双车道 2为三车道
num_up1 = 0
num_up2 = 0
data_up_lane1 = []  # 储存双车道的字典的列表
data_up_lane2 = []  # 储存三车道的字典的列表
meta_up_lane = []  # 名称的列表
for k in range(1, 61):
    str2 = str(k)
    path_recordingMeta1 = str2.zfill(2) + '_recordingMeta'
    #print(path_recordingMeta1)
    meta_up_lane.append(path_recordingMeta1)
    pathname_recordingMeta1 = 'E:/21_10_Control Transition/data/' + path_recordingMeta1 + '.csv'
    data_recordingMeta1 = pd.read_csv(pathname_recordingMeta1)
    locals()['col_' + path_recordingMeta1] = data_recordingMeta1["upperLaneMarkings"]
    locals()['data_' + path_recordingMeta1] = np.array(locals()['col_' + path_recordingMeta1])
    str1 = str(locals()['data_' + path_recordingMeta1])[1:-1]
    str1_1 = str1.strip('\'')
    list1 = str1_1.split(";")
    num1 = len(list1)
    if num1 == 3:
        list_down_lane1 = ['up_l1', 'up_l2', 'up_l3']
        dict_up_lane1 = {}
        for i in range(len(list_down_lane1)):
            dict_up_lane1[list_down_lane1[i]] = list1[i]
            # data_up_lane1.append(dict_up_lane1)
        #print(dict_up_lane1)
        data_up_lane1.append(dict_up_lane1)
        num_up1 = num_up1 + 1
    else:
        list_up_lane2 = ['up_l1', 'up_l2', 'up_l3', 'up_l4']
        dict_up_lane2 = {}
        for i in range(len(list_up_lane2)):
            dict_up_lane2[list_up_lane2[i]] = list1[i]
        #print(dict_up_lane2)
        data_up_lane2.append(dict_up_lane2)
        num_up2 = num_up2 + 1
print('\n')
print('上车道')
print('-------------------------------------------------------------------------')
print('双车道的数量：' + f'{num_up1}')
print('三车道的数量：' + f'{num_up2}')
print('-------------------------------------------------------------------------')
#print(data_up_lane1)
#print(type(data_up_lane1))
data_up_dic1 = ['01_recordingMeta', '02_recordingMeta', '03_recordingMeta', '15_recordingMeta', '16_recordingMeta',
                '17_recordingMeta', '18_recordingMeta', '19_recordingMeta', '20_recordingMeta', '21_recordingMeta',
                '22_recordingMeta', '23_recordingMeta', '24_recordingMeta']
data_up_dic2 = []
dic_up_1 = {}  # 双车道带名称字典
dic_up_2 = {}  # 三车道带名称字典
for m in meta_up_lane:
    if m not in data_up_dic1:
        data_up_dic2.append(m)
for i in range(len(data_up_dic1)):
    dic_up_1[data_up_dic1[i]] = data_up_lane1[i]
for i in range(len(data_up_dic2)):
    dic_up_2[data_up_dic2[i]] = data_up_lane2[i]
#print(meta_up_lane)
#print(len(meta_up_lane))
#print(data_up_dic1)
#print(len(data_up_dic1))
#print(data_up_dic2)
#print(len(data_up_dic2))
print('双车道（下）：' + f'{dic_up_1}')
print('三车道（下）：' + f'{dic_up_2}')
print('-------------------------------------------------------------------------')

# 下车道车道线坐标
num_down1 = 0
num_down2 = 0
data_down_lane1 = []  # 储存双车道的字典的列表
data_down_lane2 = []  # 储存三车道的字典的列表
for j in range(1, 61):
    str3 = str(j)
    path_recordingMeta2 = str3.zfill(2) + '_recordingMeta'
    #print(path_recordingMeta2)
    pathname_recordingMeta2 = 'E:/21_10_Control Transition/data/' + path_recordingMeta2 + '.csv'
    data_recordingMeta2 = pd.read_csv(pathname_recordingMeta2)
    locals()['col_' + path_recordingMeta2] = data_recordingMeta2["lowerLaneMarkings"]
    locals()['data_' + path_recordingMeta2] = np.array(locals()['col_' + path_recordingMeta2])
    str2 = str(locals()['data_' + path_recordingMeta2])[1:-1]
    str2_1 = str2.strip('\'')
    list2 = str2_1.split(";")
    num2 = len(list2)
    if num2 == 3:
        list_down_lane1 = ['down_l1', 'down_l2', 'down_l3']
        dict_down_lane1 = {}
        for i in range(len(list_down_lane1)):
            dict_down_lane1[list_down_lane1[i]] = list2[i]
        #print(dict_down_lane1)
        data_down_lane1.append(dict_down_lane1)
        num_down1 = num_down1 + 1
    else:
        list_down_lane2 = ['down_l1', 'down_l2', 'down_l3', 'down_l4']
        dict_down_lane2 = {}
        for i in range(len(list_down_lane2)):
            dict_down_lane2[list_down_lane2[i]] = list2[i]
        #print(dict_down_lane2)
        data_down_lane2.append(dict_down_lane2)
        num_down2 = num_down2 + 1
print('下车道')
print('-------------------------------------------------------------------------')
print('双车道的数量：' + f'{num_down1}')
print('三车道的数量：' + f'{num_down2}')
print('-------------------------------------------------------------------------')
data_down_dic1 = data_up_dic1
data_down_dic2 = data_up_dic2
dic_down_1 = {}  # 双车道带名称字典
dic_down_2 = {}  # 三车道带名称字典
for i in range(len(data_down_dic1)):
    dic_down_1[data_down_dic1[i]] = data_down_lane1[i]
for i in range(len(data_down_dic2)):
    dic_down_2[data_down_dic2[i]] = data_down_lane2[i]
print('双车道（下）：' + f'{dic_down_1}')
print('三车道（下）：' + f'{dic_down_2}')
print('-------------------------------------------------------------------------')
print('\n')
# 跨道点判断：判断车辆轨迹是否与车道线相交


# 汽车航向角
#def f(x, y):  # 车辆航向角计算
    #return ((y + height / 2) ** t - (y + height / 2) ** (t - 3)) / ((x + width) ** t - (x + width) ** (t - 3))



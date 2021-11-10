import numpy as np
import math
import sys
import pandas as pd

# 处理时间t

# 上车道中线坐标

# 下车道中线坐标
for j in range(1, 61):
    str2 = str(j)
    path_recordingMeta = str2.zfill(2) + '_recordingMeta'
    print(path_recordingMeta)
    pathname_recordingMeta = 'E:/21_10_Control Transition/data/' + path_recordingMeta + '.csv'
    # print(pathname_recordingMeta)
    data_recordingMeta = pd.read_csv(pathname_recordingMeta)
    print(data_recordingMeta)
    locals()['col_' + path_recordingMeta] = data_recordingMeta["lowerLaneMarkings"]
    print(locals()['col_' + path_recordingMeta])
    locals()['data_' + path_recordingMeta] = np.array(locals()['col_' + path_recordingMeta])
    print(locals()['data_' + path_recordingMeta])
# 跨道点判断：判断车辆轨迹是否与车道线相交


# 汽车航向角
#def f(x, y):  # 车辆航向角计算
    #return ((y + height / 2) ** t - (y + height / 2) ** (t - 3)) / ((x + width) ** t - (x + width) ** (t - 3))



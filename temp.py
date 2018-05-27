import numpy as np
import pandas as pd
from math import sqrt
import time
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
# print(data_1.describe())


data_1 = pd.read_csv(open('c:/data/mm/2.csv'))
tim = data_1.ix[:, '时间']  # 2018042910515071 ,整型
tim = [int(time.mktime(time.strptime(str(t)[0:14], "%Y%m%d%H%M%S"))) for t in tim]  # 时间戳

print(tim)
head = ['时间戳']
df = pd.DataFrame(tim, columns=head)
df.to_csv("c:/data/mm/time.csv", encoding="utf-8", index = False)


# 处理R信息数据， 61.csv
data_61 = pd.read_csv(open('c:/data/mm/61.csv'))
#data_61.as_matrix(columns=None)

array_61 = np.asarray(data_61)
head = ['时间', '经度', '纬度', '传感器类型', 'RA_1_1', 'RA_1_2', 'RA_2_1',	'RA_2_2', 'RA_3_1',	'RA_3_2', 'RA_4_1', 'RA_4_2', '信号源批号	']
df = pd.DataFrame(array_61, columns=head)

df.to_csv('c:/data/mm/test.csv', index=False)

# 遍历各单元格，将多项数据求和处理
for i in range(len(array_61)):
    for j in range(len(array_61[i])):
        try:
            array_61[i][j] = float(sum(list([float(k) for k in array_61[i][j].split(',')])))
        except:
            pass

target_number = array_61[:, 13]
signal_number = array_61[:, 12]

start_list = []
end_list = []

start_list.append(0)
for i in range(len(signal_number) - 1):
    if signal_number[i] != signal_number[i + 1]:
        end_list.append(i)
        start_list.append(i + 1)

end_list.append(len(signal_number) - 1)

name_dic_r = {array_61[start_list[i], 12]: array_61[start_list[i], 13] for i in range(len(start_list))}


temp_r = []  # 按列求均
for i in range(len(start_list)):
    r_list = [sum(array_61[start_list[i]:end_list[i], 4]) / len(array_61[start_list[i]:end_list[i], 4]),
              sum(array_61[start_list[i]:end_list[i], 5]) / len(array_61[start_list[i]:end_list[i], 5]),
              sum(array_61[start_list[i]:end_list[i], 6]) / len(array_61[start_list[i]:end_list[i], 6]),
              sum(array_61[start_list[i]:end_list[i], 7]) / len(array_61[start_list[i]:end_list[i], 7]),
              sum(array_61[start_list[i]:end_list[i], 8]) / len(array_61[start_list[i]:end_list[i], 8]),
              sum(array_61[start_list[i]:end_list[i], 9]) / len(array_61[start_list[i]:end_list[i], 9]),
              sum(array_61[start_list[i]:end_list[i], 10]) / len(array_61[start_list[i]:end_list[i], 10]),
              sum(array_61[start_list[i]:end_list[i], 11]) / len(array_61[start_list[i]:end_list[i], 11])]
    temp_r.append(r_list)

target_R = {array_61[start_list[i], 12]: sum(temp_r[i]) for i in range(len(start_list))}









































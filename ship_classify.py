import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
import time

def get_database():
    # R
    data_41 = pd.read_csv(open('./data/41.csv'))  # R类信号源
    r_singal_name = data_41.ix[:, '信号源名称']
    r_1 = data_41.ix[:, 'RA_1_1']
    r_2 = data_41.ix[:, 'RA_1_2']
    r_3 = data_41.ix[:, 'RA_2_1']
    r_4 = data_41.ix[:, 'RA_2_2']
    r_5 = data_41.ix[:, 'RA_3_1']
    r_6 = data_41.ix[:, 'RA_3_2']
    r_7 = data_41.ix[:, 'RA_4_1']
    r_8 = data_41.ix[:, 'RA_4_2']
    r_all = [r_1, r_2, r_3, r_4, r_5, r_6, r_7, r_8]
    for i in r_all:
        for j in range(len(i)):
            try:
                i[j] = sum([float(k) for k in i[j].split(',')])
            except:
                pass
    R = {}  # 特征值：项和
    for i in range(len(r_singal_name)):
        R[r_singal_name[i]] = r_1[i] + r_2[i] + r_3[i] + r_4[i] + r_5[i] + r_6[i] + r_7[i] + r_8[i]
    # L1
    data_42 = pd.read_csv(open('./data/42.csv'))  # L1类信号源
    l1_singal_name = data_42.ix[:, '信号源名称']
    l1_1 = data_42.ix[:, 'L1A_1']
    l1_2 = data_42.ix[:, 'L1A_2']
    l1_3 = data_42.ix[:, 'L1A_3']
    l1_all = [l1_1, l1_2, l1_3]
    L1 = {}  # 特征值： 项和
    for i in range(len(l1_singal_name)):
        L1[l1_singal_name[i]] = l1_1[i] + l1_2[i] + l1_3[i]
    # L2
    data_43 = pd.read_csv(open('./data/43.csv'))  # L2类信号源
    l2_singal_name = data_43.ix[:, '信号源名称']
    l2_1 = data_43.ix[:, 'L2A_1']
    l2_2 = data_43.ix[:, 'L2A_2']
    l2_3 = data_43.ix[:, 'L2A_3']
    l2_all = [l2_1, l2_2, l2_3]
    L2 = {}  # 特征值：项和
    for i in range(len(l2_singal_name)):
        L2[l2_singal_name[i]] = l2_1[i] + l2_2[i] + l2_3[i]
    # A
    data_44 = pd.read_csv(open('./data/44.csv'))  # A类信号源
    a_singal_name = data_44.ix[:, '信号源名称']
    a_1 = data_44.ix[:, 'MMSI编号']
    A = {}  # 特征值：MMSI编号
    for i in range(len(a_singal_name)):
        A[a_singal_name[i]] = a_1[i]
    # 船舶
    data_3 = pd.read_csv(open('./data/3.csv'))  # 船舶携带信号种类
    ship_name = data_3.ix[:, '船舶名称']
    ship_number = data_3.ix[:, '船舶编号']
    ship_name_number_dic = {i: j for i, j in zip(ship_name,ship_number)}
    ship_number_name_dic = {j: i for i, j in ship_name_number_dic.items()}
    s_1 = data_3.ix[:, 'R类信号源1']
    s_2 = data_3.ix[:, 'R类信号源2']
    s_3 = data_3.ix[:, 'R类信号源3']
    s_4 = data_3.ix[:, 'LI1类信号源']
    s_5 = data_3.ix[:, 'L2类信号源']
    s_6 = data_3.ix[:, 'A类信号源']
    S = {}
    for i in range(len(ship_number)):
        S[ship_number[i]] = [s_1[i], s_2[i], s_3[i], s_4[i], s_5[i], s_6[i]]
    return R, L1, L2, A, S, ship_name_number_dic, ship_number_name_dic


R, L1, L2, A, S, ship_name_number_dic, ship_number_name_dic = get_database()  # 对比数据库

# 提取目标数据

## 处理R信息数据， 61.csv
data_61 = pd.read_csv(open('./data/61.csv'))
array_61 = np.asarray(data_61)


# 遍历各单元格，将多项数据求和处理
for i in range(len(array_61)):
    for j in range(len(array_61[i])):
        try:
            array_61[i][j] = float(sum(list([float(k) for k in array_61[i][j].split(',')])))
        except:
            pass

target_number_r = array_61[:, 13]
signal_number_r = array_61[:, 12]

start_list_r = []
end_list_r = []

start_list_r.append(0)
for i in range(len(signal_number_r) - 1):
    if signal_number_r[i] != signal_number_r[i + 1]:
        end_list_r.append(i)
        start_list_r.append(i + 1)

end_list_r.append(len(signal_number_r) - 1)

name_dic_r = {array_61[start_list_r[i], 12]: array_61[start_list_r[i], 13] for i in range(len(start_list_r))}


temp_r = []  # 按列求均
for i in range(len(start_list_r)):
    r_list = [sum(array_61[start_list_r[i]:end_list_r[i], 4]) / len(array_61[start_list_r[i]:end_list_r[i], 4]),
              sum(array_61[start_list_r[i]:end_list_r[i], 5]) / len(array_61[start_list_r[i]:end_list_r[i], 5]),
              sum(array_61[start_list_r[i]:end_list_r[i], 6]) / len(array_61[start_list_r[i]:end_list_r[i], 6]),
              sum(array_61[start_list_r[i]:end_list_r[i], 7]) / len(array_61[start_list_r[i]:end_list_r[i], 7]),
              sum(array_61[start_list_r[i]:end_list_r[i], 8]) / len(array_61[start_list_r[i]:end_list_r[i], 8]),
              sum(array_61[start_list_r[i]:end_list_r[i], 9]) / len(array_61[start_list_r[i]:end_list_r[i], 9]),
              sum(array_61[start_list_r[i]:end_list_r[i], 10]) / len(array_61[start_list_r[i]:end_list_r[i], 10]),
              sum(array_61[start_list_r[i]:end_list_r[i], 11]) / len(array_61[start_list_r[i]:end_list_r[i], 11])]
    temp_r.append(r_list)

target_R = {array_61[start_list_r[i], 12]: sum(temp_r[i]) for i in range(len(start_list_r))}

## 处理L1, 62.csv

data_62 = pd.read_csv(open('./data/62.csv'))
array_62 = np.asarray(data_62)

target_number_l1 = array_62[:, 8]
signal_number_l1 = array_62[:, 7]

start_list_l1 = []
end_list_l1 = []

start_list_l1.append(0)
for i in range(len(signal_number_l1) - 1):
    if signal_number_l1[i] != signal_number_l1[i + 1]:
        end_list_l1.append(i)
        start_list_l1.append(i + 1)

end_list_l1.append(len(signal_number_l1) - 1)

name_dic_l1 = {array_62[start_list_l1[i], 7]: array_62[start_list_l1[i], 8] for i in range(len(start_list_l1))}


temp_l1 = []  # 按列求均
for i in range(len(start_list_l1)):
    l1_list = [sum(array_62[start_list_l1[i]:end_list_l1[i], 4]) / len(array_62[start_list_l1[i]:end_list_l1[i], 4]),
              sum(array_62[start_list_l1[i]:end_list_l1[i], 5]) / len(array_62[start_list_l1[i]:end_list_l1[i], 5]),
              sum(array_62[start_list_l1[i]:end_list_l1[i], 6]) / len(array_62[start_list_l1[i]:end_list_l1[i], 6])]
    temp_l1.append(l1_list)

target_L1 = {array_62[start_list_l1[i], 7]: sum(temp_l1[i]) for i in range(len(start_list_l1))}

## 处理L2, 63.csv
data_63 = pd.read_csv(open('./data/63.csv'))
array_63 = np.asarray(data_63)

target_number_l2 = array_63[:, 8]
signal_number_l2 = array_63[:, 7]

start_list_l2 = []
end_list_l2 = []

start_list_l2.append(0)
for i in range(len(signal_number_l2) - 1):
    if signal_number_l2[i] != signal_number_l2[i + 1]:
        end_list_l2.append(i)
        start_list_l2.append(i + 1)

end_list_l2.append(len(signal_number_l2) - 1)

name_dic_l2 = {array_63[start_list_l2[i], 7]: array_63[start_list_l2[i], 8] for i in range(len(start_list_l2))}


temp_l2 = []  # 按列求均
for i in range(len(start_list_l2)):
    l2_list = [sum(array_63[start_list_l2[i]:end_list_l2[i], 4]) / len(array_63[start_list_l2[i]:end_list_l2[i], 4]),
              sum(array_63[start_list_l2[i]:end_list_l2[i], 5]) / len(array_63[start_list_l2[i]:end_list_l2[i], 5]),
              sum(array_63[start_list_l2[i]:end_list_l2[i], 6]) / len(array_63[start_list_l2[i]:end_list_l2[i], 6])]
    temp_l2.append(l2_list)

target_L2 = {array_63[start_list_l2[i], 7]: sum(temp_l2[i]) for i in range(len(start_list_l2))}

## 处理A, 64.csv
data_64 = pd.read_csv(open('./data/64.csv'))


signal_number_4 = data_64.ix[:, '信号源批号']
target_number_4 = data_64.ix[:, '目标编号']
name_dic_a = {i: j for i, j in zip(signal_number_4, target_number_4)}

target_a_1 = data_64.ix[:, 'MMSI编号']

target_A = {}  # 特征值：MMSI编号

for i in range(len(signal_number_4)):
    target_A[signal_number_4[i]] = target_a_1[i]


# 目标分类 30，4，2
features = [target_R, target_L1, target_L2, target_A]

## 检测R
r_result = []
for number, r_value in target_R.items():
    exist_r_signal = []
    for r_name, r_real_value in R.items():
        if abs(r_value - r_real_value) <= 30:
            exist_r_signal.append(r_name)
    exist_r_signal = list(set(exist_r_signal))  # 剔除重复
    exist_ship_number = []
    for i in exist_r_signal:
        for s_number, s_signals in S.items():
            for signal in s_signals:
                if i == signal:
                    exist_ship_number.append(s_number)
    exist_ship_number = list(set(exist_ship_number))
    r_result.append(exist_ship_number)

r_number_result_dic = {i: j for i, j in zip([i for i, j in name_dic_r.items()], r_result)}
# refer to name_dic_r

## 检测L1
l1_result = []
for number, l1_value in target_L1.items():
    exist_l1_signal = []
    for l1_name, l1_real_value in L1.items():
        if abs(l1_value - l1_real_value) <= 4:
            exist_l1_signal.append(l1_name)
    exist_l1_signal = list(set(exist_l1_signal))  # 剔除重复
    exist_ship_number = []
    for i in exist_l1_signal:
        for s_number, s_signals in S.items():
            for signal in s_signals:
                if i == signal:
                    exist_ship_number.append(s_number)
    exist_ship_number = list(set(exist_ship_number))
    l1_result.append(exist_ship_number)

l1_number_result_dic = {i: j for i, j in zip([i for i, j in name_dic_l1.items()], l1_result)}
# refer to name_dic_l1


## 检测L2
l2_result = []
for number, l2_value in target_L2.items():
    exist_l2_signal = []
    for l2_name, l2_real_value in L2.items():
        if abs(l2_value - l2_real_value) <= 2:
            exist_l2_signal.append(l2_name)
    exist_l2_signal = list(set(exist_l2_signal))  # 剔除重复
    exist_ship_number = []
    for i in exist_l2_signal:
        for s_number, s_signals in S.items():
            for signal in s_signals:
                if i == signal:
                    exist_ship_number.append(s_number)
    exist_ship_number = list(set(exist_ship_number))
    l2_result.append(exist_ship_number)

l2_number_result_dic = {i: j for i, j in zip([i for i, j in name_dic_l2.items()], l2_result)}
# refer to name_dic_l2

## 检测A
a_result = []
for number, a_value in target_A.items():
    exist_a_signal = []
    for a_name, a_real_value in A.items():
        if a_value == a_real_value:
            exist_a_signal.append(a_name)
    exist_a_signal = list(set(exist_a_signal))  # 剔除重复
    exist_ship_number = []
    for i in exist_a_signal:
        for s_number, s_signals in S.items():
            for signal in s_signals:
                if i == signal:
                    exist_ship_number.append(s_number)
    exist_ship_number = list(set(exist_ship_number))
    a_result.append(exist_ship_number)

a_number_result_dic = {i: j for i, j in zip([i for i, j in name_dic_a.items()], a_result)}
# refer to name_dic_a

#  按目标编号取交集
target_number = list(set(list([j for i, j in name_dic_r.items()]) + list([j for i, j in name_dic_l1.items()]) + list([j for i, j in name_dic_l2.items()]) + list([j for i, j in name_dic_a.items()])))
number_result_dic = {**r_number_result_dic, **l1_number_result_dic, **l2_number_result_dic, **a_number_result_dic}
name_dic = {**name_dic_r, **name_dic_l1, **name_dic_l2, **name_dic_a}

name_number_dic = {}  # 目标: [信号源]
for i in target_number:
    name_number_dic[i] = []
    for j, k in name_dic.items():
        if i == k:
            name_number_dic[i].append(j)

final_result = {}
for i, j in name_number_dic.items():
    final_result[i] = []
    for k in j:
        if number_result_dic[k] != []:final_result[i].append(number_result_dic[k])
        #continue


intersection = 1
for i, j in final_result.items():
    # intersection = None
    if len(j) > 1:
        for k in range(len(j) - 1):
            intersection = set(j[k]) & set(j[k + 1])
        final_result[i] = list(intersection)
    else:
        final_result[i] = final_result[i][0]

final_result_number = final_result
print('按船舶编号输出的分类结果：')
print(final_result_number)

final_result_name = final_result
for i, j in final_result_name.items():
    for k in range(len(j)):
        final_result_name[i][k] = ship_number_name_dic[j[k]]

print('按船舶名称输出的分类结果：')
print(final_result_name)

print('程序运行结束，15秒后自动关闭窗口。')
time.sleep(15)


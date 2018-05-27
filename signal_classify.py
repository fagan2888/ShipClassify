import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
import time

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

r_values = [j for i, j in R.items()]
r_values.sort()
plt.plot(r_values)
plt.xlabel('R信号种类')
plt.ylabel('特征值')
plt.title('R类信号源中25种特征值对比（升序）')
plt.legend(loc='best')
plt.show()

diff_r_values = []
for i in range(len(r_values) - 1):
    diff_r_values.append(abs(r_values[i + 1] - r_values[i]))

diff_r_values.sort()
print(diff_r_values)

plt.plot(diff_r_values)
plt.xlabel('R信号种类')
plt.ylabel('特征值差值')
plt.title('R类信号源中25种特征值相差值对比（最小的24个差值升序排列）')
plt.legend(loc='best')
plt.show()

head = ['差值']
df = pd.DataFrame(diff_r_values, columns=head)
df.to_csv("./data/R类信号源中24种特征值相差值对比（最小的24个差值升序排列）.csv", encoding="utf-8", index = False)

# L1
data_42 = pd.read_csv(open('./data/42.csv'))  # L1类信号源
l1_singal_name = data_42.ix[:, '信号源名称']
l1_1 = data_42.ix[:, 'L1A_1']
l1_2 = data_42.ix[:, 'L1A_2']
l1_3 = data_42.ix[:, 'L1A_3']

l1_all = [l1_1, l1_2, l1_3]

L1 = {}  # 特征值：项和

for i in range(len(l1_singal_name)):
    L1[l1_singal_name[i]] = l1_1[i] + l1_2[i] + l1_3[i]

l1_values = [j for i, j in L1.items()]
l1_values.sort()
plt.plot(l1_values)
plt.xlabel('L1信号种类')
plt.ylabel('特征值')
plt.title('L1类信号源中21种特征值对比（升序）')
plt.legend(loc='best')
plt.show()


diff_l1_values = []
for i in range(len(l1_values) - 1):
    diff_l1_values.append(abs(l1_values[i + 1] - l1_values[i]))

diff_l1_values.sort()

plt.plot(diff_l1_values)
plt.xlabel('L1信号种类')
plt.ylabel('特征值差值')
plt.title('L1类信号源中21种特征值相差值对比（最小的20个差值升序排列）')
plt.legend(loc='best')
plt.show()

head = ['差值']
df = pd.DataFrame(diff_l1_values, columns=head)
df.to_csv("./data/L1类信号源中21种特征值相差值对比（最小的20个差值升序排列）.csv", encoding="utf-8", index = False)


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

l2_values = [j for i, j in L2.items()]
l2_values.sort()
plt.plot(l2_values)
plt.xlabel('L2信号种类')
plt.ylabel('特征值')
plt.title('L2类信号源中21种特征值对比（升序）')
plt.legend(loc='best')
plt.show()


diff_l2_values = []
for i in range(len(l2_values) - 1):
    diff_l2_values.append(abs(l2_values[i + 1] - l2_values[i]))

diff_l2_values.sort()

plt.plot(diff_l2_values)
plt.xlabel('L2信号种类')
plt.ylabel('特征值差值')
plt.title('L2类信号源中21种特征值相差值对比（最小的20个差值升序排列）')
plt.legend(loc='best')
plt.show()

head = ['差值']
df = pd.DataFrame(diff_l2_values, columns=head)
df.to_csv("./data/L2类信号源中21种特征值相差值对比（最小的20个差值升序排列）.csv", encoding="utf-8", index = False)


# A
data_44 = pd.read_csv(open('./data/44.csv'))  # A类信号源
a_singal_name = data_44.ix[:, '信号源名称']
a_1 = data_44.ix[:, 'MMSI编号']

A = {}  # 特征值：MMSI编号

for i in range(len(a_singal_name)):
    A[a_singal_name[i]] = a_1[i]


#  船舶
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


#  待分类目标
data_51 = pd.read_csv(open('./data/51.csv'))  # 目标R类信号源
data_52 = pd.read_csv(open('./data/52.csv'))  # 目标L1类信号源
data_53 = pd.read_csv(open('./data/53.csv'))  # 目标L2类信号源
data_54 = pd.read_csv(open('./data/54.csv'))  # 目标A类信号源

##  读取R信号特征值
signal_number_1 = data_51.ix[:, '信号源批号']
target_number_1 = data_51.ix[:, '目标编号']
name_dic_r = {i: j for i, j in zip(signal_number_1, target_number_1)}

target_r_1 = data_51.ix[:, 'RA_1_1']
target_r_2 = data_51.ix[:, 'RA_1_2']
target_r_3 = data_51.ix[:, 'RA_2_1']
target_r_4 = data_51.ix[:, 'RA_2_2']
target_r_5 = data_51.ix[:, 'RA_3_1']
target_r_6 = data_51.ix[:, 'RA_3_2']
target_r_7 = data_51.ix[:, 'RA_4_1']
target_r_8 = data_51.ix[:, 'RA_4_2']

target_r_all = [target_r_1, target_r_2, target_r_3, target_r_4, target_r_5, target_r_6, target_r_7, target_r_8]

for i in target_r_all:
    for j in range(len(i)):
        try:
            i[j] = sum([float(k) for k in i[j].split(',')])
        except:
            pass

target_R = {}  # 特征值：项和

for i in range(len(signal_number_1)):
    target_R[signal_number_1[i]] = target_r_1[i] + target_r_2[i] + target_r_3[i] + target_r_4[i] + target_r_5[i] + target_r_6[i] + target_r_7[i] + target_r_8[i]

## 读取L1信号特征值
signal_number_2 = data_52.ix[:, '信号源批号']
target_number_2 = data_52.ix[:, '目标编号']
name_dic_l1 = {i: j for i, j in zip(signal_number_2, target_number_2)}

target_l1_1 = data_52.ix[:, 'L1A_1']
target_l1_2 = data_52.ix[:, 'L1A_2']
target_l1_3 = data_52.ix[:, 'L1A_3']

target_L1 = {}  # 特征值：项和

for i in range(len(signal_number_2)):
    target_L1[signal_number_2[i]] = target_l1_1[i] + target_l1_2[i] + target_l1_3[i]

## 读取L2信号特征值
signal_number_3 = data_53.ix[:, '信号源批号']
target_number_3 = data_53.ix[:, '目标编号']
name_dic_l2 = {i: j for i, j in zip(signal_number_3, target_number_3)}

target_l2_1 = data_53.ix[:, 'L2A_1']
target_l2_2 = data_53.ix[:, 'L2A_2']
target_l2_3 = data_53.ix[:, 'L2A_3']

target_L2 = {}  # 特征值：项和

for i in range(len(signal_number_3)):
    target_L2[signal_number_3[i]] = target_l2_1[i] + target_l2_2[i] + target_l2_3[i]

## 读取A信号特征值
signal_number_4 = data_54.ix[:, '信号源批号']
target_number_4 = data_54.ix[:, '目标编号']
name_dic_a = {i: j for i, j in zip(signal_number_4, target_number_4)}

target_a_1 = data_54.ix[:, 'MMSI编号']

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

r_number_result_dic = {i: j for i, j in zip(signal_number_1, r_result)}
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

l1_number_result_dic = {i: j for i, j in zip(signal_number_2, l1_result)}
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

l2_number_result_dic = {i: j for i, j in zip(signal_number_3, l2_result)}
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

a_number_result_dic = {i: j for i, j in zip(signal_number_4, a_result)}
# refer to name_dic_a

#  按目标编号取交集
target_number = list(set(list(target_number_1) + list(target_number_2) + list(target_number_3) + list(target_number_4)))
number_result_dic = {**r_number_result_dic, **l1_number_result_dic, **l2_number_result_dic, **a_number_result_dic}
name_dic = {**name_dic_r, **name_dic_l1, **name_dic_l2, **name_dic_a}

name_number_dic = {}  # 101: [1011, 1012, 1013, 1014, 1015]
for i in target_number:
    name_number_dic[i] = []
    for j, k in name_dic.items():
        if i == k:
            name_number_dic[i].append(j)

final_result = {}  # {目标编号：[[],[],[]]}
for i, j in name_number_dic.items():
    final_result[i] = []
    for k in j:
        if number_result_dic[k] != []:final_result[i].append(number_result_dic[k])



intersection = 1
for i, j in final_result.items():
    if len(j) > 1:
    # intersection = None
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

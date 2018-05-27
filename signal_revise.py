import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号


data_1 = pd.read_csv(open('./data/1.csv'))
L1A_1 = data_1.ix[:, 'L1A_1']  # 12，13，16，13
L1A_2 = data_1.ix[:, 'L1A_2']
L1A_3 = data_1.ix[:, 'L1A_3']

singal_1, singal_2, singal_3, singal_4 = L1A_1[0:12], L1A_1[12:25], L1A_1[25:41], L1A_1[41:54]
singal_5, singal_6, singal_7, singal_8 = L1A_2[0:12], L1A_2[12:25], L1A_2[25:41], L1A_2[41:54]
singal_9, singal_10, singal_11, singal_12 = L1A_3[0:12], L1A_3[12:25], L1A_3[25:41], L1A_3[41:54]


def revise(x):
    new_x = []
    x = list(x)
    new_x.append(x[0])
    new_x.append(x[1])
    for i in range(len(x) - 2):
        s = 0
        for j in range(i + 2 + 1):
            s += x[j]
        new_x.append(s / (i + 2 + 1))
    return new_x


def evaluate(x):
    return np.var(np.array(x))


new_singal_1 = revise(singal_1)
new_singal_2 = revise(singal_2)
new_singal_3 = revise(singal_3)
new_singal_4 = revise(singal_4)
new_singal_5 = revise(singal_5)
new_singal_6 = revise(singal_6)
new_singal_7 = revise(singal_7)
new_singal_8 = revise(singal_8)
new_singal_9 = revise(singal_9)
new_singal_10 = revise(singal_10)
new_singal_11 = revise(singal_11)
new_singal_12 = revise(singal_12)


e_1, new_e_1 = evaluate(singal_1), evaluate(new_singal_1)
e_2, new_e_2 = evaluate(singal_2), evaluate(new_singal_2)
e_3, new_e_3 = evaluate(singal_3), evaluate(new_singal_3)
e_4, new_e_4 = evaluate(singal_4), evaluate(new_singal_4)
e_5, new_e_5 = evaluate(singal_5), evaluate(new_singal_5)
e_6, new_e_6 = evaluate(singal_6), evaluate(new_singal_6)
e_7, new_e_7 = evaluate(singal_7), evaluate(new_singal_7)
e_8, new_e_8 = evaluate(singal_8), evaluate(new_singal_8)
e_9, new_e_9 = evaluate(singal_9), evaluate(new_singal_9)
e_10, new_e_10 = evaluate(singal_10), evaluate(new_singal_10)
e_11, new_e_11 = evaluate(singal_11), evaluate(new_singal_11)
e_12, new_e_12 = evaluate(singal_12), evaluate(new_singal_12)


print(e_1, new_e_1)
print(e_2, new_e_2)
print(e_3, new_e_3)
print(e_4, new_e_4)
print(e_5, new_e_5)
print(e_6, new_e_6)
print(e_7, new_e_7)
print(e_8, new_e_8)
print(e_9, new_e_9)
print(e_10, new_e_10)
print(e_11, new_e_11)
print(e_12, new_e_12)

plt.plot([e_1, e_2, e_3, e_4, e_5, e_6, e_7, e_8, e_9, e_10, e_11, e_12], label='修正前特征信号均方误差')
plt.plot([new_e_1, new_e_2, new_e_3, new_e_4, new_e_5, new_e_6, new_e_7, new_e_8, new_e_9, new_e_10, new_e_11, new_e_12], label='修正后特征信号均方误差')
plt.xlabel('编号')
plt.ylabel('方差数值')
plt.title('十二种信号修正前后均方误差对比')
plt.legend(loc='best')

plt.show()

import numpy as np
import pandas as pd
from math import sqrt
import time
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
# print(data_1.describe())


# 最小二乘回归
def least_squares(x, y):
    x_ = x.mean()
    y_ = y.mean()
    m = np.zeros(1)
    n = np.zeros(1)
    k = np.zeros(1)
    p = np.zeros(1)
    for i in np.arange(len(x)):
        k = (x[i]-x_) * (y[i]-y_)
        m += k
        p = np.square(x[i]-x_)
        n = n + p
    a = m / n
    b = y_ - a * x_
    return a[0], b[0]


# 北纬26°上相邻经线圈相距100.053km，经线圈上相邻纬线圈相距111.600km

# 数值修正
def revise(x, y, t):
    x = np.array(x)
    y = np.array(y)
    new_x = []
    new_y = []
    new_x.append(x[0])
    new_x.append(x[1])
    new_y.append(y[0])
    new_y.append(y[1])
    for i in range(len(x) - 2):
        speed = sqrt(((x[i + 2] - x[i + 2 - 1]) * 100053)**2 + ((y[i + 2] - y[i + 2 - 1]) * 111600)**2) / (t[i + 2] - t[i + 1])
        print('航行速度：', speed, 'm/s')
        k, b = least_squares(x[0:i + 2], y[0:i + 2])
        x_ = new_x[i + 2 - 1] - sqrt((speed * (t[i + 2] - t[i + 2 -1]))**2 / (k**2 + 1)) / 100053
        y_ = new_y[i + 2 - 1] - sqrt((speed * (t[i + 2] - t[i + 2 -1]))**2 / (k**2 + 1)) * k / 111600
        new_x.append((x_ + x[i + 2]) / 2)
        new_y.append((y_ + y[i + 2]) / 2)
    return new_x, new_y


def compare(x, y, new_x, new_y, title_name):
    plt.plot(new_x, new_y, label='修正轨迹')
    plt.plot(x, y, label='原始轨迹')
    plt.legend(loc='best')
    plt.xlabel('经度')
    plt.ylabel('纬度')
    plt.title(title_name)
    plt.show()


# 残差平方和评估：数据与拟合直线残差平方和
def evaluate(x, y):
    x = np.array(x)
    y = np.array(y)
    k, b = least_squares(x, y)
    # print('k, b:', k, b)
    diff_list = x * k + b - y
    # print(diff_list)
    sum_square = 0
    for i in diff_list:
        sum_square += i ** 2
    return sum_square / len(x)


data_1 = pd.read_csv(open('./data/1.csv'))
lon = data_1.ix[:, '经度']  # 12，13，16，13
lat = data_1.ix[:, '纬度']
tim = data_1.ix[:, '时间']  # 2018042910515071 ,整型
tim = [int(time.mktime(time.strptime(str(t)[0:14], "%Y%m%d%H%M%S"))) for t in tim]  # 时间戳

lon_1, lat_1, t_1 = lon[0:12], lat[0:12], tim[0:12]
lon_2, lat_2, t_2 = lon[12:25], lat[12:25], tim[12:25]  # straight
lon_3, lat_3, t_3 = lon[25:41], lat[25:41], tim[25:41]
lon_4, lat_4, t_4 = lon[41:54], lat[41:54], tim[41:54]

new_lon_1, new_lat_1 = revise(lon_1, lat_1, t_1)
new_lon_2, new_lat_2 = revise(lon_2, lat_2, t_2)
new_lon_3, new_lat_3 = revise(lon_3, lat_3, t_3)
new_lon_4, new_lat_4 = revise(lon_4, lat_4, t_4)

compare(lon_1, lat_1, new_lon_1, new_lat_1, '信号源一原始轨迹和修正轨迹对比')
compare(lon_2, lat_2, new_lon_2, new_lat_2, '信号源二原始轨迹和修正轨迹对比')
compare(lon_3, lat_3, new_lon_3, new_lat_3, '信号源三原始轨迹和修正轨迹对比')
compare(lon_4, lat_4, new_lon_4, new_lat_4, '信号源四原始轨迹和修正轨迹对比')

evaluate(lon_1[2:], lat_1[2:]), evaluate(new_lon_1[2:], new_lat_1[2:])
evaluate(lon_2[2:], lat_2[2:]), evaluate(new_lon_2[2:], new_lat_2[2:])
evaluate(lon_3[2:], lat_3[2:]), evaluate(new_lon_3[2:], new_lat_3[2:])
evaluate(lon_4[2:], lat_4[2:]), evaluate(new_lon_4[2:], new_lat_4[2:])


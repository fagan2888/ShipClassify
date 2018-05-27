#coding:utf-8
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False  # 用来正常显示负号
import time


data_1 = pd.read_csv(open('./data/1.csv'))
# print(data_1.describe())

lon = data_1.ix[:, '经度']  # 12，13，16，13
lat = data_1.ix[:, '纬度']
tim = data_1.ix[:, '时间']  # 2018042910515071

tim = [int(time.mktime(time.strptime(str(t)[0:14], "%Y%m%d%H%M%S"))) for t in tim]  # 整型 -> 时间戳

plt.plot(lon[0:12], lat[0:12], label='信号源一航行轨迹')
plt.plot(lon[12:25], lat[12:25], label='信号源二航行轨迹')  # straight
plt.plot(lon[25:41], lat[25:41], label='信号源三航行轨迹')
plt.plot(lon[41:54], lat[41:54], label='信号源四航行轨迹')
plt.legend(loc='best')
plt.xlabel(u'经度')
plt.ylabel(u'纬度')
plt.title(u'附录一数据中四种信号源航行轨迹')
plt.show()

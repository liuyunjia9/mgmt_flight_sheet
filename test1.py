import matplotlib.pyplot as plt
import matplotlib.dates as mdate
plt.rcParams['font.sans-serif']=['Microsoft YaHei']    #指定默认字体
plt.rcParams['axes.unicode_minus']=False   #用来正常显示负号
p1 = plt.barh(df['姓名'],df['天数'],0.8,df['起始日期'])
plt.gca().xaxis.set_major_formatter(mdate.DateFormatter('%m-%d'))
plt.bar_label(p1,labels=df['航线'],label_type='center',fontsize=5)
plt.yticks(fontsize=5)
plt.xticks(fontsize=5)
plt.gcf().savefig('../testblueline.jpg',dpi= 1000)
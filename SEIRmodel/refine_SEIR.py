import scipy.integrate as spi
import numpy as np
import matplotlib.pyplot as plt
import math



#基础数据：需要扒取
# I_0为感染者的初始人数 524*1.5
I_0 = 109
# E_0为潜伏者的初始人数
E_0 = 223
# R_0为治愈者的初始人数
R_0 = 4
# S_0为易感者的初始人数
# S_0 = N - I_0 - E_0 - R_0
S_0=21536000
# Sq 隔离易感染者
S_q=1000
# Eq隔离潜伏者
E_q=200
# H住院患者
H=I_0+E_q
# T为传播时间/周期（可以更改）
T = 35


#以下需配置（来源WHO）
#θ潜伏者相对感染者传播能力的比值-假设潜伏期患者与已经表现出症状的患者传染能力相同
cita=1
#γ隔离接触速率-隔离14天
gamma=1/14
# σ潜伏者向感染者转化速率 潜伏期7天
sigama=1/7
# α病死率----需基于实际死亡人数进行调整
alpha=0.013
# δI感染者隔离速率
delta_I=0.13
# γI感染者恢复速率
gamma_I=0.043
# δq 隔离潜伏者向隔离感染者的转化速率
delta_q=0.013
# γH隔离感染者的恢复速率
gamma_H=0.043
# β 传染概率
beta = 3.3*math.pow(10,-9)
# q 隔离比例
q=59*math.pow(10,-6)
#λ隔离解除速率
lamada=1/14

# 防控等级影响配置，分为低、中、高
# c 接触率（低时c最大，高时c最小）也可以考虑人口密度等
c=2.9
# ρ有效接触系数（低时无系数或系数为1，高时系数<0）
rou=1
#ρc有效接触率



# INI为初始状态下的数组
INI = (S_0,E_0,I_0,R_0,S_q,E_q,H)


def funcSEIR(inivalue,_):
    Y = np.zeros(7)
    X = inivalue
    Y[0] = -(rou*c*beta+rou*c*q*(1-beta))*X[0]*(X[2]+cita*X[1])+lamada*X[4]
    Y[1] = rou*c*beta*(1-q)*X[0]*(X[2]+cita*X[1])-sigama*X[1]
    Y[2] = sigama*X[1]-(delta_I+alpha+gamma_I)*X[2]
    Y[3] = rou*c*q*(1-beta)*X[0]*(X[2]+cita*X[1])-lamada*X[4]
    Y[4] = rou*c*beta*q*X[0]*(X[2]+cita*X[1])-delta_I*X[4]
    Y[5] = delta_I*X[2]+delta_q*X[5]-(alpha+gamma_H)*X[6]
    Y[6] = gamma_I*X[2]+gamma_H*X[6]
    return Y

T_range = np.arange(0,T + 1)
RES = spi.odeint(funcSEIR,INI,T_range)

#显示中文
plt.rcParams['font.sans-serif']=['SimHei']
plt.plot(RES[:,2],color = 'red',label = '模拟感染人数',marker = '.')




plt.title('北京')
plt.legend()
plt.xlabel('天数')
plt.ylabel('人数')
plt.show()

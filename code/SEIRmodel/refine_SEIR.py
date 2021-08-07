import scipy.integrate as spi
import numpy as np
import matplotlib.pyplot as plt
import math


class SEIR():
    def __init__(self, N_i, I_i, R_i, S_qi, E_qi, T_i, risk, contact_rate):
        # 基础数据：需要扒取
        # I_0为感染者的初始人数 524*1.5
        self.I_0 = I_i
        # E_0为潜伏者的初始人数
        self.E_0 = self.I_0
        # R_0为治愈者的初始人数
        self.R_0 = R_i
        # S_0为易感者的初始人数
        self.S_0 = N_i - self.I_0 - self.E_0 - self.R_0
        # S_0=21536000
        # Sq 隔离易感染者
        self.S_q = S_qi
        # Eq隔离潜伏者
        self.E_q = E_qi
        # H住院患者
        self.H = self.I_0 + self.E_q
        # T为传播时间/周期（可以更改/配置）
        self.T = T_i
        # c 接触率（低时c最大，高时c最小）也可以考虑人口密度等
        self.c = risk
        # ρ有效接触系数（低时无系数或系数为1，高时系数<0）
        self.rou = contact_rate
        self.T_range = np.arange(0, self.T + 1)
        self.INI = (self.S_0, self.E_0, self.I_0, self.R_0, self.S_q, self.E_q, self.H)

    def funcSEIR(self, inivalue, _):
        # 以下需配置（来源WHO）
        # θ潜伏者相对感染者传播能力的比值-假设潜伏期患者与已经表现出症状的患者传染能力相同
        cita = 1
        # σ潜伏者向感染者转化速率 潜伏期7天
        sigama = 1 / 7
        # α病死率----需基于实际死亡人数进行调整
        alpha = 0.013
        # δI感染者隔离速率
        delta_I = 0.13
        # γI感染者恢复速率
        gamma_I = 0.043
        # δq 隔离潜伏者向隔离感染者的转化速率
        delta_q = 0.013
        # γH隔离感染者的恢复速率
        gamma_H = 0.043
        # β 传染概率
        beta = 3.3 * math.pow(10, -9)
        # q 隔离比例
        q = 59 * math.pow(10, -6)
        # λ隔离解除速率
        lamada = 1 / 14

        Y = np.zeros(7)
        X = inivalue
        # S_0
        Y[0] = -(self.rou * self.c * beta + self.rou * self.c * q * (1 - beta)) \
               * X[0] * (X[2] + cita * X[1]) + lamada * X[4]
        # E_0
        Y[1] = self.rou * self.c * beta * (1 - q) * X[0] * (X[2] + cita * X[1]) - sigama * X[1]
        # I_0
        Y[2] = sigama * X[1] - (delta_I + alpha + gamma_I) * X[2]
        # R_0
        Y[3] = self.rou * self.c * q * (1 - beta) * X[0] * (X[2] + cita * X[1]) - lamada * X[4]
        # S_q
        Y[4] = self.rou * self.c * beta * q * X[0] * (X[2] + cita * X[1]) - delta_I * X[4]
        # E_q
        Y[5] = delta_I * X[2] + delta_q * X[5] - (alpha + gamma_H) * X[6]
        # H
        Y[6] = gamma_I * X[2] + gamma_H * X[6]
        return Y

    def result(self):
        return spi.odeint(self.funcSEIR, self.INI, self.T_range)

    def predict(self):
        RES = self.result()
        return RES[:, 2]


if __name__ == '__main__':
    X = SEIR(21536000, 22, 4, 100, 200, 60, 0.5, 0.1)
    # INI为初始状态下的数组
    pred = X.predict()

    # 显示中文
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.plot(pred, color='red', label='模拟感染人数', marker='.')

    plt.title('北京')
    plt.legend()
    plt.xlabel('天数')
    plt.ylabel('人数')
    plt.show()

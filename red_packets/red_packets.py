#!/usr/bin/env
# -*- coding: UTF-8 -*-

# method 1
# 方法1：二倍均值法


# 剩余红包金额为M，剩余人数为N，那么有如下公式：

# 每次抢到的金额 = 随机区间 （0， M / N X 2）

# 这个公式，保证了每次随机金额的平均值是相等的，不会因为抢红包的先后顺序而造成不公平。

# 举个栗子：

# 假设有10个人，红包总额100元。

# 100/10X2 = 20, 所以第一个人的随机范围是（0，20 )，平均可以抢到10元。

# 假设第一个人随机到10元，那么剩余金额是100-10 = 90 元。

# 90/9X2 = 20, 所以第二个人的随机范围同样是（0，20 )，平均可以抢到10元。

# 假设第二个人随机到10元，那么剩余金额是90-10 = 80 元。

# 80/8X2 = 20, 所以第三个人的随机范围同样是（0，20 )，平均可以抢到10元。

# 以此类推，每一次随机范围的均值是相等的。

import random

# total money
M = 100
# numbers of peaple
N = 10

def getMoney(m, n):
    packets = list()
    for i in range(n - 1):
        # random range start and end
        start = 0
        end = (m - 10 * i) / (10 - i) * 2
        # everyone get money
        money = random.randrange(start=start, stop=int(end))
        packets.append(money)
    packets.append(m - sum(packets))
    return packets


def output(packets):
    for i, money in enumerate(packets):
        print("person ", i + 1, " get ", money)

if __name__ == "__main__":
    packets = getMoney(M, N)
    output(packets)
    
"""
在满足背包最大重量的前提下，求背包中物品总重量。
"""
import sys

# 回溯法
maxW = 0
w = [2,2,4,6,3]
n = 5
bagMaxW = 9
# 可以增加备忘录，减少重复计算
mem = [[False for i in range(bagMaxW + 1)] for i in range(n)]

# i,第几个物品
# 加入时，当前重量
def getMaxW(i, cw):
    global maxW
    global mem
    if cw == bagMaxW or i == n:
        if cw > maxW: maxW = cw
        return

    if mem[i][cw] == True: return
    mem[i][cw] = True

    getMaxW(i+1, cw)
    if cw + w[i] <= bagMaxW:
        getMaxW(i+1, cw + w[i])

getMaxW(0, 0)
print(maxW)

#动态规划
def knapsack():
    # 状态转移表
    states = [[False for i in range(bagMaxW + 1)] for i in range(n)]
    states[0][0] = True
    states[0][w[0]] = True
    for i in range(n):
        for j in range(bagMaxW + 1):
            if states[i-1][j] == True:
                states[i][j] = True
        for j in range(bagMaxW + 1 - w[i]):
            if states[i-1][j] == True:
                states[i][j + w[i]] = True

    for i in range(bagMaxW, -1, -1):
        if states[n-1][i]:
            return i
    return 0

print(knapsack())

# 可以用一维数组实现。因为后一行一定包含前一行的情况
def knapsack1():
    states = [False for i in range(bagMaxW + 1)]
    states[0] = True
    states[w[0]] = True
    for i in range(1, n):
        for j in range(bagMaxW - w[i], -1, -1):
            if states[j]:
                states[j + w[i]] = True

        # 从小到大遍历，会有重复计算。
        # for j in range(bagMaxW - w[i]):
        #     if states[j]:
        #         states[j + w[i]] = True

    for i in range(bagMaxW, -1, -1):
        if states[i]:
            return i
    return 0

print(knapsack1())

# 增加物品的价值因数，求在满足最大重量限制下，价值的最大值
value = [3,4,8,9,6]
maxV = 0

# 回溯法
def kanpsack2_recall(i, cw, cv):
    global maxV
    if cw == bagMaxW or i == n: # cw==w 表示装满了，i==n 表示物品都考察完了
        if cv > maxV: maxV = cv
        return

    kanpsack2_recall(i+1, cw, cv) # 选择不装第 i 个物品
    if cw + w[i] <= bagMaxW:
        kanpsack2_recall(i+1, cw + w[i], cv + value[i]) # 选择装第 i 个物品

kanpsack2_recall(0, 0, 0)
print(maxV)

# 动态规划
def kanpsack2():
    states = [[-1 for i in range(bagMaxW + 1)] for i in range(n)]

    states[0][0] = 0
    states[0][w[0]] = value[0]

    for i in range(1, n):
        # 不选择第 i 个物品
        for j in range(bagMaxW + 1):
            if states[i-1][j] >= 0:
                states[i][j] = states[i-1][j]

        # 选择第 i 个物品
        for j in range(bagMaxW - w[i] + 1):
            if states[i-1][j] >= 0:
                v = states[i-1][j] + value[i]
                if v > states[i-1][j + w[i]]:
                    states[i][j + w[i]] = v

    # 找出最大值
    curMaxV = 0
    for i in range(bagMaxW + 1):
        if states[n-1][i] > curMaxV:
            curMaxV = states[n-1][i]

    return curMaxV

print("kanpsack2: ", kanpsack2())

# 双11，满200减50
items = [32, 12, 45, 33, 55, 100, 87]
n = 7
maxM = 200
def double11():
    # 超过 3 倍就没有薅羊毛的价值了
    states = [[False for i in range(3*maxM + 1)] for i in range(n)]
    states[0][0] = True
    states[0][items[0]] = True

    # 不购买第 i 个商品
    for i in range(1, n):
        for j in range(3*maxM + 1):
            if states[i-1][j]: states[i][j] = True

    # 购买第 i 个商品
    for i in range(1, n):
        for j in range(3*maxM + 1 - items[i]):
            if states[i-1][j]: states[i][j + items[i]] = True

    maxSum = -1
    # 找到输出结果大于等于 maxM 的最小值
    for i in range(maxM, maxM*3 + 1):
        if states[n-1][i]:
            maxSum = i
            break

    if maxSum == -1: return # 没有满足200的额度的

    for i in range(n-1, 0, -1):
        if maxSum - items[i] >= 0 and states[i-1][maxSum - items[i]]:
            print(items[i]) # 购买这个商品
            maxSum -= items[i]
        # else 没有购买这个商品，j 不变。

    if maxSum != 0: print(items[0])

double11()


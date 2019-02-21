"""
假设有一个n乘以n的矩阵w[n][n]。矩阵存储的都是正整数。棋子起始位置在左上角，终止位置在右下角。
将棋子从左上角移到右下角。
每次只能向右或向下移动一个位置。
求左上角移动到右下角的最短路径长度？
"""
import sys

# 回溯
MinDist = sys.maxsize
# w, 二维数组，每个格子的权重
def minDistBT(i, j, dist, w, n):
    global MinDist
    if i == n and j == n:
        if dist < MinDist:
            MinDist = dist
        return

    if i < n:
        minDistBT(i+1, j, dist+w[i][j], w, n)
    if j < n:
        minDistBT(i, j+1, dist+w[i][j], w, n)

w = [[1,4,2], [2,4,2], [2,4,5]]
minDistBT(0, 0, 0, w, 2)
print(MinDist + w[2][2])

# 动态转移表
def minDistDP(w, n):
    # 声明二维数组
    state = [[0 for i in range(n)] for i in range(n)]
    sum = 0
    # 第一行
    for i in range(n):
        sum += w[0][i]
        state[0][i] = sum

    sum = 0
    # 第一列
    for i in range(n):
        sum += w[i][0]
        state[i][0] = sum

    for i in range(1, n):
        for j in range(1, n):
            state[i][j] = w[i][j] + min(state[i-1][j], state[i][j-1])

    return state[n-1][n-1]

print(minDistDP(w, 3))

# 动态转移方程。递归，备忘录
mem = [[0 for i in range(3)] for i in range(3)]
def minDistDP_1(i, j):
    if i == 0 and j == 0:
        return w[i][j]
    if mem[i][j] > 0:
        return mem[i][j]

    minLeft = sys.maxsize
    if j - 1 >= 0:
        minLeft = minDistDP_1(i, j-1)
    minUp = sys.maxsize
    if i - 1 >= 0:
        minUp = minDistDP_1(i-1, j)

    curMinDist = w[i][j] + min(minLeft, minUp)
    mem[i][j] = curMinDist
    return curMinDist

print(minDistDP_1(2,2))
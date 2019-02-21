#两个字符串相似度

import sys

# 回溯
a = "mitcmu"
b = "mtacnu"
n = 6
m = 6
minDist = sys.maxsize
def lwstBT(i, j, edist):
    global minDist
    if i == n or j == m:
        if i < n: edist += (n-i)
        if j < m: edist += (m-j)
        if edist < minDist: minDist = edist
        return

    if a[i] == b[j]:
        lwstBT(i+1, j+1, edist)
    else:
        lwstBT(i+1, j, edist+1)
        lwstBT(i, j+1, edist+1)
        lwstBT(i+1, j+1, edist+1)

lwstBT(0,0,0)
print(minDist)

#动规
def lwstDP(a,n,b,m):
    minDist = [[0 for i in range(m)] for i in range(n)]
    for j in range(m):
        if a[0] == b[j]: minDist[0][j] = j #
        elif j != 0: minDist[0][j] = minDist[0][j-1] + 1
        else: minDist[0][j] = 1 # j=0时，不相等时，等于1
    for i in range(n):
        if b[0] == a[i]: minDist[i][0] = i
        elif i != 0: minDist[i][0] = minDist[i-1][0] + 1
        else: minDist[i][0] = 1

    for i in range(1, n):
        for j in range(1, m):
            if a[i] == b[j]:
                minDist[i][j] = min(minDist[i-1][j] + 1, minDist[i][j-1] + 1, minDist[i-1][j-1])
            else:
                minDist[i][j] = min(minDist[i-1][j] + 1, minDist[i][j-1] + 1, minDist[i-1][j-1] + 1)
    return minDist[n-1][m-1]

print(lwstDP(a,n,b,m))

"""
最长公共子串

转移方程：
    如果：a[i]==b[j]，那么：max_lcs(i, j) 就等于：
    max(max_lcs(i-1,j-1)+1, max_lcs(i-1, j), max_lcs(i, j-1))；

    如果：a[i]!=b[j]，那么：max_lcs(i, j) 就等于：
    max(max_lcs(i-1,j-1), max_lcs(i-1, j), max_lcs(i, j-1))；

    其中 max 表示求三数中的最大值。
"""
def lcs(a,n,b,m):
    maxlcs = [[0 for i in range(m)] for i in range(n)]
    for j in range(m):
        if a[0] == b[j]: maxlcs[0][j] = 1
        elif j != 0: maxlcs[0][j] = maxlcs[0][j-1]
        else: maxlcs[0][j] = 0
    for i in range(n):
        if b[0] == a[i]: maxlcs[i][0] = 1
        elif i != 0: maxlcs[i][0] = maxlcs[i-1][0]
        else: maxlcs[i][0] = 0

    for i in range(1, n):
        for j in range(1, m):
            if a[i] == b[j]:
                maxlcs[i][j] = max(maxlcs[i-1][j], maxlcs[i][j-1], maxlcs[i-1][j-1]+1)
            else:
                maxlcs[i][j] = max(maxlcs[i-1][j], maxlcs[i][j-1], maxlcs[i-1][j-1])
    return maxlcs[n-1][m-1]

print("lcs: ", lcs(a,n,b,m))

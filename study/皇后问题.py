n = int(input())
mapL = [list(map(int,input().split())) for _ in range(n)]   #模拟棋盘
count = 0   #计数器
def dfs(row,n,s,mapL):
    global count
    if row == n:    #判断是否是放完了最后一行，注意我的行数是从0开始，0代表第一行
        if s == 2:  #2代表黑皇后，3代表白皇后
            dfs(0,n,3,mapL) #黑皇后放完，开始放白皇后
        if s == 3:  #全部放完
            count += 1
        return
    for i in range(n):
        if mapL[row][i] != 1:   #不为1、说明放了皇后，或者不能皇后
            continue
        if check(row,i,s,mapL):
            mapL[row][i] = s    #可以放，将格子的数字变为放置对应皇后的数字
            dfs(row+1,n,s,mapL)
            mapL[row][i] = 1    #回溯
def check(row,j,s,mapL):
    r = row - 1
    k = j - 1
    for i in range(row-1,-1,-1):    #检查对应列
        if mapL[i][j] == s:
            return False
    while r>=0 and k>=0:    #检查对应左上角
        if mapL[r][k] == s:
            return False
        r -= 1
        k -= 1
    r = row -1
    k = j + 1
    while r>=0 and k<n: #检查对 应右上角
        if mapL[r][k] == s:
            return False
        r -= 1
        k += 1
    return True
dfs(0,n,2,mapL)
print(count)

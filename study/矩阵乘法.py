#输入方阵的大小(n*n) 和幂m
n,m=map(int,input().split())
# 输入数据生成矩阵
matrix=[]
for _ in range(n):
    matrix.append(list(map(int,input().split())))
#矩阵matrix_a和矩阵matrix_b相乘得到matrix_result
def multi(matrix_a,matrix_b):
    #对于a*b和b*c的矩阵,得到的规模是a*c
    matrix_result=[[0 for _ in range(len(matrix_b[0]))] for _ in range(len(matrix_a))]
    for i in range(len(matrix_a)):
        for j in range(len(matrix_b[0])):
            #这里len(matrix_b)也可以换成len(matrix_a[0])
            for k in range(len(matrix_b)):
                matrix_result[i][j]+=matrix_a[i][k]*matrix_b[k][j]
    return matrix_result
# 求和matrix规模相同的单位矩阵E
def unit_1(n):
    #print('unit进来了')
    #初始化为0
    E=[[0 for _  in range(n)]for _ in range(n)]
    #对角线为1
    for i in range(n):
        E[i][i]=1
    #print(E)
    return E
#矩阵快速幂
def quick_multi(matrix,m):
    #print('quick进来')
    res=unit_1(len(matrix))
    while m:
        if m&1:
            res=multi(res,matrix)
        matrix=multi(matrix,matrix)
        m=m>>1
    #print('quick结束')
    return res
#输出
for r in quick_multi(matrix,m):
    print(' '.join([str(i) for i in r]))
from sys import stdin as s

w,h = map(int,s.readline().split())
x,y = map(int,s.readline().split())
dp=[[0]*(w)for _ in range(h)]

dp[0][0]=1


#토스트 집까지의 거리
for i in range(y):
    for j in range(x):
        if j==0:
            dp[i][j]=1
        else:
            dp[i][j]=(dp[i-1][j]+dp[i][j-1])%1000007
            

first = (dp[y-1][x-1])%1000007
dp[y-1][x-1] = 1
 
#토스트 집에서부터 집까지거리
for i in range(y-1,h):
    for j in range(x-1,w): 
        if j==0:
            dp[i][j]=1
        elif i==y-1 and j==x-1:
            continue
        else:
            dp[i][j]=(dp[i-1][j]+dp[i][j-1])%1000007

print((first * dp[h-1][w-1])%1000007)


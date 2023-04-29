from sys import stdin as s

n = int(s.readline())
grape =[0]*(n+2)

for i in range(1,n+1):
    grape[i]=int(s.readline())

dp=[0]*(n+2)
dp[1] = grape[1]
dp[2] = grape[1] + grape[2]

for i in range(3,n+1):
        dp[i] = max(dp[i-1],dp[i-3]+grape[i]+grape[i-1],dp[i-2]+grape[i])

print(max(dp))
    
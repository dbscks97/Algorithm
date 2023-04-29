from sys import stdin as s

N = int(s.readline())
dp=[0]*(N+1)

for i in range(2,N+1):
    dp[i]=dp[i-1]+1
    
    if (i%3==0) and (i%2==0):
        dp[i]=min(dp[i//2]+1,dp[i//3]+1)
    elif i%2==0:
        dp[i]=min(dp[i],dp[i//2]+1)
    elif i%3==0:
        dp[i]=min(dp[i],dp[i//3]+1)

print(dp[N])
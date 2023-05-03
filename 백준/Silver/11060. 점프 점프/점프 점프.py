from sys import stdin as s

n = int(s.readline())
arr = list(map(int,s.readline().split()))
dp=[n+1]*(n)
dp[0]=0

for i in range(n):
    for j in range(1,1+arr[i]):
        if i+j<n:
            dp[i+j] = min(dp[i]+1,dp[i+j])

if dp[-1]==(n+1):
    print(-1)
else:
    print(max(dp))
      
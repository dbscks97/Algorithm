from sys import stdin as s

n =int(s.readline())
dp=[0]*(n+1)
arr=[0]+list(map(int,s.readline().split()))

for i in range(1, n+1):
    for j in range(1,i+1):
        dp[i] = max(dp[i], arr[j] + dp[i-j])
print(dp[n])
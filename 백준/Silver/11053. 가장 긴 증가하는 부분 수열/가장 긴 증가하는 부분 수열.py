from sys import stdin as s

A = int(s.readline())

arr = list(map(int,s.readline().split()))

dp = [1]*A

for i in range(1,A):
    for j in range(0,i):
        if arr[j] <arr[i]:
            dp[i] = max(dp[i],dp[j]+1)

print(max(dp))
    

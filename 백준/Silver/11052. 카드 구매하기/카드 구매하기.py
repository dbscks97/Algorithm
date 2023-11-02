from sys import stdin as s
N = int(s.readline())

arr =[0] + list(map(int,s.readline().split()))
dp = [0] * len(arr)
result = 0

for i in range(1,N+1):
    for j in range(1,i+1):
        dp[i] = max(dp[i],dp[i-j]+arr[j])

print(dp[N])
    
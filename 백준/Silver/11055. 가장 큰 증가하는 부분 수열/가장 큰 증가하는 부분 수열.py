from sys import stdin as s

A = int(s.readline())
arr = list(map(int,s.readline().split()))
dp = [0] * (A+1)
dp[0] = arr[0]
for i in range(1,A):
  for j in range(i):
    if arr[j]<arr[i]:
      dp[i]=max(dp[i], dp[j]+arr[i])
    else:
      dp[i]=max(dp[i], arr[i])

print(max(dp))
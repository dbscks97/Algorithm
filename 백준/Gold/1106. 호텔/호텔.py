from sys import stdin as s

C,N = map(int,s.readline().split())
arr=[]
count=0
result=0
for i in range(N):
    cost,people = map(int,s.readline().split())
    arr.append((cost,people))

max_people = max(arr, key=lambda x: x[1])[1]

dp = [float('inf')] * (C+max_people + 1)
dp[0]=0

for cost,people in arr:
    for i in range(people,C+max_people+1):
        dp[i]=min(dp[i-people]+cost,dp[i])

print(min(dp[C:]))


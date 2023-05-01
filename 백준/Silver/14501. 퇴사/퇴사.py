from sys import stdin as s

n = int(s.readline())
arr=[(0,0)]
dp = [0 for _ in range(n+1)]

for i in range(n):
    A,B = map(int,s.readline().split())
    arr.append((A,B))

for i in range(1,n+1):
    time = arr[i][0]
    money = arr[i][1]
    
    if i+time > n+1:
        continue
    else:
        dp[i]= max(dp[i],money)
        for j in range(i+time,n+1):
            next_time = arr[j][0]
            if j+next_time <= n+1:
                dp[j] = max(dp[j],arr[j][1]+dp[i])

print(max(dp))
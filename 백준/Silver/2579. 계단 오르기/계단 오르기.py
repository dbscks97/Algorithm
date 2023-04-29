from sys import stdin as s

n = int(s.readline())
stairs=[0]*(n+1)
dp=[0]*(n+1)
for i in range(1,n+1):
    stairs[i] = int(s.readline())

if n == 1:
    print(stairs[n])

elif n == 2:
    print(stairs[1]+stairs[2])
else:
    dp[1]=stairs[1]
    dp[2]=stairs[1]+stairs[2]

    for i in range(3,n+1):
        dp[i] = max(dp[i-3]+stairs[i-1]+stairs[i],dp[i-2]+stairs[i])

    print(dp[n])
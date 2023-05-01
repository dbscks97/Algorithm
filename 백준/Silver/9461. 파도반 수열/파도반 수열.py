from sys import stdin as s

T= int(s.readline())

for i in range(T):
    N = int(s.readline())
    dp=[0]*(N+4)
    dp[1]=1
    dp[2]=1
    dp[3]=1
    dp[4]=2
    for j in range(5,N+1):
        dp[j] = dp[j-1]+dp[j-5]

    print(dp[N])
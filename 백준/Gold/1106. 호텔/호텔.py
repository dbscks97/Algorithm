from sys import stdin as s

C,N = map(int,s.readline().split())

dp=[1e9]*(C+1000)
dp[0] = 0
for i in range(N):
    cost, people = map(int,s.readline().split())
    
    for j in range(1,C+1+people):
        dp[j] = min(dp[j-people]+cost,dp[j])
        
print(min(dp[C:]))
    
from sys import stdin as s

K = int(s.readline())

paper = sorted([sorted(map(int, s.readline().split())) for i in range(K)])


dp = [1] * K

for i in range(1,K):
    for j in range(i):
        if paper[i][1] >= paper[j][1]:
            dp[i] = max(dp[i],dp[j]+1)
        # else:
        #     if paper[i][0] >= paper[j][1]:
        #         if paper[i][1] >= paper[j][0]:
        #             dp[i] = max(dp[i],dp[j]+1)
            
print(max(dp))
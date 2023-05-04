from sys import stdin as s

n = int(s.readline())
dp=[[0]*n for _ in range(n)]
arr=[list(map(int,s.readline().split())) for _ in range(n)]
dp[0][0]= 1


for i in range(n):
    for j in range(n):
        
        if i == n-1 and j == n-1:
            print(dp[i][j])
            break
        
        temp = arr[i][j]
        
        if dp[i][j]!=0:
            if (j+temp) < n:
                dp[i][j+temp] += dp[i][j]
               
                    
                
            if (i+temp) <n:
                dp[i+temp][j] += dp[i][j]


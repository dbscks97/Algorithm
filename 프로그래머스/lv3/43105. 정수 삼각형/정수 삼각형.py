def solution(triangle):
    answer = 0
    dp = [[0] * len(triangle) for _ in range(len(triangle))]
    dp[0][0] = triangle[0][0]
    
    for i in range(len(triangle)):
        for j in range(i):
            dp[i][j] = max(dp[i][j], dp[i-1][j]+triangle[i][j])
            dp[i][j+1] = dp[i-1][j]+triangle[i][j+1]
    answer = max(dp[-1])
    return answer
from sys import stdin as s
import sys
sys.setrecursionlimit(10**8)

def dfs(x,y):
    
    if x == m-1 and y == n-1:
        return 1
    
    if dp[x][y] != -1:
        return dp[x][y]      

    ways=0
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<m and 0<=ny<n and arr[x][y] > arr[nx][ny]: 
            ways += dfs(nx,ny)
            
    dp[x][y] = ways
    return dp[x][y]

if __name__=='__main__':
    m,n = map(int,s.readline().split())

    arr = [list(map(int,s.readline().split()))for _ in range(m)]
    dp=[[-1]*n for _ in range(m)]
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]

    print(dfs(0,0))

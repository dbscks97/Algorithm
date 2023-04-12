import sys
from collections import deque

def bfs(i,j,h):
    
    queue = deque()
    queue.append((i,j))
    v[i][j] = 1
    
    while queue:
        ci,cj = queue.popleft()
        
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj = ci+di,cj+dj
            
            if 0<=ni<n and 0<=nj<n and v[ni][nj]==0 and graph[ni][nj]>h:
                queue.append((ni,nj))
                v[ni][nj]=1
        



def solve(h):
    cnt = 0
    
    for i in range(n):
        for j in range(n):
            if v[i][j]==0 and graph[i][j]>h:
                bfs(i,j,h)
                cnt+=1
    return cnt

if __name__=='__main__':
    n = int(sys.stdin.readline())
    ans = 1

    graph = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]



    for h in range(1,101):
        v=[[0]*n for _ in range(n)]
        ans = max(ans,solve(h))
    
print(ans)
    
            
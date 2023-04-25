from sys import stdin as s
from collections import deque


def bfs(si,sj,ei,ej):
 
    q = deque()
    q.append((si,sj))
    v[si][sj]=1
    

    while q:
        ci,cj = q.popleft()
        
        if (ci,cj)==(ei,ej):
            return v[ei][ej]
        
        for i in range(4):
            nx = ci+dx[i]
            ny = cj+dy[i]
            
            if 0<=nx<N and 0<=ny<N and not v[nx][ny]:
                if graph[nx][ny]:
                    q.appendleft((nx,ny))
                    v[nx][ny]=v[ci][cj]
                else:
                    q.append((nx,ny))
                    v[nx][ny]=v[ci][cj]+1
 
    
if __name__=='__main__':
    
    N = int(s.readline().strip())
    
    
    graph=[list(map(int,s.readline().strip())) for _ in range(N+1)]
    v = [[0]*(N) for _ in range(N)]
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]

    
    ans=bfs(0,0,N-1,N-1)
    
    if ans:
        print(ans-1)
    else:
        print(0)
    
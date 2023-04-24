from sys import stdin as s
from collections import deque

def bfs(si,sj,ei,ej):
    global cnt
    
    q=deque()
    q.append((si,sj))
    visit[si][sj]=1
    
    while q:
        ci,cj = q.popleft()
        
        if (ci,cj)==(ei,ej):
            return visit[ei][ej]
        
        for di,dj in ((0,1),(1,0),(0,-1),(-1,0)):
            ni,nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<M and arr[ni][nj]==1 and visit[ni][nj]==0:
                q.append((ni,nj))
                visit[ni][nj]=visit[ci][cj]+1
    


if __name__=='__main__':
    N,M = map(int,s.readline().split())
    
    arr=[list(map(int,s.readline().strip())) for _ in range(N)]

    visit =[[0]*M for _ in range(N)]
    ans=bfs(0,0,N-1,M-1)
    
    print(ans)
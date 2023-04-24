from collections import deque
import sys
from sys import stdin as s
sys.setrecursionlimit(10**6)

def bfs(si,sj,ei,ej):
    q=deque()
    q.append((si,sj))
    v[si][sj]=1
    
    while q:
        ci,cj = q.popleft()
        
        if (ci,cj) ==  (ei,ej):
            return v[ei][ej]
        
        di = [0,1,0,-1]
        dj = [1,0,-1,0]
        
        for i in range(4):
            ni = ci+di[i]
            nj = cj+dj[i]
            
            if 0<=ni<N and 0<=nj<M and arr[ni][nj]==1 and v[ni][nj]==0:
                v[ni][nj]=v[ci][cj]+1
                q.append((ni,nj))
                            

if __name__=='__main__':
    
    N,M = map(int,s.readline().split())
    arr = [list(map(int,s.readline().strip()))for _ in range(N)]
    v = [[0] * M for _ in range(N)]
    
    ans = bfs(0,0,N-1,M-1)
    
    print(ans)
    
    
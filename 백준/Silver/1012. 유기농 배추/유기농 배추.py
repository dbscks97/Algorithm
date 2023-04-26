from sys import stdin as s
from collections import deque

def bfs(si,sj):
    
    q = deque()
    q.append((si,sj))
    v[si][sj]=1
    
    while q:
        
        ci,cj = q.popleft()
        dx = [0,1,0,-1]
        dy = [1,0,-1,0]
                    
        for i in range(4):
            nx = ci +dx[i]
            ny = cj +dy[i]
            
            if 0<=nx<N and 0<=ny<M and graph[nx][ny] and not v[nx][ny]:
                q.append((nx,ny))
                v[nx][ny]=1

if __name__=='__main__':
    T = int(s.readline())
    
    for k in range(T):
        
        M,N,K = map(int,s.readline().split())
        v = [[0]*M for _ in range(N)]
        graph =[[0]*M for _ in range(N)]
        cnt =0
        
        for i in range(K):
            a,b = map(int,s.readline().split())
            graph[b][a] =1
    
        for i in range(N):
            for j in range(M):
                if not v[i][j] and graph[i][j]!=0:
                    bfs(i,j)
                    cnt+=1
        print(cnt)    
        
        
    
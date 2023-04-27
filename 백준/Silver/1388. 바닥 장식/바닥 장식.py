from sys import stdin as s
from collections import deque

def bfs(x,y):
    q = deque()
    q.append((x,y))
    v[x][y]=1
    
    while q:
        ci,cj = q.popleft()
           
        if graph[ci][cj] =='-':
            v[ci][cj]=1
            if cj+1 < M and graph[ci][cj+1] == '-':
                q.append((ci,cj+1))
        else:
            v[ci][cj]=1
            if ci+1 < N and graph[ci+1][cj] =='|':
                q.append((ci+1,cj))
            

if __name__=='__main__':
    
    N,M = map(int,s.readline().split())
    
    graph =[list(map(str,s.readline().strip()))for _ in range(N)]
    v=[[0]*M for _ in range(N)]
    cnt =0 
    
    for i in range(N):
        for j in range(M):
            if not v[i][j]:
                bfs(i,j)
                cnt+=1
    
    print(cnt)
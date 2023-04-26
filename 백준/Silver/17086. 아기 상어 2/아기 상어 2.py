from sys import stdin as s
from collections import deque

def bfs():
    
    while q:
        si,sj = q.popleft()
        dx = [0,1,0,-1,1,1,-1,-1]
        dy = [1,0,-1,0,1,-1,1,-1]
        for i in range(8):
            nx = si +dx[i]
            ny = sj +dy[i]
            
            if 0<=nx<N and 0<=ny<M and not graph[nx][ny]:
                q.append((nx,ny))
                graph[nx][ny]=graph[si][sj]+1

if __name__=='__main__':
    N,M = map(int,s.readline().split())
    
    graph =[list(map(int,s.readline().split())) for _ in range(N)]
    q=deque()
    distance = 0
    for i in range(N):
            for j in range(M):
                if graph[i][j]==1:
                    q.append((i,j))
    
    bfs()
    
    
    for i in range(N):
        for j in range(M):
            distance =max(distance,graph[i][j])
    print(distance-1)
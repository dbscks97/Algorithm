from sys import stdin as s
from collections import deque

def bfs(si,sj):
    q = deque()
    q.append((si,sj))
    v[si][sj] = 1
    dan_count=1
    while q:
        ci,cj = q.popleft()
        
        
        dx = [0,1,0,-1]
        dy = [1,0,-1,0]
        
        for i in range(4):
            nx = ci + dx[i]
            ny = cj + dy[i]
            
            if 0<=nx<N and 0<=ny<N and not v[nx][ny] and graph[nx][ny]:
                v[nx][ny]=1
                dan_count+=1
                q.append((nx,ny))
                
    answer.append(dan_count) 
if __name__=='__main__':
    N = int(s.readline())
    
    graph = [list(map(int,s.readline().strip()))for _ in range(N)]
    v= [[0]*N for _ in range(N)]
    answer=[]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if not v[i][j] and graph[i][j]:
                bfs(i,j)
                cnt+=1
    
    answer.sort()
    print(cnt)
    for i in answer:
        print(i)
    
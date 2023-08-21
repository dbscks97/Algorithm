from sys import stdin as s
from collections import deque

def bfs(si,sj):
    global count
    
    q=deque()
    melts=deque()
    q.append((si,sj))
    v[si][sj] = 1
    
    while q:
        ci,cj = q.popleft()
        
        dx =[0,1,0,-1]
        dy =[1,0,-1,0]
        
        for i in range(4):
            nx = dx[i] + ci
            ny = dy[i] + cj
            
            if 0<=nx<N and 0<=ny<M and not v[nx][ny]:
                if cheese[nx][ny]==0:
                    q.append((nx,ny))
                    v[nx][ny] = 1
                    
                if cheese[nx][ny]==1:
                    melts.append((nx,ny))
                    v[nx][ny] = 1
                    
    for x,y in melts:
        cheese[x][y] = 0
    
    return len(melts)
                  

if __name__ == "__main__":
    N, M = map(int,s.readline().split())
    cheese = [list(map(int,s.readline().split())) for _ in range(N)]
    
    count = 0
    time = 1
    ans=[]
    for i in range(N):
        for j in range(M):
            if cheese[i][j]==1:
                count += 1
                
    while True:
        v = [[0] * M for _ in range(N)]
        melt_count = bfs(0,0)
        ans.append(melt_count)
        count -= melt_count
        if count == 0:
            print(time)
            print(ans[-1])
            break
        time += 1
 



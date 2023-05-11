from sys import stdin as s
from collections import deque

def bfs(si,sj):
    global cnt
    global q_size
  
    
    while q:
        q_size=len(q)
        for _ in range(q_size):
            ci,cj = q.popleft()
    
            for i in range(4):
                nx = ci+dx[i]
                ny = cj+dy[i]

                if 0<=nx<N and 0<=ny<M and tomato[nx][ny]==0:
                    q.append((nx,ny))
                    tomato[nx][ny]=2
        cnt+=1
                
if __name__=='__main__':
    M,N = map(int,s.readline().split())
    tomato=[list(map(int,s.readline().split())) for _ in range(N)]
    q=deque()
    cnt=0
    q_size=0
    ans=[]
        
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    
    for i in range(N):
        for j in range(M):
            if tomato[i][j]==1:
                q.appendleft((i,j))
                tomato[i][j]=2
    
    bfs(i,j)
    
    for i in range(N):
        for j in range(M):
            if tomato[i][j]==0:
                ans.append((i,j))
                break

    if ans:
        print(-1)
    else:
        print(cnt-1)

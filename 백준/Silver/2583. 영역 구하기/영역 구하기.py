from sys import stdin as s
from collections import deque

def bfs(si,sj):
    q=deque()
    block_count=1
    v[si][sj]=1
    q.append((si,sj))
    
    dx=[0,1,0,-1]
    dy=[1,0,-1,0]
    while(q):
        ci,cj = q.popleft()
        
        for i in range(4):
            nx = ci + dx[i]
            ny = cj + dy[i]
            
            if 0<=nx<N and 0<=ny<M and v[nx][ny]==0:
                v[nx][ny]=1
                q.append((nx,ny))
                block_count+=1
    
    answer.append(block_count)  
        
N,M,K = map(int,s.readline().split())
v=[[0]*M for _ in range(N)]
area_count=0
answer=[]
for i in range(K):
    s_x,s_y,e_x,e_y = map(int,s.readline().split())
    
    for k in range(s_x,e_x):
        for j in range(s_y,e_y):
            v[j][k]=1
# v=v[::-1]

for i in range(N):
    for j in range(M):
        if v[i][j]==0:
            bfs(i,j)
            area_count+=1
answer.sort()
print(area_count)
print(*answer)
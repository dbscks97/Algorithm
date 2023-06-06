from sys import stdin as s
from collections import deque


def bfs(si,sj):
    q=deque()
    q.append((si,sj))
    v[si][sj]=1
    dx=[0,1,0,-1]
    dy=[1,0,-1,0]
    
    while q:
        ci,cj = q.popleft()
        
        for i in range(4):    
            nx = ci+dx[i]
            ny = cj+dy[i]
            
            if 0<=nx<N and 0<=ny<M and not v[nx][ny] and arr[nx][ny]==-1:
                v[nx][ny]=1
                arr[nx][ny] = arr[ci][cj]+1
                q.append((nx,ny))
    
if __name__=='__main__':
    N,M = map(int,s.readline().split())
    ans=[]
    arr = [list(map(int,s.readline().split())) for _ in range(N)]
    v = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 2:
                ans.append((i,j))
            if arr[i][j] == 1:
                arr[i][j] = -1
    arr[ans[0][0]][ans[0][1]]=0
    bfs(ans[0][0],ans[0][1])
    
    
    for row in arr:
        print(" ".join(map(str,row)))
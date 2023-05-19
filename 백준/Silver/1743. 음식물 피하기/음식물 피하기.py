from sys import stdin as s
from collections import deque

def bfs(si,sj):
    global cnt
    cnt=1
    q=deque()
    q.append((si,sj))
    v[si][sj]=1
    
    while q:
        ci,cj = q.popleft()
        
        for i in range(4):
            nx= ci+dx[i]
            ny= cj+dy[i]
            
            if 0<=nx<N and 0<=ny<M and arr[nx][ny] =='#' and not v[nx][ny]:
                cnt+=1
                q.append((nx,ny))
                v[nx][ny]=1
    
    ans.append(cnt)

if __name__=='__main__':
    N,M,K = map(int,s.readline().split())
    arr=[[0]*M for _ in range(N)]
    v=[[0]*M for _ in range(N)]
    ans=[]

    dx=[0,1,0,-1]
    dy=[1,0,-1,0]    

    for i in range(K):
        a,b =map(int,s.readline().split())
        arr[a-1][b-1] = '#'



    for i in range(N):
        for j in range(M):
            if arr[i][j]!=0:
                bfs(i,j)

    print(max(ans))


        
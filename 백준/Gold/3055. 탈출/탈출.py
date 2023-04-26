from sys import stdin as s
from collections import deque


def bfs(si,sj):
    

    v[si][sj]=1
    
    while q:
        ci,cj = q.popleft()
        
        dx = [0,1,0,-1]
        dy = [1,0,-1,0]
                
        for i in range(4):
            nx = ci + dx[i]
            ny = cj + dy[i]
            
            if 0<=nx<R and 0<=ny<C and (graph[nx][ny]=='.' or graph[nx][ny]=='D') and graph[ci][cj]=='S':
                v[nx][ny] = v[ci][cj]+1
                graph[nx][ny]='S'
                q.append((nx,ny))
            
            elif 0<=nx<R and 0<=ny<C and (graph[nx][ny]=='.' or graph[nx][ny]=='S') and graph[ci][cj]=='*':
                graph[nx][ny]='*'
                q.append((nx,ny))     
              

if __name__=='__main__':
    R,C = map(int,s.readline().split())
    graph = [list(map(str,s.readline().strip())) for _ in range(R)]
    
    v = [[0]*C for _ in range(R)]
    q = deque()
    
    #고슴도치 집 위치 저장
    for i in range(R):
        for j in range(C):
            if graph[i][j]=='D':
                c,d = i,j
                
    #고슴도치 위치 찾고 q에 저장 
    for i in range(R):
        for j in range(C):
            if graph[i][j]=='S':
                x,y =i,j
                q.append((x,y))
                     
    #물의 위치 찾고 q에 저장
    for i in range(R):
        for j in range(C):
            if graph[i][j]=='*':
                q.append((i,j))
    
    bfs(x,y)
    
    #bfs종료후에 v배열확인 후 원하는 값 출력
    if v[c][d]:
        print(v[c][d]-1)
    else:
        print('KAKTUS')

    
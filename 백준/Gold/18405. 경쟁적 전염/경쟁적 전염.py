from sys import stdin as s
from collections import deque

def bfs(ci,cj):
    global cnt
    v[ci][cj]=1
    
    while q:
        if cnt ==S*(len(answer)):
            break
        ci,cj = q.popleft()
        cnt +=1
        
        dx = [0,1,0,-1]
        dy = [1,0,-1,0]
        
        for i in range(4):
            nx = ci+dx[i]
            ny = cj+dy[i]
            
            if 0<=nx<N and 0<=ny<N and not v[nx][ny]:
                v[nx][ny] = 1
                graph[nx][ny]=graph[ci][cj]
                q.append((nx,ny))
    

if __name__=='__main__':
    
    N,K = map(int,s.readline().split())
    cnt=0
    graph=[list(map(int,s.readline().split()))for _ in range(N)]
    v=[[0]*N for _ in range(N)]
    answer = []*N
    q= deque()
    S,X,Y = map(int,s.readline().split())

    
    for i in range(N):
        for j in range(N):
            if graph[i][j]:
                temp = graph[i][j]
                answer.append((temp,i,j))
                v[i][j]=1
                
    answer.sort(key=lambda x:x[0])

    for i in answer:
        q.append((i[1],i[2]))


    bfs(answer[0][1],answer[0][2])

    if graph[X-1][Y-1]:
        print(graph[X-1][Y-1])
    else:
        print(0)
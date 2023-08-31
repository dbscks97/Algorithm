from collections import deque
def solution(maps):
    h =len(maps)
    w = len(maps[0])
    def bfs(st,en):
        v=[[0]*w for _ in range(h)]
        q=deque()
        q.append(st)
        v[st[0]][st[1]] = 1
        
        while q:
            ci,cj=q.popleft()
            
            dx=[0,1,0,-1]
            dy=[1,0,-1,0]
            
            for i in range(4):
                nx = dx[i]+ci
                ny = dy[i]+cj
                
                if 0<=nx<h and 0<=ny<w and not v[nx][ny]:
                    if maps[nx][ny] == 'O' or maps[nx][ny] =='L' or maps[nx][ny] =='E' or maps[nx][ny]=='S':
                        q.append((nx,ny))
                        v[nx][ny] = v[ci][cj] +1
                    
        return v[en[0]][en[1]]-1
                   
    for i in range(h):
        for j in range(w):
            if maps[i][j]=='S':
                start = (i,j)
            elif maps[i][j]=='L':
                lever = (i,j)
            elif maps[i][j]=='E':
                end = (i,j)
            
                
    first = bfs(start,lever)
    if first == -1:
        return -1
    second = bfs(lever,end)
    if second == -1:
        return -1
    
        
    return first+second
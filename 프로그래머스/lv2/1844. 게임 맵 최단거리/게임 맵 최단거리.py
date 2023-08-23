from collections import deque

def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    v = [[0]*m for _ in range(n)]
    result = maps[n-1][m-1]
    def bfs(si,sj):
        q=deque()
        q.append((si,sj))
        v[si][sj]=1
        while q:
            ci,cj = q.popleft()
            
            dx = [0,1,0,-1]
            dy = [1,0,-1,0]
            
            for i in range(4):
                nx = dx[i] + ci
                ny = dy[i] + cj
                
                if 0<=nx<n and 0<=ny<m and not v[nx][ny] and maps[nx][ny] ==1:
                    q.append((nx,ny))
                    v[nx][ny] = v[ci][cj] + 1
                    
                        
        return v[n-1][m-1]
    answer += bfs(0,0)    
    
    
    if v[n-1][m-1] == 0:
        answer -= 1
    else:
        print(answer)
    return answer
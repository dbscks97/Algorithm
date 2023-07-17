from sys import stdin as s
from collections import deque

def bfs(si,sj):
    q=deque()
    q.append((si,sj))
    c = arr[si][sj]
    arr[si][sj] = 1
    cnt=0
    while q:
        ci,cj = q.popleft()
        cnt+=1
        dx = [0,1,0,-1]
        dy = [1,0,-1,0]
        
        for i in range(4):
            nx = ci+dx[i]
            ny = cj+dy[i]
            
            if 0 <= nx < M and 0 <= ny <N:
                if arr[nx][ny] == c:
                    q.append((nx,ny))
                    arr[nx][ny]=1
                    
    return cnt
        
    
 

if __name__=='__main__':
    N,M = map(int,s.readline().split())

    arr = [list(map(str,s.readline().strip())) for _ in range(M)]
    v = [[0] * N for _ in range(M)]
    ans = []
    w = b = 0
    for i in range(M):
        for j in range(N):
            if arr[i][j] == 'W':
                w += bfs(i, j)**2
            elif arr[i][j] == 'B':
                b += bfs(i, j)**2
    print(w,b)
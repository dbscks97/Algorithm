from sys import stdin as s
from collections import deque

def bfs(si,sj):
    q = deque()
    q.append((si,sj))
    v[si][sj] = 1
    
    while q:
        ci, cj = q.popleft()
        
        dx = [-1,-1,1,1,2,2,-2,-2]
        dy = [2,-2,2,-2,1,-1,1,-1]
        
        for i in range(8):
            nx = ci + dx[i]
            ny = cj + dy[i]
            
            if 0<=nx<l and 0<=ny<l and not v[nx][ny]:
                q.append((nx,ny))
                v[nx][ny] = v[ci][cj] + 1
                

if __name__=='__main__':
    T = int(s.readline())
    
    for i in range(T):
        l = int(s.readline())
        si, sj = map(int,s.readline().split())
        ei, ej = map(int,s.readline().split())
        
        v=[[0] * l for _ in range(l)]
        
        bfs(si,sj)
        print(v[ei][ej]-1)
        
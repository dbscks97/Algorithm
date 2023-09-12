from collections import deque

def bfs(si, sj, m, n, v):
    q = deque()
    q.append((si, sj))
    v[si][sj] = 1 

    dx = [0, 1]
    dy = [1, 0]

    while q:
        ci, cj = q.popleft()
        
        for i in range(2):
            nx = dx[i] + ci
            ny = dy[i] + cj

            if 0 <= nx <= n and 0 <= ny <= m and not v[nx][ny]:
                if v[nx-1][ny] == -1:
                    v[nx][ny] += v[nx][ny-1]
                elif v[nx][ny-1] == -1:
                    v[nx][ny] += v[nx-1][ny]
                else:
                    v[nx][ny] = (v[nx-1][ny] + v[nx][ny-1]) % 1000000007
                q.append((nx, ny))

def solution(m, n, puddles):
    answer = 0
    v = [[0] * (m + 1) for _ in range(n + 1)]
    
    for puddle in puddles:
        a = puddle[1]
        b = puddle[0]
        v[a][b] = -1
    
    bfs(1, 1, m, n, v)
    
    answer = v[n][m] % 1000000007  
    
    return answer

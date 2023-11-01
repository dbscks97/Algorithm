from sys import stdin as s
from collections import deque

def bfs(si,sj):
    global pic_count
    global result
    
    q = deque()
    q.append((si,sj))
    v[si][sj] = 1
    pic_count += 1
    pic_max_area = 1
    
    while q:
        ci,cj = q.popleft()
        
        dx = [0,1,0,-1]
        dy = [1,0,-1,0]
        
        for i in range(4):
            nx = ci + dx[i]
            ny = cj + dy[i]
            
            if 0<=nx<n and 0<=ny<m and not v[nx][ny] and arr[nx][ny] ==1:
                q.append((nx,ny))
                v[nx][ny]=1
                pic_max_area +=1
    result = max(result,pic_max_area)
            
                

if __name__=='__main__':
    arr = []

    n,m = map(int,s.readline().split())
    pic_count = 0
    result = 0

    for i in range(n):
        arr_list = list(map(int,s.readline().split()))
        arr.append(arr_list)

    
    v = [[0] * m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1 and not v[i][j]:
                bfs(i,j)
    
    print(pic_count)
    print(result)
from collections import deque
import sys
from sys import stdin as s
sys.setrecursionlimit(10**5)


def count(x,y):
    cnt =0
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        
        if 0<=nx<N and 0<=ny<M and arr[nx][ny]==0:
            cnt -= 1
    answer[x][y]=cnt
       

def dfs(x,y):
    if x<0 or y<0 or x>=N-1 or y>=M-1:
        return
    if arr[x][y]:
        v[x][y]=1
        
    count(x,y)
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        
        if not v[nx][ny]:
            if 0<=nx<N and 0<=ny<M and arr[nx][ny]!=0:
                v[nx][ny]=1
                dfs(nx,ny)

      
            
if __name__=='__main__':
    
    N,M = map(int,s.readline().split())
    year = 0
    arr = [list(map(int,s.readline().split())) for _ in range(N)]
     # v로 방문표시
     # - 누적 표시
    dx =[0,1,0,-1]
    dy =[1,0,-1,0]
    ice_cnt=0
    
    
    
    
    while True:
        v = [[0]*M for _ in range(N)]
        answer =[[0]*M for _ in range(N)]
        ice_cnt=0
        
        for i in range(1,N):
            for j in range(1,M):
                if not v[i][j] and arr[i][j]>0:
                    dfs(i,j)
                    ice_cnt+=1
        
        
        if ice_cnt >1:
            break
        elif ice_cnt==0:
            year=0
            break
               
        
        for i in range(N):
            for j in range(M):
                if answer[i][j]+ arr[i][j] <0:
                    answer[i][j] = 0
                else:
                    answer[i][j] += arr[i][j]

        for i in range(N):
            for j in range(M):
                arr[i][j] = answer[i][j]


        year +=1 
        
        
                            
    print(year)
    
                
        
        
from sys import stdin as s
from collections import deque
import copy


def bfs():
    global result
    global count
    q=deque()
    test_map = copy.deepcopy(arr)
    
    #바이러스 위치 q에 저장
    for i in range(N):
        for j in range(M):
            if test_map[i][j]==2:
                q.append((i,j))
            
    #바이러스를 모든 칸에 전염시키는과정        
    while q:
        x,y = q.popleft()
        
        for i in range(4):    
            nx = x+dx[i]
            ny = y+dy[i]
            
            if 0<=nx<N and 0<=ny<M and not test_map[nx][ny]:
                q.append((nx,ny))
                test_map[nx][ny]=2
    
    #바이러스 전염 후 안전영역의 개수 카운트하기
    count=0
    for i in range(N):
        for j in range(M):
            if test_map[i][j]==0:
                count+=1
    #안전영역 최대개수 저장
    result=max(result,count)


#벽을 세우고 벽의 개수가 3이되면 bfs실행
def wall(count):
    if count==3:
        bfs()
        return
    for i in range(N):
            for j in range(M):
                if arr[i][j]==0:
                    arr[i][j]=1
                    wall(count+1)
                    arr[i][j]=0
if __name__=='__main__':
    N,M = map(int,s.readline().split())
    arr= [list(map(int,s.readline().split()))for _ in range(N)]
    
    result=0
    count=0
    
    #네 방향 탐색을 위한 변수설정
    dx=[0,1,0,-1]
    dy=[1,0,-1,0]
    
    wall(0)
    print(result)
    
    
    
                
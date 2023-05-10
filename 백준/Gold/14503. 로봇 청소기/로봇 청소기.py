from sys import stdin as s 
from collections import deque

def bfs(x,y,direct):
    global cnt
    #현재칸 청소하면 2로 넣어줌
    if arr[x][y]==0:
        arr[x][y]=2
        cnt+=1
   
    check =1
    #왼쪽으로 90도 회전을 시작으로 4방향 검사
    for _ in range(4):
        #왼쪽으로 90도 회전
        direct = (direct + 3)%4
        nx = x+dx[direct]
        ny = y+dy[direct]
        
        if not arr[nx][ny]:
            bfs(nx,ny,direct)
            check=0
            return
        # 후진하기
    if check==1:
        direct = (direct+2)%4
        nx = x+dx[direct]
        ny = y+dy[direct]
        
        if arr[nx][ny] != 1:
            bfs(nx,ny,(direct+2)%4)


if __name__=='__main__':
    N,M = map(int,s.readline().split())
    r,c,d = map(int,s.readline().split())
    cnt=0
    #북동남서순서
    dx=[-1,0,1,0]
    dy=[0,1,0,-1]
    arr = [list(map(int,s.readline().split())) for _ in range(N)]
    bfs(r,c,d)
    print(cnt)
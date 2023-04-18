from sys import stdin as s
from collections import deque

#s = open('input.txt','rt')
snake = deque([])
N = int(s.readline())
K = int(s.readline())

arr = [[0] * N for _ in range(N)]

for i in range(K):
    X,Y = map(int,s.readline().split())
    arr[X-1][Y-1]=1
    
time_list =deque([])
L = int(s.readline())

for i in range(L):
    time_set, vector = list(map(str,s.readline().split()))
    time_list.append((time_set,vector))



# 동, 남, 서, 북 (시계방향)
dx = [0,1,0,-1]
dy = [1,0,-1,0]

# 최초 값 설정
x,y,d = 0,0,0
time = 0

while True:
    time +=1
    snake.append((x,y))
    
    x += dx[d]
    y += dy[d]
        
    if x<0 or x>=N or y<0 or y>=N or arr[x][y]==2:
        break
    
    if not arr[x][y]:
        i,j = snake.popleft()
        arr[i][j] =0
        
    arr[x][y] =2
    
    if time_list:
        if time == int(time_list[0][0]):
            if time_list[0][1] =='D':  #D일경우 오른쪽으로 90도 회전
                d = (d+1) % 4
                time_list.popleft() 
            else:                      #D가 아닐경우(L) 왼쪽으로 90도 회전
                d = (d-1) % 4
                time_list.popleft()
        
     
print(time)

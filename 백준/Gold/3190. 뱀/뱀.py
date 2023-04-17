from sys import stdin as s
from collections import deque

#s = open('input.txt','rt')



N = int(s.readline())
K = int(s.readline())
arr = [[0] * N for _ in range(N)] # 전체 N*N에 0을 넣어준다 , 사과위치는 1

for i in range(K):
    apple_x, apple_y = map(int,s.readline().split())
    arr[apple_x-1][apple_y-1]=1
    
snake = deque([])
timeq = deque([])

L = int(s.readline())
time_list=[]

# L을 받고 time_list에 값 저장해둠.
for i in range(L):
    time_number,time_string = list(map(str,s.readline().split()))
    timeq.append((time_number, time_string))
    
# 동,남,서,북 -> 시계방향으로 이동 
dx=[0,1,0,-1]
dy=[1,0,-1,0]

#초기 x,y,d 값 설정 d가 0일경우 동쪽으로 이동
x,y,d = 0,0,0
time =0

while True:
    time +=1
    snake.append((x,y))
    
    x += dx[d]
    y += dy[d]
    
    
    # 범위를 벗어나거나 자신의 몸통을 부딪히면 종료
    if x < 0 or x >= N or y < 0 or y >= N or arr[x][y] == 2:
        break
    
    # 다음 x,y에 사과가 없으면 큐에서 왼쪽꺼빼고 0으로 값 넣어줌
    if not arr[x][y]:
        a,b =snake.popleft()
        arr[a][b]=0
    
    arr[x][y]=2
    # print(type(int(timeq[0][0])))
    if timeq:
        if time == int(timeq[0][0]):
            if timeq[0][1] == 'D':
                d = (d+1)%4
                timeq.popleft()
            else:
                d = (d-1)%4
                timeq.popleft()

print(time)

import sys
from sys import stdin as s
from collections import deque

#s = open('input.txt','rt')

# 스택 객체 생성
q = deque()

n = int(s.readline())

for i in range(n):
    
    command = s.readline().split()
    
    if command[0] =='push':
        q.append(command[1])
        
    elif command[0] =='pop':
        if q:
            print(q.popleft())
            q.popleft
        else:
            print(-1)
    
    elif command[0] =='size':
        print(len(q))
    
    elif command[0] =='front':
        if q:
            print(q[0])
        else:
            print(-1)
    
    elif command[0] =='back':
        if q:
            print(q[-1])
        else:
            print(-1)
    
    elif command[0] =='empty':
        if q:
            print(0)
        else:
            print(1)
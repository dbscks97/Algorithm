import sys
from sys import stdin as s
from collections import deque

#s = open('input.txt','rt')

# 스택 객체 생성
q = deque()

n = int(s.readline())

for i in range(1,n+1):
    q.append(i)





while q:
      
    if len(q)==1:
        print(q[0])
        break
    
    else:
        q.popleft()
        temp =q.popleft()
        q.append(temp)
    

    
    
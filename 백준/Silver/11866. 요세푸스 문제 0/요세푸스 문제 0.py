import sys
from sys import stdin as s
from collections import deque

#s = open('input.txt','rt')

# 스택 객체 생성
q = deque()
n,k= map(int,s.readline().split())


for i in range(1, n + 1):
    q.append(i)
print('<', end='')
while q:
    for i in range(k - 1):
        q.append(q[0])
        q.popleft()
    print(q.popleft(), end='')
    if q:
        print(', ', end='')
print('>')
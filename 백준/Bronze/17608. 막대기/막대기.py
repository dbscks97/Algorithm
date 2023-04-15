import sys
from sys import stdin as s
from collections import deque

#s = open('input.txt','rt')

# 스택 객체 생성
stack = deque()

cnt =0
n = int(s.readline())
max = 0
result=0
for i in range(n):
    stack.append(int(s.readline()))


for i in range(len(stack)):
    if stack:
        max=stack.pop()
        if  max > result:
            cnt += 1
            result =max
        

print(cnt)

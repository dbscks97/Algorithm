import sys
from sys import stdin as s
from collections import deque

#s = open('input.txt','rt')

# 스택 객체 생성
stack = deque()

n = int(s.readline())


for i in range(n):
    
    A = int(s.readline())
    
    if A == 0:
        stack.pop()
    else:
        stack.append(A)

print(sum(stack))
        
    
        
    
from sys import stdin as s
from collections import deque

#s = open('input.txt','rt')


N,K = map(int,s.readline().split())

num = list(s.readline().rstrip())
ans =[]
stack = [] 

for i in num:
    
     
    while stack and K>0 and stack[-1] < i:
        stack.pop()
        K -=1
        
    stack.append(i)
    
if K>0:
    print(''.join(stack[:-K]))
else:
    print(''.join(stack))
    
    
        
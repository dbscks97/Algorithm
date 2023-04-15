import sys
from sys import stdin as s
from collections import deque

#s = open('input.txt','rt')

# 스택 객체 생성
stack = deque()

n = int(s.readline())
for i in range(n):
    A=list(s.readline().strip())
    sum=0
    
    for i in A:
        if i =='(':
            sum +=1
        elif i ==')':
            sum -=1
        if sum<0:
            print('NO')
            break
    
    if sum>0:
        print('NO')
    elif sum ==0:
        print('YES') 


from sys import stdin as s
from collections import deque

n = int(s.readline())
arr = deque()
stack = []
answer= []

for i in range(n):
    num = int(s.readline())
    arr.append(num)
    
while arr:
    for i in range(1,n+1):
        if i <= arr[0]:
            stack.append(i)
            answer.append('+')
        
        while arr and stack and arr[0] <= stack[-1]:
            answer.append('-')
            stack.pop()
            arr.popleft()
    break

if arr:
    print('NO')
else:
    for i in range(len(answer)):
        print(answer[i])
    
    
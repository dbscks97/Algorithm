from sys import stdin as s 
from collections import deque

arr = list(map(str,s.readline().rstrip()))
bomb = list(map(str,s.readline().rstrip()))
answer = []

for i in range(len(arr)):
    answer.append(arr[i])
    
    if ''.join(answer[-len(bomb):]) == ''.join(bomb):
        for _ in range(len(bomb)):
            answer.pop()

if answer:
    print(''.join(answer))
else:
    print('FRULA')
    
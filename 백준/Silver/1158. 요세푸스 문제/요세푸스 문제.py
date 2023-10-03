from sys import stdin as s
from collections import deque

N,K = map(int,s.readline().split())
arr = deque()
result = []

for i in range(1,N+1):
    arr.append(i)

for i in range(N):
    for j in range(1,K+1):
        if j==K:
            result.append(arr.popleft())
        else:
            a = arr.popleft()
            arr.append(a)

print(f'<{", ".join(map(str,result))}>')

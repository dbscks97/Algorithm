from sys import stdin as s
from collections import deque

ans = deque()
N = int(s.readline())

for i in range(1,N+1):
    ans.append(i)

while(len(ans)>1):
    ans.popleft()
    a = ans.popleft()
    ans.append(a)

print(ans[0])
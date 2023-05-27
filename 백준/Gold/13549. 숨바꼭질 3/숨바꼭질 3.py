from sys import stdin as s
from collections import deque
N,K = map(int,s.readline().split())
q=deque()
q.append(N)
MAX=100001
v=[-1 for _ in range(MAX)]
v[N]=0

while q:
    s = q.popleft()
    
    if 0<=s-1<MAX and v[s-1]==-1:
        v[s-1]=v[s]+1
        q.append(s-1)
    if 0<=s*2<MAX and v[s*2]==-1:
        v[s*2]=v[s]
        q.append(s*2)
    if 0<=s+1<MAX and v[s+1]==-1:
        v[s+1]=v[s]+1
        q.append(s+1)

print(v[K])

        
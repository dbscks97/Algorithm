from collections import deque
import sys
from sys import stdin as s
sys.setrecursionlimit(10**6)


def bfs(s):
    global answer 
    q = deque()
    q.append(s)
    v[s]=1
    distance[s]=0
    
    while q:
        c = q.popleft()
        
        for n in arr[c]:
            if not v[n]:
                q.append(n)
                v[n] = 1
                distance[n] = distance[c]+1
                if distance[n]==K:
                    answer.append(n)
            
if __name__=='__main__':
    
    N,M,K,X= map(int,s.readline().split())
    v = [0] * (N+1)
    distance = [0] * (N+1)
    arr = [[]for _ in range(N+1)]
    answer = []
    for i in range(1,M+1):
        A,B = map(int,s.readline().split())
        arr[A].append(B)
    
    
    bfs(X)
    answer.sort()
    if answer:
        for i in answer:
            print(i)
    else:
        print(-1)
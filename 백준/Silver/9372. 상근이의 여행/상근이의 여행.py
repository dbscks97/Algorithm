from sys import stdin as s
from collections import deque
def bfs(x):
    global cnt
    q=deque()
    q.append(x)
    v[x]=1
    
    while q:
        if sum(v)==N:
            print(cnt)
            break
        c = q.popleft()
        for n in arr[c]:
            if not v[n]:
                v[n]=1
                q.append(n)
                cnt+=1


if __name__=='__main__':
    T = int(s.readline())
    
    for i in range(T):
        N,M = map(int,s.readline().split())
        arr=[[] for _ in range(N+1)]
        cnt=0
        v=[0] * (N+1)
        for i in range(M):
            a,b = map(int,s.readline().split())
            arr[a].append(b)
            arr[b].append(a)
        
        bfs(1)
            
from collections import deque
from sys import stdin as s


def dfs(start,end):
    global cnt
    global answer
    v[start]=1
    
    if start==end:
        answer = cnt
    
    
    
    for n in arr[start]:
        if not v[n]:
            v[n]=1
            cnt+=1
            dfs(n,end)
            cnt-=1
            
if __name__=='__main__':
    
    N = int(s.readline())
    A,B = map(int,s.readline().split())
    M = int(s.readline())
    cnt =0
    answer =0
    arr = [[] for _ in range(N+1)]
    v = [0] * (N+1)
    for i in range(1,M+1):
        x,y = map(int,s.readline().split())
        arr[x].append(y)
        arr[y].append(x)

    dfs(A,B)

    if answer==0:
        print(-1)
    else:
        print(answer)
    
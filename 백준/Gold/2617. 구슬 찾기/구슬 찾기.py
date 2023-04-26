from sys import stdin as s
from collections import deque

def dfs(arr,n):
    global cnt
    v[n]=1
    
    for i in arr[n]:
        if not v[i]:
            v[i]=1
            cnt+=1
            dfs(arr,i)

if __name__=='__main__':
    N,M = map(int,s.readline().split())
    light_graph=[[] for _ in range(N+1)]
    heavy_graph=[[] for _ in range(N+1)]
    mid = (N+1)/2
    answer=0
    
        
    for i in range(M):
        A,B = map(int,s.readline().split())
        light_graph[A].append(B)
        heavy_graph[B].append(A)
        
    for i in range(1,N+1):
        v=[[]for _ in range(N+1)]
        
        cnt =0
        dfs(heavy_graph,i)
        if cnt>=mid:
            answer+=1
            
        cnt=0
        dfs(light_graph,i)
        if cnt>=mid:
            answer+=1
    
    print(answer)
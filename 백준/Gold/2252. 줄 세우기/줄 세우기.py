from sys import stdin as s
from collections import deque

def topology():
    q=deque()
    answer = []
    
    for i in range(1,N+1):
        if in_degree[i]==0:
            q.append(i)
    
    while q:
        c = q.popleft()
        answer.append(c)
        
        for n in graph[c]:
            in_degree[n]-=1
            if in_degree[n]==0:
                q.append(n)
        
    for ans in answer:
        print(ans,end=' ')

if __name__=='__main__':
    
    N,M = map(int,s.readline().split())
    in_degree=[0]*(N+1)
    graph=[[] for _ in range(N+1)]
    
    for i in range(M):
        A,B = map(int,s.readline().split())
        graph[A].append(B)
        in_degree[B]+=1
    
    topology()

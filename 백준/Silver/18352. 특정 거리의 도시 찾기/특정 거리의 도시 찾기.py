from sys import stdin as s
from collections import deque


def bfs(c):
    q=deque()
    q.append(c)
    visit[c]=1
    distance[c]=0
    answer =[]
    while q:
        s = q.popleft()
        
        for n in adj[s]:
            if not visit[n]:
                visit[n]=1
                q.append(n)
                distance[n] = distance[s]+1
                if distance[n] == K:
                    answer.append(n)
    if len(answer)==0:
        print(-1)
    else:
        answer.sort()
        for i in answer:
            print(i,end='\n')
    

if __name__=='__main__':
    
    N,M,K,X = map(int,s.readline().split())
    
    adj=[[]for _ in range(N+1)]
    visit = [0] *(N+1)
    distance = [0] * (N+1)
    
    for i in range(1,M+1):
        A,B= map(int,s.readline().split())
        adj[A].append(B)
    
    
    bfs(X)
    
    
    
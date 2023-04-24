import sys
from sys import stdin as s
from collections import deque
sys.setrecursionlimit(10000)



def bfs(s):
    q = deque()
    q.append(s)
    visit[s]=1
    
    while q:
        c = q.popleft()
        for n in adj[c]:
            if not visit[n]:
                visit[n]= -visit[c]
                q.append(n)
            else:
                if visit[n] == visit[c]:
                    return False
    return True

if __name__=='__main__':
    
    K = int(s.readline())
    
    for i in range(K):
        V,E = map(int,s.readline().split())
        adj= [[]for _ in range(V+1)]
        visit= [0]*(V+1)
        ans_bfs=0    
        flag=1
        for j in range(E):
            u,v =map(int,s.readline().split())
            adj[u].append(v)
            adj[v].append(u)
        
        
        for i in range(1,V+1):
            if visit[i] == 0:
                if not bfs(i):
                    flag = -1
                    break
        print('YES' if flag == 1 else 'NO')

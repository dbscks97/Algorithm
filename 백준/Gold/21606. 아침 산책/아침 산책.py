from sys import stdin as s

def dfs(c):
    global cnt
    
    visit[c]=1
    
    for n in adj[c]:
        if not visit[n] and check[n]==1:
            visit[n]=1
            cnt+=1
        elif not visit[n] and check[n]==0:
                visit[n]=1
                dfs(n)
    
if __name__=='__main__':
    
    N = int(s.readline())
    
    A = list(map(int,s.readline().strip())) #A[1]의 값이 0
    
    adj=[[]for _ in range(N+1)]
    for i in range(N-1):
        u,v = map(int,s.readline().split())
        adj[u].append(v)
        adj[v].append(u)
    
    check =[0]
    for i in A:
        check.append(i)
    

    cnt = 0

    for i in range(1,N+1):
        visit=[0]*(N+1)
        if check[i]==1:
            dfs(i)
    
    print(cnt)
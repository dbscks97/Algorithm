from sys import stdin as s

def dfs(c):
    global cnt
    v[c]=1  #초기값 방문표시
    
    for n in arr[c]:
        if not v[n]:
            v[n]=1
            cnt+=1
            dfs(n)
            
if __name__=='__main__':
    
    V = int(s.readline())
    E = int(s.readline())
    
    arr = [[]for _ in range(V+1)]
    v = [0]* (V+1)
    cnt =0
    for i in range(E):
        A,B = map(int,s.readline().split())
        arr[A].append(B)
        arr[B].append(A)
    
    dfs(1)
    print(cnt)
import sys

a,b = map(int,sys.stdin.readline().split())


s = []

visited = [False] * a

def sol(depth,a,b):
    
    if len(s) == b:
        print(' '.join(map(str,s)))
        return 

    for i in range(a):
        if not visited[i]:
            visited[i]=True
            s.append(i+1)
            sol(depth+1,a,b)
            s.pop()
            visited[i]=False                        
        
sol(0,a,b)
            
import sys

def dfs(start):
    global cnt
    
    if sum(s) ==  b and len(s)>0:
        cnt+=1    
    
    for i in range(start,a):
            s.append(n_list[i])
            dfs(i+1)
            s.pop()
            
    return cnt
    
    
a,b = map(int,sys.stdin.readline().split())

s = []
cnt = 0 


n_list = list(map(int,sys.stdin.readline().split()))
    

dfs(0)
print(cnt)


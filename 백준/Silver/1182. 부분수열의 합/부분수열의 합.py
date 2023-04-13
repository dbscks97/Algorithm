from sys import stdin as s
import sys

sys.setrecursionlimit(10**6)



def dfs(start,li):
    global cnt
    
    if sum(li)==b and len(li)>0:
        cnt+=1
            
    for i in range(start,a):
        li.append(c[i])
        dfs(i+1,li)
        li.pop()


if __name__=='__main__':
    
    a,b = map(int,s.readline().split())
    c = list(map(int,s.readline().split()))
    
    cnt =0
        
    dfs(0,[])
    print(cnt)
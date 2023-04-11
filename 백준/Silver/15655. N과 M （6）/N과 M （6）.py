# 중복된 값 제거할때는 함수인자에 start값을 넣어주고 재귀함수호출할때 인자에 i+1값 넣어주기

import sys

a,b = map(int,sys.stdin.readline().split())
n_list = list(map(int,sys.stdin.readline().split()))

n_list.sort()
visited = [False]*a
s = []

def sol(depth,a,b,start):
        
    if depth == b:
       
        print(' '.join(map(str,s)))
        return 

    for i in range(start,a):
        if not visited[i]:
            visited[i]=True
            s.append(n_list[i])
            sol(depth+1,a,b,i+1)
            s.pop()
            visited[i]=False
                
        
sol(0,a,b,0)            
            

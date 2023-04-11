# 이미 sort가 되있으니 전 값과 다음넣을 값이 같다면 붙어있다.
# 지금 넣는 값을 확인할 over 변수에 값을 넣은 다음에 다음 값을 넣을때 if문으로 비교를해서 값이 같으면 탈출

# start값 넣어서 뒤로갈수록 값이 커지게끔

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
    over = 0
    for i in range(start,a):
        if not visited[i] and over != n_list[i]:
            visited[i]=True
            s.append(n_list[i])
            over = n_list[i]
            sol(depth+1,a,b,i+1)
            s.pop()
            visited[i]=False
                
        
sol(0,a,b,0)            
            
            

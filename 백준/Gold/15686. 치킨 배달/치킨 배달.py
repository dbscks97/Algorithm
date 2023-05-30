from sys import stdin as s

def dfs(cur,arr):
    global answer
    if len(arr) == M:
        result=0
        for x,y in house:
            min_dist =float('inf')
            for ix,iy in arr:
                dist = abs(x-ix)+abs(y-iy)
                min_dist = min(min_dist,dist)
            result+=min_dist
        answer = min(answer,result)
        return
        
    
    if cur == len(chicken):
        return
    
    dfs(cur+1, arr+[chicken[cur]])
    dfs(cur+1, arr)
        
if __name__=='__main__':
    N,M =map(int,s.readline().split())
    arr = [list(map(int,s.readline().split())) for _ in range(N)]
    answer=float('inf')
    chicken =[]
    house=[]
    
    for i in range(N):
        for j in range(N):
            if arr[i][j]==1:
                house.append((i,j))
            if arr[i][j]==2:
                chicken.append((i,j))
    dfs(0,[])
    print(answer)
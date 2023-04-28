from sys import stdin as s

T = int(s.readline())

for i in range(T):
    N = int(s.readline())
    
    arr = [list(map(int,s.readline().split())) for _ in range(N)]
    arr.sort(key=lambda x:x[0])
    cnt =1 
    min = arr[0][1]
    
    for i in range(1,N):
        if arr[i][1] <min:
            min = arr[i][1]
            cnt+=1
    
    print(cnt)

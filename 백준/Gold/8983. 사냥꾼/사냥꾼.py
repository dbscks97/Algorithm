from sys import stdin as s

#s = open('input.txt','rt')

M,N,L = map(int,s.readline().split())

arr =list(map(int,s.readline().split()))

bird_arr = [list(map(int,s.readline().split())) for _ in range(N)]

arr.sort()

cnt=0


for i,j in bird_arr:
    temp = L-j
    start = 0
    end = len(arr)-1
    
    while start<=end: 
        mid = (start + end)//2
        
        
        if arr[mid] < i-temp:
            start = mid + 1
        
        elif arr[mid] > i+temp:
            end = mid - 1
        
        else:
            cnt +=1        
            break
    
print(cnt)
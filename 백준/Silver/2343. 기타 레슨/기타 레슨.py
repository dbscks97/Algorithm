from sys import stdin as s

N, M = map(int, s.readline().split())
arr = list(map(int, s.readline().split()))

answer = []
start, end = max(arr), sum(arr)

while(start<=end):
    count=1
    result = 0
    mid = (start + end) //2

    for i in range(N):

        if result + arr[i] > mid:
            count+=1
            result=0
        
        result += arr[i]
            
    if count>M:
        start = mid +1
    else:
        end = mid -1 
          
print(start)


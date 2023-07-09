from sys import stdin as s

N = int(s.readline())
K = int(s.readline())

start = 1
end = 100000000000

while(start<=end):
    mid = (start + end) // 2
    result = 0
    
    if mid > N*N:
        end = mid-1
        continue
    
    for i in range(1,N+1):
        result += min((mid // i) , N )
    
    if result<K:
        start = mid +1
    else:
        end = mid -1
    
print(start)



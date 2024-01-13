from sys import stdin as s
import heapq

N,M,K = map(int,s.readline().split())

arr = [list(map(int,s.readline().split()))for _ in range(K)]
arr.sort(key=lambda x:(x[1]))
heap=[]
result = 0
answer =0 
for v,c in arr:
    result += v
    heapq.heappush(heap,v)
    
    if len(heap)==N:
        if result >= M:
            answer = c
            break
        else:
            result -= heapq.heappop(heap)

if answer:
    print(answer)
else:
    print(-1)


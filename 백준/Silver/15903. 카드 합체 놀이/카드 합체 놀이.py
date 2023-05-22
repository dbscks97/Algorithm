from sys import stdin as s
import heapq as hq

n,m=map(int,s.readline().split())
card = list(map(int,s.readline().split()))
heap =[]
for i in range(n):
    hq.heappush(heap,card[i])


for i in range(m):
    a=hq.heappop(heap)
    b=hq.heappop(heap)
    c=a+b
    hq.heappush(heap,c)
    hq.heappush(heap,c)

print(sum(heap))
    


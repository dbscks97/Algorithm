from sys import stdin as s
import heapq as hq

#s = open('input.txt','rt')

heap = []
result =[]
N = int(s.readline())

# hq.heappush(leftheap,(-x,x))
for i in range(N):
    x = int(s.readline())
    hq.heappush(heap,x)

if heap:
    for i in range(N-1):
        a=hq.heappop(heap)
        b=hq.heappop(heap)
        result.append(a+b)
        c= a+b
        hq.heappush(heap,c)

        

        

print(sum(result))
        
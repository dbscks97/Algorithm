import sys
from sys import stdin as s
import heapq as hq

#s = open('input.txt','rt')


n = int(s.readline())

heap = []

for i in range(n):
    
    x = int(s.readline())
    
    if x == 0:
        if heap:
            print(hq.heappop(heap))
        else:
            print(0)
    else:
        hq.heappush(heap,x)
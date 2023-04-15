import sys
from sys import stdin as s
import heapq as hq
#s = open('input.txt','rt')

n = int(s.readline())

heap= []


for i in range(n):
    x = int(s.readline())
    
    if x == 0:
        if heap:
            print(hq.heappop(heap)[1])
        else:
            print(0)
        
    elif x >0:
        hq.heappush(heap,(-x,x))

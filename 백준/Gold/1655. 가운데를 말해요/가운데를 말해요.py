from sys import stdin as s
import heapq as hq

#s = open('input.txt','rt')


n = int(s.readline())

leftheap = []
rightheap = []

for i in range(n):
    
    x = int(s.readline())
    
    if len(leftheap) == len(rightheap):
        hq.heappush(leftheap,(-x,x))
        
    else:
        hq.heappush(rightheap,(x,x))
        
        
    if  leftheap and rightheap and leftheap[0][1]>rightheap[0][1]:
        right_min, d = hq.heappop(rightheap)
        left_max, v = hq.heappop(leftheap)   
        hq.heappush(leftheap,(-d,d))
        hq.heappush(rightheap,(v,v))
    
    
    print(leftheap[0][1])
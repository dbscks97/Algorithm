from sys import stdin as s
import sys



def tree(arr,M):
    global result
    start = 0
    end = max(arr)
    
    while start <= end:
        mid = (start + end) //2
        
        total = 0
        
        for i in arr:
            if i > mid:
                total += i-mid    
        
        if total<M:
            end = mid -1
        else:
            result = mid
            start = mid+1
            
        

if __name__=='__main__':
    
    N,M = map(int,s.readline().split())
    
    arr = list(map(int,s.readline().split()))
    result = 0
    
    tree(arr,M)
    print(result)
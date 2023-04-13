import sys

a = int(sys.stdin.readline())
N = a
cnt=0
    
for i in range(100):      
        x = N // 10
        y = N % 10
        z = (x+y)%10
        N = (y*10) + z
        cnt += 1    
            
        if N == a:
            break   
    
print(cnt) 
        
        
    
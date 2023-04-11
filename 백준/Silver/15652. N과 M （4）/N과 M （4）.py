import sys

a,b = map(int,sys.stdin.readline().split())

s = []

def sol(start):
    
    if len(s) == b:
        print(' '.join(map(str,s)))
        return 

    else:
        for i in range(start,a+1):
                s.append(i)
                sol(i)
                s.pop()
                
                
                
        
sol(1)
          
import sys

a,b = map(int,sys.stdin.readline().split())

s = []

def sol():
    
    if len(s) == b:
        print(' '.join(map(str,s)))
        return 

    else:
        for i in range(1,a+1):
            if i not in s:
                s.append(i)
                sol()
                s.pop()
        
sol()
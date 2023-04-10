import sys

N,R,C = map(int,sys.stdin.readline().split())

result = 0

def z(n,r,c):
    global result

    if r==R and c==C:
        print(result)
        exit(0)
    
    if not (R<n+r and C<n+c):
        result += n*n 
        return
    
    z(n//2,r,c)
    z(n//2,r,c+n//2)
    z(n//2,r+n//2,c)
    z(n//2,r+n//2,c+n//2)
    
      
z(2**N,0,0)
    

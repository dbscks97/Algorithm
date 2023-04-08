import sys
T = int(sys.stdin.readline())
prime_list = []

for n in range(2,10000):
    for i in range(2,int(n**0.5)+1):
        if n%i ==0:
            break
    else:
        prime_list.append(n)
        
for i in range(1,T+1):
    n = int(sys.stdin.readline())
    half = n//2
    for j in range(half,1,-1):
        if(j in prime_list) and (n-j in prime_list):
            print(j, n-j)
            break
            
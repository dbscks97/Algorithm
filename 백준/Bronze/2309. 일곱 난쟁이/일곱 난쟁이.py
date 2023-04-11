import sys

n = []

for i in range(9):
    n.append(int(sys.stdin.readline()))
    
total = sum(n)


for i in range(0,9):
    for j in range(1,9):
        if total - n[i] - n[j]  == 100:   
            n.remove(n[i])
            n.remove(n[j-1])
            n.sort()
            
            for k in n:
                print(k)
                
            exit()
            
        


        
from sys import stdin as s

N,M = map(int,s.readline().split())
arr = [list(map(str,s.readline().strip())) for _ in range(N)]

answer=[]
for i in range(N-7):
    for j in range(M-7):
        count_1=0
        count_2=0
        for k in range(i,i+8):
            for z in range(j,j+8):
                if (k+z)%2==0:
                    if arr[k][z]!='W':
                        count_1+=1
                    if arr[k][z] !='B':
                        count_2+=1
                else:
                    if arr[k][z]!='B':
                        count_1+=1
                    if arr[k][z] !='W':
                        count_2+=1
                        
                        
        answer.append(min(count_1,count_2))

print(min(answer))
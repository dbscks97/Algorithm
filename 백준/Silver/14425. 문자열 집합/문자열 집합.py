from sys import stdin as s

N,M = map(int,s.readline().split())
N_arr=[]
M_arr=[]
count=0
for i in range(N):
    a = str(s.readline().strip())
    N_arr.append(a)


for i in range(M):
    b = str(s.readline().strip())
    M_arr.append(b)


for i in M_arr:
    if i in N_arr:
        count +=1

print(count)
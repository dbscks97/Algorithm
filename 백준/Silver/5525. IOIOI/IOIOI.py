from sys import stdin as s
N=int(s.readline())
M=int(s.readline())
arr=list(map(str,s.readline()))

correct = ['I'] + ['O','I']*N
cnt=0

for i in range(M-2):
    if arr[i:len(correct)+i] == correct:
        cnt+=1

print(cnt)
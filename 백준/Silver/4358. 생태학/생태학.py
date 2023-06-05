from sys import stdin as s
from collections import Counter

arr=[]
cnt=0

while(True):
    word = s.readline().rstrip()
    if not word:
        break
    
    arr.append(word)
    cnt+=1

arr = sorted(Counter(arr).items())

for i in range(len(arr)):
    print(arr[i][0],"{:.4f}".format(arr[i][1]/cnt*100))
from sys import stdin as s

N = int(s.readline())
arr = []

result=0

for i in range(N):
    a = int(s.readline())
    arr.append(a)

arr.sort()
      

for i in range(1,len(arr)+1):
    result += abs(i - arr[i-1])

print(result)
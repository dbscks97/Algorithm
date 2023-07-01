from sys import stdin as s

n = s.readline()
arr = list(map(int,s.readline().strip()))
result = 0

for i in range(len(arr)):
    result += arr[i]

print(result)    
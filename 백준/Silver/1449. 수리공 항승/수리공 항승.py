from sys import stdin as s
from collections import deque

N,L = map(int,s.readline().split())
arr = list(map(int,s.readline().split()))
arr.sort()
count =0
result_min=0
result_max=0
for i in arr:
    if result_min <= i <= result_max:
        continue
    result_min = i - 0.5
    result_max = result_min+L
    count+=1

print(count)
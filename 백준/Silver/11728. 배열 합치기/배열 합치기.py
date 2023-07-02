from sys import stdin as s

N,M = map(int,s.readline().split())

arr_N = list(map(int,s.readline().split()))
arr_M = list(map(int,s.readline().split()))

arr_result = arr_N + arr_M
sorted_list = arr_result.sort()

print(*arr_result)
    
    
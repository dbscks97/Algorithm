from sys import stdin as s
result = 0
cnt = 0
A,B = map(int,s.readline().split())

arr_A = list(map(int,s.readline().split()))
arr_B = list(map(int,s.readline().split()))

len_A = len(arr_A + arr_B)
len_B = len((set(arr_A + arr_B)))

result_A = len_A -len_B
print(len_B - result_A)

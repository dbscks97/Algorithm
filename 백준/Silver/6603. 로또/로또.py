from sys import stdin as s
from itertools import combinations

while(1):
    arr = list(map(int,s.readline().split()))

    if arr[0] == 0:
        break

    else:
        result = combinations(arr[1:],6)
        result_list = list(result)
        for i in result_list:
            print(*i)
            
        print("")
    


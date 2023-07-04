from sys import stdin as s 
from itertools import permutations

n = int(s.readline())
string = []

for i in range(1,n+1):
    string.append(i)

permutations_list = permutations(string)

for permutation in permutations_list:
    print(*permutation)



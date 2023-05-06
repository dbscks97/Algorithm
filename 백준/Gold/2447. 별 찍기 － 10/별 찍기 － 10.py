#분할 정복 알고리즘(재귀) O(NlogN) 
from sys import stdin as s

n = int(s.readline())
def star(l):
    if l == 3:
        return ['***','* *','***']

    arr = star(l//3)
    stars = []

    for i in arr:
        stars.append(i*3)

    for i in arr:
        stars.append(i+' '*(l//3)+i)

    for i in arr:
        stars.append(i*3)

    return stars

print('\n'.join(star(n)))
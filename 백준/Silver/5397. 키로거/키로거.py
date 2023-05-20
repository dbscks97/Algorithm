from sys import stdin as s

N = int(s.readline())

arr = [list(map(str, s.readline().strip())) for _ in range(N)]

for i in range(N):
    left = []
    right = []
    for j in range(len(arr[i])):
        if arr[i][j] =='<':
            if left:
                right.append(left.pop())
        
        elif arr[i][j] =='>':
            if right:
                left.append(right.pop())

        elif arr[i][j] =='-':
            if left:
                left.pop()
        else:
            left.append(arr[i][j])
    left.extend(reversed(right))
    print(''.join(left))
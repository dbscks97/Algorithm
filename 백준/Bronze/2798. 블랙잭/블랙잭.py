from sys import stdin as s
import sys

def dfs(index, count, sum):
    global result

    if count == 3:
        if sum <= m:
            result = max(result, sum)
        return

    if index >= n:
        return

    dfs(index+1, count+1, sum+cards[index])
    dfs(index+1, count, sum)

if __name__ == '__main__':
    n, m = map(int, s.readline().split())
    cards = list(map(int, s.readline().split()))
    result = 0

    dfs(0, 0, 0)
    print(result)
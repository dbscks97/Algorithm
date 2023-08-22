from sys import stdin as s
from collections import deque


def solution(n, computers):
    answer = 0
    v = [0] * n
    
    def bfs(start, v, computers):
        v[start] = 1
        q = deque([start]) 

        while q:
            c = q.popleft()
            for i in range(n):
                if computers[c][i] == 1 and not v[i]:
                    v[i] = 1
                    q.append(i)
                    
    for i in range(n):
        if not v[i]:
            bfs(i, v, computers)
            answer += 1
    
    return answer
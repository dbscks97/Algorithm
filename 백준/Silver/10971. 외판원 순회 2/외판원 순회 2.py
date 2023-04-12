# start는 현재 노드, x 는 방문한 노드의 수 , cost는 현재까지 경로에서 사용된 비용
# x의 수와 n의수가 같아지면 전체 노드를 방문한 것이므로 최소값 출력

import sys


def dfs(start,x,cost):
    global answer
    if x == n:
        if n_list[start][0]:
            answer = min(answer, cost + n_list[start][0])
            return
    
    for i in range(1, n):
        if  not visited[i] and n_list[start][i]:
            visited[i] = True
            dfs(i, x + 1, cost + n_list[start][i])
            visited[i] = False
            


if __name__ == '__main__':
    
    n = int(sys.stdin.readline())
    visited = [False]* n
    answer = 1e9
    n_list = []
    
    for i in range(n):
        n_list.append(list(map(int,sys.stdin.readline().split())))
        

dfs(0,1,0)
print(answer)

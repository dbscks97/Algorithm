import sys



def solve(li):
    global answer
    
    if len(li) == n:
        total = 0
        for i in range(n-1):
            total += abs(li[i]-li[i+1])
        answer = max(answer,total)
        return
        
    for i in range(n):
        if not visited[i]:
            visited[i]=True
            li.append(n_list[i])
            solve(li)
            li.pop()
            visited[i]=False
        


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    n_list = list(map(int,sys.stdin.readline().split()))
    visited = [False] * n
    li = []
    answer = 0
    
solve([])
print(answer)
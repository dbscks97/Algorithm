from sys import stdin as s

#s = open('input.txt','rt')

def find_parent(x):
    if parent[x] == x:
        return x    
    parent[x] = find_parent(parent[x])
    return parent[x]
    

def union_parent(A,B):
    A = find_parent(A)
    B = find_parent(B)
    
    if A<B:
        parent[B]=A
    else:
        parent[A]=B


if __name__=='__main__':
    V,E = map(int,s.readline().split())
    
    #부모 테이블상에서, 부모를 자기 자신으로 초기화
    parent = [i for i in range(V+1)]
    answer = 0
    edges=[]
    for i in range(E):
        A,B,C = map(int,s.readline().split())
        edges.append((A,B,C))
    edges.sort(key=lambda x: x[2])
    
    for A,B,C in edges:    
        if find_parent(A) != find_parent(B):
            union_parent(A,B)
            answer += C 
    
    print(answer)   
    
    

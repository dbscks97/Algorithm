from sys import stdin as s

#s = open('input.txt','rt')


def find_parent(x):
    if parent[x] == x:
        return x
    else:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union(A,B):
    A=find_parent(A)
    B=find_parent(B)
    
    if A<B:
        parent[B]=A
    else:
        parent[A]=B
        

if __name__=='__main__':
    
    N = int(s.readline())
    M = int(s.readline())
    parent = [i for i in range(N+1)]
    edge =[]
    
    for i in range(M):
        A,B = map(int,s.readline().split())
        edge.append((A,B))
    # edge.sort()
    
    edge.sort(key=lambda x:x[1])
    for i in range(2):
        for i,j in edge:
            if find_parent(i) != find_parent(j):
                union(i,j) 
       
    print(parent.count(1)-1)
    
            
    
    
from sys import stdin as s

#s = open('input.txt','rt')


def find_parent(x):
    if parent[x] == x:
        return x
    else:
       parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(A,B):
    A=find_parent(A)
    B=find_parent(B)
    
    if A<B:
        parent[B]=A
    else:
        parent[A]=B
                       
if __name__=='__main__':
    
    V,E = map(int,s.readline().split())
    
    edge = []
    answer =0 
    
    parent =[i for i in range(V+1)]
    
    for i in range(E):
        A,B,C = map(int,s.readline().split())
        edge.append((A,B,C))
    edge.sort(key=lambda x:x[2])
    
    for A,B,C in edge:
        if find_parent(A) != find_parent(B):
            union_parent(A,B)
            answer += C
    
    print(answer)    

        
    
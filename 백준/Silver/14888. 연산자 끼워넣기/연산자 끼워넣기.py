from sys import stdin as s

def dfs(c):
    global answer
    global resultMax
    global resultMin
    
    if c==N:
        if answer>resultMax:
            resultMax=answer
            
        if answer<resultMin:
            resultMin=answer
        return
    
    for i in range(4):
        temp = answer
        if op[i]>0:
            if i==0:
                answer += adj[c]
            elif i==1:
                answer -= adj[c]
            elif i==2:
                answer *= adj[c]
            elif i==3:
                if answer>=0:
                    answer//=adj[c]
                else:
                    answer = (-answer//adj[c])*-1
            op[i]-=1
            dfs(c+1)
            answer=temp
            op[i]+=1                                                   

if __name__=='__main__':
    
    N = int(s.readline().strip())
    adj = list(map(int,s.readline().strip().split()))
    op =list(map(int,s.readline().strip().split()))
    resultMax = -2e9
    resultMin = 2e9
    answer=adj[0]
    
    dfs(1)
    
    print(resultMax)
    print(resultMin)

        
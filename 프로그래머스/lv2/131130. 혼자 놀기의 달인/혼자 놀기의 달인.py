def solution(cards):
    answer = 0
    length = len(cards)
    v=[0]*length
    ans=[[] for _ in range(length+1)]
    result=[]
    count=0
        
    def dfs(si):
        v[si]=1
        c=cards[si]
        ans[count].append(c)
        if not v[c-1]:            
            dfs(c-1)
        
            
    for i in range(length):
        if not v[i]:
            dfs(i)
            count+=1
    for an in ans:
        result.append(len(an))
    res = sorted(result,reverse=True)
    answer = res[0] * res[1]
    return answer
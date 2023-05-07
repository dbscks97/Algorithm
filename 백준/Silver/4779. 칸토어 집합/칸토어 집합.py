from sys import stdin as s

def func(n):
    if n ==0:
        return ['-']
        
    if n == 1:
        return ['-',' ','-']
    
    arr = func(n-1)
    ans = []
    
    for i in range(len(arr)):
        ans.append(arr[i])
    for i in range(len(arr)):
        ans.append(' ')
    for i in range(len(arr)):
        ans.append(arr[i])

    return ans
if __name__=='__main__':
    while True:
        try:
            n = int(s.readline())
            result =func(n)
            
            print(''.join(result))
        except:
            break    

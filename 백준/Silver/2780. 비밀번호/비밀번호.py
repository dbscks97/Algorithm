from sys import stdin as s

N = int(s.readline())
arr = [[0]*(10) for _ in range(N+1)]    
dp = [0]*(N+1)


for i in range(1,N+1):
    T = int(s.readline())

    if T==1:
            arr[1][0]=1
            arr[1][1]=1   
            arr[1][2]=1
            arr[1][3]=1
            arr[1][4]=1
            arr[1][5]=1
            arr[1][6]=1
            arr[1][7]=1
            arr[1][8]=1
            arr[1][9]=1
    
    else:
            arr[T][0] = arr[T-1][7]
            arr[T][1] = arr[T-1][2] + arr[T-1][4]
            arr[T][2] = arr[T-1][1] + arr[T-1][3] + arr[T-1][5]
            arr[T][3] = arr[T-1][2] + arr[T-1][6]
            arr[T][4] = arr[T-1][1] + arr[T-1][5] + arr[T-1][7]
            arr[T][5] = arr[T-1][2] + arr[T-1][4] + arr[T-1][6] + arr[T-1][8]
            arr[T][6] = arr[T-1][3] + arr[T-1][5] + arr[T-1][9]
            arr[T][7] = arr[T-1][4] + arr[T-1][8] + arr[T-1][0]
            arr[T][8] = arr[T-1][5] + arr[T-1][7] + arr[T-1][9]
            arr[T][9] = arr[T-1][6] + arr[T-1][8]
            
    dp[i] = sum(arr[i]) %1234567
    print(dp[i])

                


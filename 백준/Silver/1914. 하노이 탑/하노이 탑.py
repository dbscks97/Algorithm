def Hanoi(cnt,a,b,c):
    if cnt == 1:
        print(a,c)
    else:
        Hanoi(cnt-1,a,c,b)
        Hanoi(1,a,b,c)
        Hanoi(cnt-1,b,a,c)

cnt = int(input())

print(2**cnt-1)

if cnt<=20:
    Hanoi(cnt,1,2,3)
    

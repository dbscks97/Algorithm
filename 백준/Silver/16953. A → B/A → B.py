from sys import stdin as s

A,B = map(int,s.readline().split())
cnt = 1

while True:
    if B %10 == 1:
        B = B//10
        cnt += 1
        if B==A:
            print(cnt)
            break
    elif B<A or B%2==1:
        print(-1)
        break
    elif B%2 ==0:
        B = B // 2
        cnt +=1

        if B == A:
            print(cnt)
            break


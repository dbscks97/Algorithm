x,y,z = map(int,input().split())

days = (z-y) // (x-y)

if ((z-y) % (x-y)) != 0:
    days += 1


print(days)

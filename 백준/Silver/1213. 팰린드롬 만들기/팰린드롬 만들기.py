import sys
input = sys.stdin.readline

d = dict()
s = input().rstrip()
for i in s:
    if d.get(i) == None:
        d[i] = 1
    else:
        d[i] += 1
        
center = ''
for k,v in d.items():
    if v % 2 == 1:
        if len(center)>0:
            print("I'm Sorry Hansoo")
            break
        center = k
else:
    ans = ''
    for k,v in sorted(d.items()):
        ans+=k*(v//2)
    ans += center + ans[::-1]
    print(ans)
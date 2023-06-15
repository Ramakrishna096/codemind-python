t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    ll=sorted(l)
    c=0
    for i in range(n):
        if l[i]!=ll[i]:
            c=1
    if c==1:
        print(max(l)-min(l))
    else:
        print("0")
    
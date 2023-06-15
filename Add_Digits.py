def add(x):
    s=0
    while x!=0:
        r=x%10
        s=s+r
        x=x//10
    if len(str(s))==1:
        print(s)
    else:
        add(s)


n=int(input())
add(n)
def check(n):
    l=n
    s=0
    sum=0
    s2=0
    while l!=0:
        r=l%10
        s=s*10+r
        l=l//10
    tot=n+s
    m=tot
    while m!=0:
        r1=m%10
        s2=s2*10+r1
        m=m//10
    if s2==tot:
        print(tot)
    else:
        check(tot)

n=int(input())
check(n)
x=int(input())
a=0
b=1
c=0
while True:
    c=a+b
    a=b
    b=c
    if c<x:
        min=c
    else:
        max=c
        break
r1=x-min
r2=max-x
if r1<r2:
    print(min)
elif r1==r2:
    print(min,max)
else:
    print(max)
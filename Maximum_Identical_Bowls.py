n=int(input())
l=list(map(int,input().split()))
s=sum(l)
for i in range(n,0,-1):
    if s%i==0:
        print(i)
        break
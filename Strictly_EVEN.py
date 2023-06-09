n=int(input())
l=list(map(int,input().split()))
k=0
j=0
for i in range(0,n,2):
    if l[i]%2!=0:
        k=1
if k==1:
    print(False)
else:
    print(True)
        
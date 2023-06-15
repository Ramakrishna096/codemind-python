a,b,c=map(int,input().split())
j=0
for i in range(a,b+1):
    if i%c==0:
        j+=1
print(j)
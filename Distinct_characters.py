n=input().lower()
k=list(n)
l=[]
for i in k:
    if i!=" ":
        l.append(i)
k=list(set(l))
k.sort()

for i in range(len(k)):
    print(k[i],end="")
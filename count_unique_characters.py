n=input().lower()
k=list(n)
l=[]
for i in k:
    if k.count(i)==1 and i!=" ":
        l.append(i)
l.sort()
print(len(l))
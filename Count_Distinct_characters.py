n=input().lower()
k=list(n)
l=[]
for i in k:
    if i!=" ":
        l.append(i)
l.sort()
k=set(l)
print(len(k))
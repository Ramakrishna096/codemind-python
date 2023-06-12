n=input()
k=n.split()
lst=[]
for i in k:
    r=list(i)
    k=min(r)
    l=max(r)
    lst.append(k)
    lst.append(l)
print(*lst)
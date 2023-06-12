l1=input().lower().split()
l2=input().lower().split()
l3=[]
for i in l2:
    if i in l1 and i not in l3 and i!=" ":
        l3.append(i)
for i in l1:
    if i in l2 and i not in l3 and i!=" ":
        l3.append(i)
print(len(l3))
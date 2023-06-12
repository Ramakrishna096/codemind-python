n=input().lower()
m=input().lower()
l1=list(n)
l2=list(m)
l3=[]
for i in l2:
    if i in l1 and i not in l3 and i!=" ":
        #l3+=i
        l3.append(i)
for i in l1:
    if i in l2 and i not in l3 and i!=" ":
        #l3+=i
        l3.append(i)
l3.sort()
s=""
#l3=l3.replace(" ","")
for i in l3:
    if i!=" ":
        s+=str(i)
print(len(s))
n=input().split()
r="qwertyuiopasdfghjklzxcvbnm"
for i in n:
    lst=[]
    for j in i:
        if j in r:
            lst.append(j)
    lst.sort()
    k=0
    for l in range(len(i)):
        if i[l] not in r:
            print(i[l],end="")
        else:
            print(lst[k],end="")
            k+=1
    print(end=" ")
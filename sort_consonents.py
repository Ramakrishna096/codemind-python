n=input().split()
for i in n:
    lst=[]
    for j in i:
        if j not in "aeiou":
            lst.append(j)
    lst.sort()
    k=0
    for l in range(len(i)):
        if i[l] in "aeiou":
            print(i[l],end="")
        else:
            print(lst[k],end="")
            k+=1
    print(end=" ")
n=input().split()
c=0
s="AEIOUaeiou"
s1="BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz"
for j in n:
    a=len(j)-1
    for i in range(len(j)//2):
        if j[i] in s and  j[a] in s1:
            c+=1
            a-=1
        elif j[i] in s1 and  j[a] in s:
            c+=1
            a-=1
        else:
            a-=1
print(c)
    
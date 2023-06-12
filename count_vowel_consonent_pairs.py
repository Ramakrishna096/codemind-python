n=input()
#print(n)
c=0
s="AEIOUaeiou"
s1="BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz"
a=len(n)-1
c=0
for i in range(len(n)//2):
    if n[i] in s and  n[a] in s1:
        c+=1
        a-=1
    elif n[i] in s1 and  n[a] in s:
        c+=1
        a-=1
    else:
        a-=1
print(c)
s = input()
a = 'qwertyuiopasdfghjklzxmcnvbQWERTYUIOPALSKDJFHGMZNXBCV'
v = ''
for i in s:
    if i in a:
        v+=i
v=sorted(v)
k=0
for i in s:
    if i not in a:
        print(i,end="")
    else:
        print(v[k],end="")
        k+=1
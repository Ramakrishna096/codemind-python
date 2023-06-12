r,c=map(int,input().split())
mat=[list(map(int,input().split())) for i in range(r)]
#print(mat)
l1=[]
for i in range(c):
    s=0
    for j in range(r):
        s+=mat[j][i]
    l1.append(s)
print(*l1)
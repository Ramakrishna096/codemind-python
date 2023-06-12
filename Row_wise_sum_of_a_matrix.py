r,c=map(int,input().split())
mat=[list(map(int,input().split())) for i in range(r)]
#print(mat)
l1=[]
for i in range(r):
    s=0
    for j in range(c):
        s+=mat[i][j]
    l1.append(s)
print(*l1)
r,c=map(int,input().split())
mat=[list(map(int,input().split())) for i in range(r)]
#print(mat)
rl=[]
cl=[]
for i in range(r):
    s=0
    for j in range(c):
            s+=mat[i][j]
    rl.append(s)

for i in range(c):
    s=0
    for j in range(r):
            s+=mat[j][i]
    cl.append(s)
print((sum(cl)+sum(rl))//2)
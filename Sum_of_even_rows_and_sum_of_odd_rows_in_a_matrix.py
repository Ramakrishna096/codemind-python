r,c=map(int,input().split())
mat=[list(map(int,input().split())) for i in range(r)]
rl=[]
cl=[]
for i in range(r):
    s=0
    for j in range(c):
        if i%2==1:
            s+=mat[i][j]
    rl.append(s)

for i in range(r):
    s=0
    for j in range(c):
        if i%2==0:
            s+=mat[i][j]
    cl.append(s)
print(sum(cl),sum(rl))
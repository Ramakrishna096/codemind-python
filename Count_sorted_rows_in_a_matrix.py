r,c=map(int,input().split())
mat=[list(map(int,input().split())) for i in range(r)]
cnt=0
for i in range(r):
    lst=[]
    for j in range(c):
        lst.append(mat[i][j])
    temp=sorted(lst)
    if temp==lst:
        cnt+=1
    elif temp==lst[::-1]:
        cnt+=1
print(cnt)
r=int(input())
mat1=[list(map(int,input().split())) for i in range(r)]
mat2=[list(map(int,input().split())) for i in range(r)]
s=[]
for i in range(r):
    lst=[]
    for j in range(r):
        lst.append(abs(mat1[i][j]-mat2[i][j]))
    s.append(lst)
for i in s:
    print(*i)
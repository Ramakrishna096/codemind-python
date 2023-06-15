n=int(input())
for i in range(0,n):
    a=int(input())
    fat=1
    for j in range(a,0,-1):
        fat=fat*j
    print(fat)
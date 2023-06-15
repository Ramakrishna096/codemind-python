n=int(input())
l=n
sum=0
while n!=0:
    r=n%10
    fact=1
    for i in range(1,r+1):
        fact=fact*i
    sum=sum+fact
    n=n//10
if sum==l:
    print("The number %d is a strong number"%l)
else:
    print("The number %d is not a strong number"%l)
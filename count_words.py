n=input().lower().split()
b=0
a='aeiou'
for i in n:
    if i[0] in a and i[-1] not in a:
        b+=1
print(b)
        
    
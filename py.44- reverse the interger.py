n=int(input("enter the number"))
x=n
r=0
while n>0:
    d=n%10
    r=r*10+d
    n=n//10
print(" the reversed number is :", r)
a=()
l=[]
n=int(input("enter limit "))
for i in range(0,n):
    item=int(input("enter element "))
    l.append(item)
a=a+tuple (l)
print("tuple is",a)
x=1
y=1
n=int(input("enter the range:"))
for i in range(n):
    if i==0:
        print(x)
    if i==1:
        print(y) 
    else:
        c=x+y
        print(c)
        x=y
        y=c
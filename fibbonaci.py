#fibbonaci series
n=int(input("enter the number"))
a=0
b=1
if n==1:
    print(a)
elif n==2:
    print(a,b)
else:
    for i in range(n):
        c=a+b#c=1,2,3,5
        print(a,end=",")
        a=b#a=1,1,2
        b=c#b=1,2,3

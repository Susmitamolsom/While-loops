n=int(input("enter"))
i=1
a=1
sum=0
while i<=n:
    a=a*i
    sum=sum+a
    print(a,end=" ")
    i=i+1
print(sum)
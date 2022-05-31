n=int(input("enter"))
i=1
sum=0
while i<=n:
    if i%2==0:
        sum=sum+i
        print("+",i*i,end=" ")
    else:
        print("-",i*i,end=" ")
    i=i+1
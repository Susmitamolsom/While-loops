i=1
a=int(input("enter 1st"))
while i<=5:
    b=int(input("enter 2nd"))
    i=i+1
    if b<a:
        print("number enter by you is small")
    elif b>a:
        print("number enter by you is greater")
    elif b==a:
        print("wow you guest the correct number")
        break
else:
    print("wrong number")
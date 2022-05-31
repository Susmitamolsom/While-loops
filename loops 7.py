i=1
a=int(input("enter"))
while i<=5:
    b=int(input("enter number"))
    i=i+1
    if b==a:
        print("you guest right")
        break
else:
    print("wrong guest")
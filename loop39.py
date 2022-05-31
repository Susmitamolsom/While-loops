i=1
a=int(input("enter 1st"))
while i<=a:
    b=int(input("enter"))
    i=i+1
    if b==a:
        print("you guest right")
        break
else:
    print("you guest wrong")
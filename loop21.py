n=int(input("enter"))
for i in range (n-1):
    for j in range (n):
        if i+j==2 or j-i==2 or i==n-3:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
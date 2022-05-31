a=int(input("enter"))
rev=0
temp=a
while temp>0:
    rem=temp%10
    rev=rev*10+rem
    temp=temp//10
print(rev)
if a==rev:
    print("palindrome number")
else:
    print("not palindrome number")
n=input("enter")
i=0
armstrong=0
while i<len(n):
    b=n[i]
    c=(int(b)**3)
    armstrong=c+armstrong
    i=i+1
print(armstrong)
if int(n)==armstrong:
    print("armstrong number")
else:
    print("not armstrong number")
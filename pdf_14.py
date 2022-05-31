n=input("enter")
L=list(n)
i=0
a=["zero","one","two","three","four","five","six","seven","eight","nine"]
while i<len(L):
    print(a[int(L[i])],end=" ")
    i=i+1
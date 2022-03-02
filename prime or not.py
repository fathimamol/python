x=int(input("Enter the number:"))
i=1
c=0
while(i<=x):
    if(x%i==0):
        c=c+1
    i=i+1
if(c==2):
     print("Number is prime")
else:
    print("Number is not prime")

x=int(input("Enter the first number:"))
y=int(input("Enter the second number:"))
while(x<=y):
    i=1
    n=0
    while(i<=n):
        if(n%i==0):
            c=c+1
        i=i+1
    n=n+1
if(c==2):
    print("Prime numbers are=")

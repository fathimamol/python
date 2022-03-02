n=int(input("enter a number:"))
x=n
def armstrong(n):
    a=s=0
    while(n>0):
        a=n%10
        s=s+(a*a*a)
        n=n//10
    return(s)
s=armstrong(n)
if(s==x):
    print("number is armstrong")
else:
    print("number is not armstrong")
            

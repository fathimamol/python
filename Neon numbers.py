n=int(input("enter a number:"))
def neon(b):
    s=a=0
    q=(b**2)
    while(q>0):
        a=q%10
        s=s+a
        q=q//10
    if(s==b):
        print("the inputed number is neon")
    else:
        print("inputed number is not neon")
neon(n)

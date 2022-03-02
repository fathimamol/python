n=int(input("Enter a number:"))
def digits(s):
    sum=0
    while(s>0):
        l=s%10
        sum=sum+l
        s=s//10
    print("Sum of digits=",sum)
digits(n)

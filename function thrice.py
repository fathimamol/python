a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
c=int(input("Enter the third bumber:"))
def sum_of_3(a,b,c):
    s=a+b+c
    if(a==b==c):
        return(3*s)
    else:
        return(s)
print("sum",sum_of_3(a,b,c))


a=int(input("Enter a number:"))
def factors(a):
    for i in range(1,a+1):
        if(a%i==0):
            print("Factors=",i)
factors(a)

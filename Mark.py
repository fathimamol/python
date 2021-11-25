a=int(input("Enter the mark of ADS:"))
b=int(input("Enter the mark of ASE:"))
c=int(input("Enter the mark of MFC:"))
d=int(input("Enter the mark of DCA:"))
e=int(input("Enter the mark of P LAB:"))
total=a+b+c+d+e
avg=(total/5)
if(avg<80):
    print("A GRADE")
elif(avg<60):
    print("B GRADE")
elif(avg<40):
    print("C GRADE")
else:
    print("FAILED")



      
      
      

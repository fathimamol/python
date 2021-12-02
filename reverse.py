n=int(input("Enter a number:"))
s=a=0
while(n>0):
  a=n%10
  s=s*10+a
  n=n//10
print("Reverse=",s)
            
            

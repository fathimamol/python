a=int(input("enter the side of a square"))
area1=lambda a:a*a
x=area1(a)
print(x)
l=int(input("enter the length of a rectangle"))
b=int(input("enter the breadth of a rectangle"))
area2=lambda l,b:l*b
y=area2(l,b)
print(y)
b1=int(input("enter the base of a triangle"))
h=int(input("enter the height of a triangle"))
area3=lambda b1,h:0.5*b1*h
z=area3(b1,h)
print(z)

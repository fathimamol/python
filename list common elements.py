l1=list(input("enter the 1st list"))
l2=list(input("enter the 2nd list"))
def fnlist(l1,l2):
    c=0
    for i in l1:
        for j in l2:
            if(i==j):
                return(True)
if(fnlist(l1,l2)):
    print("common elements exists")
else:
    print("common element does not exist")
                

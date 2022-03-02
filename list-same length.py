first_list=[1,2,3,4,5,8]
second_list=[6,7,8,9,10]
s1=s2=c=0
len1=len(first_list)
len2=len(second_list)
print("Length of list1=",len1)
print("Length of list2=",len2)
if(len1==len2):
    print("Lists have same length")
else:
    print("Lists have different length")
if sum(first_list)==sum(second_list):
    print("Sum of lists are equal")
else:
    print("Sum of lists are not equal")
for i in first_list:
    for j in second_list:
        if i==j:
            c=c+1
            print("Common elements=",i)
if c==0:
    print("Common elements not exist")
else:
    print("Count of common elements=",c)
        

from array import *
arr=array('i',[])  # empty array
a=int(input("enter the size of an array:"))
for j in range(a):
    b=int(input("enter the value %d" %(j)))
    arr.append(b)

print("the values of an array are:")

for j in arr:
    print(j)

key=int(input("enter the key value:"))
m=0
for j in arr:
     if(key==j):
         m=1
         break


if(m==1):
    print("search succesfull")
else:
 print("search unsuccesfull")






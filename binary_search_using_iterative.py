from array import *
x=int(input("enter the array length:"))
arr=array('i',[])
for j in range(x):
    b=int(input("enter the value %d" %(j)))
    arr.append(b)

print("the value of an array:")
for j in arr:
    print(j)
key=int(input("enter the key value:"))
def bsearch():
    low=0
    high=len(arr)-1
    flag=0
    while(low<=high):
        mid=(low+high)//2
        if(arr[mid]==key):
            return mid
        elif(key<arr[mid]):
            high=mid-1
        else:
            low=mid+1
    return -1
result=bsearch()
if result!=-1:
    print("element at %d" %(result))
else:
    print("element not found:")
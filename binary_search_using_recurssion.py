from array import *
arr=array('i',[])
a=int(input("enter the size of an array:"))
#arr=array('i',[])
for j in range(a):
    b=int(input("enter the value:"))
    arr.append(b)

print("the values of an array are:")

for j in arr:
    print(j)
key=int(input("enter the key value:"))

def bsearch(arr,low,high,key):
    if (low < high):
        mid=(low + high)//2
        if(arr[mid]==key):
            return mid
        elif(key<mid):
            return bsearch(arr,low,mid-1,key)
        else:
            return bsearch(arr,mid+1,high,key)
    else:
     return -1
#arr=[10,20,30,40]
#key=40

result=bsearch(arr,0,len(arr)-1,key)

# Test array
#arr = [10,20,30,40]
#x = 50

# Function call
#result = binary_search(arr, 0, len(arr) - 1, key)

if result != -1:
    print("Element is present at index%d" %(result))
else:
    print("Element is not present in array")
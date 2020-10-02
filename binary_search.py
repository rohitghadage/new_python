from array import *
"""arr=array('i',[])
a=int(input("enter the size of an array:"))
#arr=array('i',[])
for j in range(a):
    b=int(input("enter the value:"))
    arr.append(b)

print("the values of an array are:")

for j in arr:
    print(j)
key=int(input("enter the key value:"))"""

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
arr=[10,20,30,40]
key=40

result=bsearch(arr,0,len(arr)-1,key)


# Returns index of x in arr if present, else -1
def binary_search(arr, low, high, x):
    # Check base case
    if high >= low:

        mid = (high + low) // 2

        # If element is present at the middle itself
        if arr[mid] == x:
            return mid

            # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)

            # Else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, high, x)

    else:
        # Element is not present in the array
        return -1


# Test array
arr = [10,20,30,40]
x = 50

# Function call
result = binary_search(arr, 0, len(arr) - 1, x)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")
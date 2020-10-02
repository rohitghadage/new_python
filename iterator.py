"""       using iterator:
list=(1,2,3,4,5)
it=iter(list)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))"""

# USING FOR LOOP:

""" 
list=(1,2,3,4,5)
for i in list:
    print(i)
     here for loop work as iter and next method"""


# using for loop inside the iterator

class mynumber:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        if self.a <= 20:
            x=self.a
            self.a+=1
            return x
        else:
            raise StopAsyncIteration


number=mynumber()
myiter=iter(number)

for x in myiter:
    print(x)









"""
# using generator function
def display():
    yield 1
    yield 2
    yield 3
value=display()
for i in value():
    print(i) """

# using generator object:
# e.g to print square of number upto 10
def sq():
    a=1
    while(a<=10):
        b=a*a
        yield b
        a+=1
value=sq()
print(value.__next__())
print(value.__next__())
print(value.__next__())
print(value.__next__())
print(value.__next__())
print(value.__next__())
print(value.__next__())
#for i in value:
 #   print(i)
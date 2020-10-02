a=5
b=0

try:
    print("start")
    x=int(input("enter the number"))
    print(x)
    print(a/b)
    #print("start")
except ZeroDivisionError as e:
    print("we cant divide number by zero",e)
except ValueError as e:
    print("invalid input",e)
finally:
    print("done")

    a = 5
    b = 0
try:
    print(a/b)
except Exception:
    print("wrong")
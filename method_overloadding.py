# method overloadding:method name same but argument list are different.In python in same class we cant give same method name
# under same class so we wright code in folloowin way
# to add number given as users:

class sum:
    # self.total=0
    def number(self, a=None, b=None, c=None):

        if (a != None and b != None and c != None):
            self.total = a + b + c
            print(self.total)
        elif (a != None and b != None):
            self.total = a + b
            print(self.total)
        else:
            self.total = a
            print(self.total)
        # return self.total


s1 = sum()
s1.number(10, 20, 30)


# method overloadding:method name same but argument list are different.In python in same class we cant give same method name
# under same class so we wright code in folloowin way
# to add number given as users:

class sum:
    # self.total=0
    def number(self, a=None, b=None, c=None):

        if (a != None and b != None and c != None):
            self.total = a + b + c
            print(self.total)
        elif (a != None and b != None):
            self.total = a + b
            print(self.total)
        else:
            self.total = a
            print(self.total)
        # return self.total


s1 = sum()
s1.number(10, 20)



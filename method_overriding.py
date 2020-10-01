# METHOD OVERRIDDING:
# to overcome overiding we use super keyword

"""class A:
    def display(self):
        print("in class A")
class B(A):
    def display(self):
        print("in class B")
a=B()
a.display() """

# using super keyword

class A:
    def display(self):
        print("in class A")
class B(A):
    def display(self):
        super().display()
        print("in class B")
a=B()
a.display()
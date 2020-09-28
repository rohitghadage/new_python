class polygon:
    def __init__(self, sides):
        self.a = sides
        print("sides of an tringle={}".format(self.a))

    def sides(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def display_side(self):
        print("side1={}\nside2={}\nside3={}".format(self.side1, self.side2, self.side3))


class tringle(polygon):
    def __init__(self):
        super().__init__(3)
        print("in tringlr init")

    def area_of_tringle(self):
        super().sides(10, 20, 30)
        super().display_side()
        self.s = self.side1 + self.side2 + self.side3
        print("area={}".format(self.s))


t = tringle()
t.area_of_tringle()






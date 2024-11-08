class Rect:
    def __init__(self, length, breath):
        self.length = length
        self.breath = breath
    def area(self):
        area = self.length * self.breath
        return area
    def perimeter(self):
        perimeter = 2 * (self.length + self.breath)
        return perimeter
    
rectangle1 = Rect(4,5)

rectangle2 = Rect(4,5)
print(rectangle1.area())
print(rectangle2.perimeter())
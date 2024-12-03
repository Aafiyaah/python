class Rectangle:
    def __init__(self, length, breadth):
       self.length = length
       self.breadth = breadth
    def area(self):
        return self.length * self.breadth
    def perimeter(self):
        return 2 * (self.length + self.breadth)
    def display(self):
        print(f"area of rectangle: {self.area() }")
        print(f"perimeter of rectangle: {self.perimeter() }")
    def compare_area(self, other):
        if self.area() == other.area():
            print("\nRectangles are equal in area")
        elif self.area() == other.area():
            print("\nRectangle 1 is area than rectangle 2")
        else:
            print("\nRectangle 2 is area than rectangle 1")
print("\nenter dimension of the first rectangle:")
length1 =int(input("enter length1: "))
breadth1 =int(input("enter breadth1: "))
rect1 = Rectangle(length1,breadth1)
rect1.display()
print("\nenter dimension of the second rectangle:")
length2 =int(input("enter length2: "))
breadth2 =int(input("enter breadth2: "))
rect2 = Rectangle(length2,breadth2)
rect2.display()

rect1.compare_area(rect2)
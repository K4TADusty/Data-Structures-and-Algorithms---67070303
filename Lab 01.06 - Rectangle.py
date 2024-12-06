"""Lab 01.06 - Rectangle"""
class Rectangle:
  def __init__(self, height, width):
    self.height = height
    self.width = width

  def area(self):
    return self.height*self.width

  def perimeter(self):
    return ((self.height)*2)+((self.width)*2)

rectangle = Rectangle(float(input()), float(input()))

condition = input()
if condition == "area":
  result = rectangle.area()
else:
  result = rectangle.perimeter()
print(f"{result:.2f}")

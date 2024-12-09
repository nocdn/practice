# creating a new type
# variables that belong to an object or class, are called fields or attributes
# functions that belong to a class, are called methods

class Rectangle:
    pass

r = Rectangle()
# r is an instance of type rectangle
r.x = 0
r.y = 0
r.w = 1
r.l = 2

def areaRectangle(rect):
    return rect.w * rect.l

print(f"Rectangle position is {r.x}, {r.y}")
print(f"Rectangle area is {areaRectangle(r)}")

def 

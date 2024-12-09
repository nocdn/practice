import math
import copy

# creating a new type
# variables that belong to an object or class, are called fields or attributes
# functions that belong to a class, are called methods

# class Rectangle:
#     pass

# r = Rectangle()
# r is an instance of type rectangle
r.x = 0
r.y = 0
r.w = 1
r.l = 2

def areaRectangle(rect):
    return rect.w * rect.l

# print(f"Rectangle position is {r.x}, {r.y}")
# print(f"Rectangle area is {areaRectangle(r)}")

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def distance(p1, p2):
    return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

p1 = Point(1, 2)
p2 = Point(4, 6)
# print(distance(p1, p2))

class Rectangle(object): 
    """represent a rectangle.
    attributes: width, height, corner (bottom left corner). """

box = Rectangle() 
box.width = 100.0 
box.height = 200.0 
box.corner = Point() 
box.corner.x = 0.0 
box.corner.y = 0.0 

def move_rectangle(rect, dx, dy):
    new_rect = copy.deepcopy(rect)
    new_rect.corner.x += dx
    new_rect.corner.y += dy
    return new_rect


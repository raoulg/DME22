"""Example code using the lesson."""

import math


class Coordinates:
    def __init__(self, x = None, y = None):
        self.x = x
        self.y = y
    
    def set_x_coordinate(self, x):
        self.x = x
        
    def set_y_coordinate(self, y):
        self.y = y
    
    def abs(self):
        return math.sqrt(self.x**2 + self.y**2)

    def __abs__(self):
        return self.abs()
    
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Coordinates(x, y)
        
    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Coordinates(x, y)
    
    def mirror_in_x(self):
        self.y = -self.y
        
    def mirror_in_y(self):
        self.x = -self.x
    
    def __str__(self):
        return f'({self.x:.3f}, {self.y:.3f})'

x = 3.14594534534

print(f'x: {x}')
        
c = Coordinates(x, 5)

d = Coordinates(10, 6)

f = c + d       # c.__add__(d)
g = c - d

pass

print(str(c))          # c.__str__()
pass

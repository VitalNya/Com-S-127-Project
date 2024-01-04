# Vital Nyabashi               4/23/2023
# Com S 127: Lab 16 circle.py
# Citation: https://www.geeksforgeeks.org/check-two-given-circles-touch-intersect/


import math


class Circle:
    def __init__(self, x, y, radius):
        self._x = x
        self._y = y
        self._radius = radius

    def get_x(self):
        return self._x

    def set_x(self, x):
        self._x = x

    def get_y(self):
        return self._y

    def set_y(self, y):
        self._y = y

    def get_radius(self):
        return self._radius

    def set_radius(self, radius):
        self._radius = radius

    def diameter(self):
        return 2 * self._radius

    def area(self):
        return math.pi * (self._radius ** 2)

    def circumference(self):
        return 2 * math.pi * self._radius

    def summary(self):
        print(f"Circle Summary: (x={self._x}, y={self._y}, radius={self._radius})")
        print(f"Diameter: {self.diameter()}")
        print(f"Area: {self.area()}")
        print(f"Circumference: {self.circumference()}")

    def __str__(self):
        return f"Circle: (x={self._x}, y={self._y}, radius={self._radius})"

    def is_intersecting(self, other):
        distance = math.sqrt(((self._x - other.get_x()) ** 2) + ((self._y - other.get_y()) ** 2))
        return distance < (self._radius + other.get_radius())

def main():
    c1 = Circle(0, 0, 5)
    c2 = Circle(10, 10, 7)

    print(c1)
    print(c2)

    print("Changing c1's radius to 10...")
    c1.set_radius(10)
    print(c1)

    print("Changing c2's x coordinate to 5...")
    c2.set_x(5)
    print(c2)

    print("Printing c1's summary...")
    c1.summary()

    print("Printing c2's summary...")
    c2.summary()

    print("Checking if c1 intersects with c2...")
    print(c1.is_intersecting(c2))


if __name__ == "__main__":
    main()

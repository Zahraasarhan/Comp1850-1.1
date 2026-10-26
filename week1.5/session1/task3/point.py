# Week 1.5, Session 1: Task 3
import math
class Point:
    """
    A Point in 2D space.
    """
    # Add constructor here
    def __init__(self, x, y):
    # Add distance() method here
        """
        Create a point with x and y coordinates.
        """
        self.x = x
        self.y = y
    def distance(self):
        """
         Return the distance from this Point to the origin.
     """
        return math.hypot(self.x, self.y)
    # Add distance_to() method here
    def distance_to(self, other_point):
       """
       Return the distance from this Point to another Point.
       """
       return math.hypot(self.x - other_point.x, self.y - other_point.y)
p1 = Point(3, 4)
p2 = Point(6, 8)
print(p1.x)
print(p1.y)
print(p1.distance())
print(p1.distance_to(p2))
    # (This will need a parameter representing another point)



# Finally, add code here to demonstrate use of Point

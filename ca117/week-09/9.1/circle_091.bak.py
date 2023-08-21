class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def midpoint(self, other):
        x = (self.x + other.x) / 2
        y = (self.y + other.y) / 2
        return Point(x, y)

    def __str__(self):
        return f"({self.x:.1f}, {self.y:.1f})"
    

class Circle:

    def __init__(self, centre=None, radius=1):
        if centre is None:
            centre = Point(0,0)
        self.centre = centre
        self.radius = radius


    def __str__(self):
        return f"Centre: ({self.centre.x:.1f}, {self.centre.y:.1f})\nRadius: {self.radius}"




# class Point:

#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y

#     def midpoint(self, other):
#         x = (self.x + other.x) / 2
#         y = (self.y + other.y) / 2
#         return Point(x, y)

#     def __str__(self):
#         return f"({self.x:.1f}, {self.y:.1f})"
    

# class Circle:

#     def __init__(self, centre=None, radius=1):
#         self.centre = centre
#         self.radius = radius
#         if self.centre == None:
#             self.centre = Point(0,0)

#     def __str__(self):
#         return f"Centre: ({self.centre.x:.1f}, {self.centre.y:.1f})\nRadius: {self.radius}"










class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def area(self):
        return self.__length * self.__width

    def __lt__(self, other):  # Corrected method name to __lt__ for '<' comparison
        return self.area() < other.area()

    def display(self):
        print("Length:", self.__length, "Width:", self.__width)  # Access private attributes

rect1 = Rectangle(3, 4)
rect2 = Rectangle(8, 6)
rect1.display()
rect2.display()

if rect1 < rect2:
    print(f"Rectangle1 has smaller area than Rectangle2")
else:
    print(f"Rectangle1 has a larger or equal area compared to Rectangle2")

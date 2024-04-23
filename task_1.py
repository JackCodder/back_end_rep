class Rectangle:
    def __init__(self, a=1, b=2):
        self.a = a
        self.b = b

    def print_square(self):
        print('Площадь =',self.a * self.b)

    def print_perimeter(self):
        print('Периметр =', 2 * (self.a + self.b))
              

rectangle = Rectangle()

rectangle.print_square()
rectangle.print_perimeter()
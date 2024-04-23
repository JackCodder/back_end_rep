class Rectangle:
    def __init__(self, a=1, b=2):
        self.a = a
        self.b = b

    def get_square(self):
        print('Площадь =',self.a * self.b)

    def get_perimeter(self):
        print('Периметр =', 2 * (self.a + self.b))
              

rectangle = Rectangle()

rectangle.get_square()
rectangle.get_perimeter()
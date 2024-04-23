class Calculator:
    def __init__(self, a=4, b=2):
        self.a = a
        self.b = b

    def get_addition(self):
        return f'Сложение чисел = {self.a + self.b}'
    
    def get_subtraction(self):
        return f'Вычитание чисел = {self.a - self.b}'
    
    def get_multiplication(self):
        return f'Умножение чисел = {self.a * self.b}'
    
    def get_division(self):
        if self.b == 0:
            return 'Делить на ноль нельзя'
        return f'Деление чисел = {self.a / self.b}'
    

calculator = Calculator(6, 3)

print(calculator.get_addition())
print(calculator.get_subtraction())
print(calculator.get_multiplication())
print(calculator.get_division())
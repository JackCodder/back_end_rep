class Person:
       def __init__(self, name, age):
           self.name = name
           self.age = age

       def __str__(self):
           return f"имя - {self.name}, возраст - {self.age} лет"

person = Person("Вася", 20)
print(person)

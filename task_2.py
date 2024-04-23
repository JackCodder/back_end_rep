class Human:
    def __init__(self, name, city, year_born):
        self.name = name
        self.city = city
        self.year_born = year_born

    def get_age(self):
        return f'вовзраст человека по имени {self.name} = {2024 - self.year_born}'
    

id_1 = Human('Вася', 'Москва', 2000)

print(id_1.get_age())
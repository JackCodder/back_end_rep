class Products:
    def __init__(self, name, price):
        super().__init__()
        # print('init Products')
        self.name = name
        self.price = price

    def print_info(self):
        print(f'{self.name}, цена = {self.price}$')
    

class MixinID:
    ID = 0

    def __init__(self):
        # print('init MixinID')
        MixinID.ID += 1
        self.id = MixinID.ID

    def print_mixin_id(self):
        print(f'идентификатор товара = {self.id}')


class Fruits(Products, MixinID):
    pass


apple = Fruits('Яблоко', 1)

apple.print_info()
apple.print_mixin_id()
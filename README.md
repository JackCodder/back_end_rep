QuerySet
In [1]: models.Birds.objects.all()
Out[1]: <QuerySet [<Birds: Гусь>, <Birds: Утка>, <Birds: Куропатка>, <Birds: Рябчик>, <Birds: Лебедь>]>

In [2]: models.Birds.objects.values()
Out[2]: <QuerySet [{'id': 1, 'name': 'Гусь', 'kind': 'anseriformes', 'information': 'Длинная шея', 'population': 5, 'is_rare': False}, {'id': 2, 'name': 'Утка', 'kind': 'anseriformes', 'information': 'Умеет плавать', 'population': 5, 'is_rare': False}, {'id': 3, 'name': 'Куропатка', 'kind': 'galliformes', 'information': '', 'population': 1, 'is_rare': True}, {'id': 4, 'name': 'Рябчик', 'kind': 'galliformes', 'information': '', 'population': 5, 'is_rare': False}, {'id': 
5, 'name': 'Лебедь', 'kind': 'anseriformes', 'information': 'Красивая птица', 'population': 3, 'is_rare': True}]>

In [3]: models.Animal.objects.all()
Out[3]: <QuerySet [<Animal: Зебра>, <Animal: Манула>, <Animal: Белый медведь>, <Animal: Геккон>, <Animal: Дельфин>]>

In [4]: list(models.Animal.objects.all())
Out[4]: 
[<Animal: Зебра>,        
 <Animal: Манула>,       
 <Animal: Белый медведь>,
 <Animal: Геккон>,       
 <Animal: Дельфин>]      

In [5]: models.Animal.objects.first()
Out[5]: <Animal: Зебра>

In [6]: models.Staff.objects.filter(salary__lt=70000)
Out[6]: <QuerySet [<Staff: Борисов Алексей>]>

In [7]: models.Animal.objects.last()
Out[7]: <Animal: Дельфин>

In [8]: models.Animal.objects.count()
Out[8]: 5

In [9]: models.Animal.objects.order_by('name')
Out[9]: <QuerySet [<Animal: Белый медведь>, <Animal: Геккон>, <Animal: Дельфин>, <Animal: Зебра>, <Animal: Манула>]>

In [10]: models.Animal.objects.order_by('-name')
Out[10]: <QuerySet [<Animal: Манула>, <Animal: Зебра>, <Animal: Дельфин>, <Animal: Геккон>, <Animal: Белый медведь>]>

In [11]: models.Animal.objects.filter(name__contains='б')
Out[11]: <QuerySet [<Animal: Зебра>]>

In [12]: models.Animal.objects.filter(name__icontains='б')
Out[12]: <QuerySet [<Animal: Зебра>]>

In [13]: models.Animal.objects.count()
Out[13]: 5

In [14]: models.Animal.objects.filter(name__exact='Дельфин')
Out[14]: <QuerySet [<Animal: Дельфин>]>

In [15]: models.Animal.objects.filter(name__exact='Дельфн')
Out[15]: <QuerySet []>

In [16]: models.Animal.objects.create(name='Барсук', population=3)
Out[16]: <Animal: Барсук>

In [17]: models.Animal.objects.filter(id__gt=5).update(is_rare=True)
Out[17]: 1

In [18]: models.Animal.objects.values('name', 'type')
Out[18]: <QuerySet [{'name': 'Зебра', 'type': 'mamal'}, {'name': 'Манула', 'type': 'mamal'}, {'name': 'Белый медведь', 'type': 'mamal'}, {'name': 'Геккон', 'type': 'reptile'}, {'name': 'Дельфин', 'type': 'fish'}, {'name': 'Барсук', 'type': 'mammal'}]>

In [19]: models.Animal.objects.values_list('name', 'type')
Out[19]: <QuerySet [('Зебра', 'mamal'), ('Манула', 'mamal'), ('Белый медведь', 'mamal'), ('Геккон', 'reptile'), ('Дельфин', 'fish'), ('Барсук', 'mammal')]>

In [20]: models.Staff.objects.filter(id=3).exists()
Out[20]: False

In [21]: models.Staff.objects.dates('date_of_birth', 'day')
Out[21]: <QuerySet [datetime.date(1999, 5, 7), datetime.date(2000, 5, 7)]>

In [22]: models.Staff.objects.filter(salary__gt=70000)
Out[22]: <QuerySet [<Staff: Петров Иван>]>

In [23]: models.Staff.objects.filter(salary__lt=70000)
Out[23]: <QuerySet [<Staff: Борисов Алексей>]>

In [24]: models.Staff.objects.latest('date_of_birth')
Out[24]: <Staff: Петров Иван>

In [25]: models.Staff.objects.get(id=1)
Out[25]: <Staff: Петров Иван>
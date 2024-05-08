from django.db import models


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование')
    content = models.TextField(blank=True, verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата публикации')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', blank=True, null=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    # category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['created_at']


# class Category(models.Model):
#     title = models.CharField(max_length=150, db_index=True, verbose_name='Наименование категории')

#     def __str__(self):
#         return self.title

#     class Meta:
#         verbose_name = 'Новость'
#         verbose_name_plural = 'Новости'
#         ordering = ['created_at']


# class Animal(models.Model):

#     TYPE_CHOICES = (
#         ('mamal', 'Млекопитающее'),
#         ('fish', 'Рыба'),
#         ('reptile', 'Рептилия'),
#     )

#     name = models.CharField('Название', max_length=100)
#     type = models.CharField('Род', max_length=100, choices=TYPE_CHOICES, default='mammal')
#     information = models.TextField('Информация', blank=True)
#     population = models.PositiveIntegerField('Популяция', default=0)
#     is_rare = models.BooleanField('Вымирающее животное', default=False)

#     class Meta:
#         verbose_name = 'Животное'
#         verbose_name_plural = 'Животные'

#     def __str__(self) -> str:
#         return self.name
    

# class Birds(models.Model):

#     TYPE_CHOICES = (
#         ('anseriformes', 'Гусеобразные'),
#         ('galliformes', 'Курообразные'),
#     )

#     name = models.CharField('Название', max_length=100)
#     kind = models.CharField('Вид', max_length=100, choices=TYPE_CHOICES, default='galliformes')
#     information = models.TextField('Информация', blank=True)
#     population = models.PositiveIntegerField('Популяция', default=0)
#     is_rare = models.BooleanField('Вымирающая птица', default=False)

#     class Meta:
#         verbose_name = 'Птица'
#         verbose_name_plural = 'Птицы'

#     def __str__(self) -> str:
#         return self.name    


# class Staff(models.Model):
#     firat_name = models.CharField('Имя', max_length=30)
#     last_name = models.CharField('Фамилия', max_length=40)
#     patronymic = models.CharField('Отчество', max_length=30, blank=True)

#     date_of_birth = models.DateField('Дата рождения')
#     picture = models.ImageField('Фото сотрудника', upload_to='pictures', null=True, blank=True)
#     salary = models.DecimalField('Заработная плата', max_digits=8, decimal_places=2, editable=True)

#     class Meta:
#         verbose_name = 'Сотрудник'
#         verbose_name_plural = 'Сотрудники'

#     def __str__(self) -> str:
#         return f'{self.last_name} {self.firat_name}'
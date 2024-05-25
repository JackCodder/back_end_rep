from django.test import TestCase
from django.test import Client
from core import models


class Tests(TestCase):
    def setUp(self):
        self.client = Client()
        self.animal = models.Animal.objects.create(
            name='Кабан',
            type='mammal',
            population=15,
            is_rare=True
        )
        
    def test_index(self):
        response = self.client.get('/index/')
        self.assertEqual(response.status_code, 200)

    def test_detail_animal(self):
        response = self.client.get(f'/animal/{self.animal.id}/')
        self.assertEqual(response.status_code, 200)

    def test_redirect(self):
        response = self.client.get('/redirect/')
        self.assertEqual(response.status_code, 302)

    def test_create_animal(self):
        data = {
            "name": "Пес",
            "type": "mamal",
            "population": 10,
        }
        response = self.client.post('/animals/', data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['name'], 'Пес')


    def test_list_animals(self):
        response = self.client.get('/animals/')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.data, list)

    def test_retrieve_animal(self):
        animal = models.Animal.objects.create(name='Cat', type='Feline')
        response = self.client.get('/animals/{}/'.format(animal.id))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], 'Cat')
        self.assertEqual(response.data['type'], 'Feline')

    def test_update_animal(self):
        animal = models.Animal.objects.create(name='Cat', type='Feline')
        data = {
            "name": "Заяц",
            "type": "mamal",
            "population": 10,
        }
        response = self.client.put('/animals/{}/'.format(animal.id), data, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], 'Заяц')


    def test_delete_animal(self):
        animal = models.Animal.objects.create(name='Cat', type='Feline')
        response = self.client.delete('/animals/{}/'.format(animal.id))
        self.assertEqual(response.status_code, 204)
        with self.assertRaises(models.Animal.DoesNotExist):
            models.Animal.objects.get(id=animal.id)


class NewsModelTest(TestCase):
    def test_create_news(self):
        news = models.News.objects.create(
            title="Новость",
            content="Эта новость для теста",
            category=None,
        )
        self.assertEqual(news.title, "Новость")
        self.assertEqual(news.content, "Эта новость для теста")
        self.assertIsNone(news.category)

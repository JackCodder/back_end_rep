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

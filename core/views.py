from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

from core import models


def index(request):
    news = models.News.objects.all()
    return render(request, 'core/index.html', context={'news': news, 'title': 'Список новостей'})

def time(request):
    return HttpResponse(f'<h1>Текущая дата и время</h1><p>{datetime.now()}</p>')

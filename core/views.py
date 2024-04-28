from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


def index(request):
    return HttpResponse('Hello!')

def time(request):
    return HttpResponse(f'<h1>Текущая дата и время</h1><p>{datetime.now()}</p>')

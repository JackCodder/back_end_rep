from typing import Any
from django.shortcuts import render
from django.http import HttpResponse
from core import models, forms, filters, serializers
from django.views.generic import ListView, TemplateView, DetailView, RedirectView, FormView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet


class ClassBasedIndex(TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        news = models.News.objects.all()
        categories = models.Category.objects.all()
        context = {
            'news': news,
            'title': 'Список новостей',
            'categories': categories,
        }
        return context


class ClassCategory(TemplateView):
    template_name = 'core/category.html'

    def get_context_data(self, category_id, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        news = models.News.objects.filter(category=category_id)
        categories = models.Category.objects.all()
        category = models.Category.objects.get(pk=category_id)
        context = {
            'news': news,
            'categories': categories,
            'category': category,
        }
        return context


class AnimalList(ListView):
    model = models.Animal
    context_object_name = 'animals'
    template_name = 'core/animal_list.html'

    def get_filters(self):
        return filters.Animal(self.request.GET)
    
    def get_queryset(self):
        return self.get_filters().qs
    
    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['filters'] = self.get_filters()
        return context


class AnimalDetail(DetailView):
    model = models.Animal
    context_object_name = 'animal'
    template_name = 'core/animal_detail.html'

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['additioonal_info'] = 'Режим работы: Каждый день 10:00 - 21:00'
        return context


class Redirect(RedirectView):
    query_string = True
    url = 'http://paranoia.com/'


class SimpleForm(FormView):
    template_name = 'core/form.html'
    form_class = forms.SimpleForm
    success_url = '/index/'

    def form_valid(self, form) -> HttpResponse:
        print(form.cleaned_data)
        return super().form_valid(form)
    

class AnimalList(APIView):
    def get(self, request):
        qs = models.Animal.objects.all()
        serializer = serializers.Animal(qs, many=True)

        return Response(data=serializer.data)
    
    def post(self, request):
        serializer = serializers.Animal(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'message': 'OK'})
    

class AnimalList(ModelViewSet):
    queryset = models.Animal.objects.all()
    filterset_class = filters.Animal
    serializer_class = serializers.Animal


        
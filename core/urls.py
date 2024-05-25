from django.urls import path
from core import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('animals', views.AnimalList, basename='animals')

urlpatterns = [
    path('index/', views.ClassBasedIndex.as_view(), name='home'),
    path('category/<int:category_id>', views.ClassCategory.as_view(), name='category'),
    # path('animals/', views.AnimalList.as_view(), name='animals'),
    path('animal/<int:pk>/', views.AnimalDetail.as_view(), name='animal_detail'),
    path('redirect/', views.Redirect.as_view(), name='redirect'),
    path('form_example/', views.SimpleForm.as_view(), name='form_example'),
]

urlpatterns += router.urls
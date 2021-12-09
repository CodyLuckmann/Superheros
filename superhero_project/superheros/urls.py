from django.urls import path

from . import views

app_name = 'superheros'
urlpatterns = [
    path('index/', views.index, name = 'index')
]
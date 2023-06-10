from django.urls import path
from . import views

app_name = 'converter'

urlpatterns = [
    path('', views.index, name='index')
]

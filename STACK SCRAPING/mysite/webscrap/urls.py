from django.urls import include, path
from . import views

#URL patterns
urlpatterns = [
    path('webscrap/', views.index, name='index'),
    path('contact/', views.contact, name='contact')
]
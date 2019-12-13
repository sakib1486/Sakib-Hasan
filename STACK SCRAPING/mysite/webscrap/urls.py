from django.urls import include, path
from . import views

#URL patterns
urlpatterns = [
    path('webscrap/', views.index, name='index'),
    path('newest/', views.newest, name='newest'),
    path('voted/', views.voted, name='voted'),
    path('latest/', views.latest, name='latest')
]
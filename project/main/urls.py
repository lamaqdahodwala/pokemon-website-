from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('id', views.byId, name='byid'),
    path('name', views.byName, name='byname'),
    path('pokemon/<int:id>', views.pokemon, name='pokemon'),
    path('findpokemon', views.findpokemon, name='findit')
]
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('id', views.byId, name='byid')
]
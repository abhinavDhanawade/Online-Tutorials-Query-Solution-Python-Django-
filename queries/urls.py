from django.urls import path
from . import views
urlpatterns = [
    path('', views.queries, name='queries'),
    path('search', views.search, name='search'),
    path('filter/<str:catego>', views.filter, name='filter'),
    path('<str:title>', views.solution, name='solution'),    
]

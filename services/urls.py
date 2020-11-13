from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('tutorials/', views.alltutorials, name='alltutorials'),
    path('tutorials/<str:title>/', views.tutorial_details, name='tutorial_details'),
    path('tutorials/addtutorial', views.addtutorial, name='addtutorial'),
    path('mycourse', views.mycourse, name='mycourse'),
    path('mycourse/<str:title>/', views.tutorial, name='tutorial'),
    path('delete/<str:title>', views.delete_querie, name='delete_querie'),
    path('profile', views.profilee, name='profilee'),
    path('contact', views.contact, name='contact'),
    path('filter/<str:catego>', views.tfilter, name='tfilter'),
]

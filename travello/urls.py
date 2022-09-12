from django.urls import path

from travello import views

urlpatterns = [
    path('', views.index, name='home'),
    # path('home', views.home, name='homepage')
]
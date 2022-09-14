from django.urls import path
from . import views

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('terms', views.terms, name='terms'),
    path('signout', views.signout, name='sign-out')
]

from django.urls import path
from core import views

urlpatterns = [
    path('', views.IndexPage.as_view(), name='index_page'),
    path('sign_up', views.SignUp.as_view(), name='sign_up'),
    path('exit', views.Exit.as_view(), name='exit'),
    path('login', views.Login.as_view(), name='login'),

]

from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    path('search/', views.search, name='search'),
    path('settings/', views.settings, name='settings'),
    path('upload', views.upload, name='upload'),
    path('like-post', views.like_post, name='like-post'),
    path('signup/', views.signup_user, name='signup_user'),
    path('login/', views.signin_user, name='signin_user'),
    path('logout/', views.logout_user, name='logout_user'),
]
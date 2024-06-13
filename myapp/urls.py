from django.urls import path
from myapp.views import * 
from myapp.views import login_view
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', index, name='index'),
    path('login/', login_view, name='login'),
    path('register/', register, name='register'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('profile/edit/', profile_view, name='profile_edit'),
    path('profile/', profile_page, name='profile'),




]
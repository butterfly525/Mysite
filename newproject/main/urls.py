
from django.urls import path
from . import views
from .views import LoginView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.index, name='home'),
    path('save_data/<int:id>/', views.save_data, name='save_data'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),

]

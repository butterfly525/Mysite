
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('save_data/<int:id>/', views.save_data, name='save_data'),
 

]

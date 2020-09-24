from django.urls import path
from . import views 


app_name = 'taifa'
urlpatterns = [
    path('', views.home, name = 'home'),
    path('account/', views.account, name = 'account')
]
from django.urls import path
from myapp.views import *

urlpatterns = [
    path('', index, name='indexpage'),
    path('forget/', forgetpassword, name='forget'),
    path('home/', home, name='home'),
]
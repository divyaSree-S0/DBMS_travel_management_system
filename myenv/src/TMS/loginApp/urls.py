from django.urls import path
from loginApp.views import loginView

urlpatterns = [
    path('',loginView, name='login'),
]
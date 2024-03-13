from django.urls import path
from homeApp.views import aboutView, contactView,homeView

urlpatterns = [
    path('about/',aboutView, name='about'),
    path('contact/', contactView, name='contact'),
    path('', homeView, name='home'),
]
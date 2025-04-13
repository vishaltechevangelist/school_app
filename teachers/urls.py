from django.urls import path
from teachers import views

urlpatterns = [
    path('home/', views.home)
]

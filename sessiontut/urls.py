from django.urls import path
from sessiontut import views

urlpatterns = [
    path('set/', views.home),
    path('get/', views.get),
    path('delete/', views.delete),
    path('update/', views.update)
]

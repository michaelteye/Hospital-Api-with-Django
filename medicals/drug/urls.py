from django.urls import path
from .views import DetailView, Personal

urlpatterns = [
    path('user/', Personal.as_view()),
    path('user/<int:pk>/',DetailView.as_view()),
]



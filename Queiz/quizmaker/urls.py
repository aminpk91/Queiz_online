from django.urls import path

from .views import list_Qs,create_Q,create_quiz

urlpatterns = [
    path('Qs/', list_Qs),
    path('createq/', create_Q),
    path('Queiz/<str:name>', create_quiz),
    ]
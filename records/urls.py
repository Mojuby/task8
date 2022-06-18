from django.urls import path
from . import views

urlpatterns = [
    path('book-a-room/', views.book_a_room, name = 'book-a-room'),
    path('reservations/', views.reservations, name = 'reservations'),
]
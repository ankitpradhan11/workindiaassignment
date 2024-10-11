from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_user),
    path('add_train/', views.add_train),
    path('check_availability/', views.check_seat_availability),
    path('book_seat/', views.book_seat),
]

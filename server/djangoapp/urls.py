from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_user),
    path('get_cars/', views.get_cars),
    path('dealerships/', views.get_dealerships),
    path('dealer/<int:dealer_id>/', views.get_dealer),
    path('reviews/', views.get_dealer_reviews),
    path('add_review/', views.add_review),
]
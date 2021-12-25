from django.urls import path,include
from .views import CarGet,car_post,rate_post
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('cars', CarGet, basename='cars')



urlpatterns = [
    path('POST/cars/', car_post),
    path('POST/rate/', rate_post),
    path('GET/',include(router.urls)),
]

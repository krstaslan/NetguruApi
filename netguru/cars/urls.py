from django.urls import path, include
from .views import CarGet, car_post, rate_post, Delete, rates  # , Delete, car_delete, save_rate
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('cars', CarGet, basename='cars')

urlpatterns = [
    path('POST/cars/', car_post),
    path('POST/rate/', rate_post),
    path('GET/rate/', rates),
    path('GET/', include(router.urls)),
    path('DELETE/cars/<int:pid>', Delete,name='car_delete'),
    #path('DELETE/', Delete.as_view()),
    # path('POST/<int:pid>',save_rate, name='save-rate'),
]

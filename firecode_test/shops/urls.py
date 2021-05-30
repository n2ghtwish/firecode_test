from django.urls import path
from .views import CityView, StreetView, ShopView, ErrorView


app_name = 'cities'
urlpatterns = [
    path('city/', CityView.as_view()),
    path('city/street/', StreetView.as_view()),
    path('shop/', ShopView.as_view()),
    path('', ErrorView.as_view()),
    path('<slug:slug>/', ErrorView.as_view()),
]

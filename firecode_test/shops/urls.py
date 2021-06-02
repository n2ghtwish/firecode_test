from django.urls import path
from .views import CityView, StreetView, ShopView, ErrorView, PeeWeeCityView, PeeWeeStreetView, PeeWeeShopView


app_name = 'cities'
urlpatterns = [
    path('city/', CityView.as_view()),
    path('peeweecity/', PeeWeeCityView.as_view()),
    path('city/street/', StreetView.as_view()),
    path('peeweecity/peeweestreet/', PeeWeeStreetView.as_view()),
    path('shop/', ShopView.as_view()),
    path('peeweeshop/', PeeWeeShopView.as_view()),
    path('<slug:slug>/', ErrorView.as_view()),
    path('', ErrorView.as_view()),
]

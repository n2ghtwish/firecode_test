from django.urls import path
from .views import ErrorView, PeeWeeCityView, PeeWeeStreetView, PeeWeeShopView


app_name = 'cities'
urlpatterns = [
    path('city/', PeeWeeCityView.as_view()),
    path('city/street/', PeeWeeStreetView.as_view()),
    path('shop/', PeeWeeShopView.as_view()),
    path('<slug:slug>/', ErrorView.as_view()),
    path('', ErrorView.as_view()),
]

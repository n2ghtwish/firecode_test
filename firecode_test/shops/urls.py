from django.urls import path
from .views import CityView


app_name = 'cities'
urlpatterns = [
    path('city/', CityView.as_view()),
]

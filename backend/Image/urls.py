from django.urls import path
from .views import ImageAPI
urlpatterns = [
    path('', ImageAPI.as_view()), #POST
    path('<str:uuid_name>', ImageAPI.as_view()), #GET
]
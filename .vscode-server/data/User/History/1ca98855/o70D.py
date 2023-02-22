from django.urls import path
from .views import ImageAPIView
urlpatterns = [
    path('', ImageAPIView.as_view()), #POST
    path('<int:name>/', ImageAPIView.as_view()), #GET
]
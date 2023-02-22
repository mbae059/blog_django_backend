from django.urls import path
from .views import ImageAPIView
urlpatterns = [
    path('', ImageAPIView.as_view()), #POST
    path('<int:id>/', ImageAPIView.as_view()), #GET
]
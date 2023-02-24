from django.urls import path
from .views import FeedAPI, LikeAPI
urlpatterns = [
    path("content/<str:nickname>/<int:id>", FeedAPI.as_view()),
    path("", FeedAPI.as_view()),
    path("like/<int:id>", LikeAPI.as_view())
]

from django.urls import path
from .views import FeedAPI
urlpatterns = [
    path("<str:nickname>/<int:id>", FeedAPI.as_view()),
    path("", FeedAPI.as_view()),

]

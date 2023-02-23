from django.urls import path 
from .views import RegisterAPI, LoginAPI, LogoutAPI, IntroductionAPI
urlpatterns = [
    path("register", RegisterAPI.as_view()),
    path("login", LoginAPI.as_view()),
    path('logout', LogoutAPI.as_view()),
    path('introduction', IntroductionAPI.as_view())
]

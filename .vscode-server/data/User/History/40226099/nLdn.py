from django.urls import path 

urlpatterns = [
    path("user/", include('User.urls')),
]

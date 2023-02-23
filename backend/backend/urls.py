from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("user/", include('User.urls')),
    path('image/', include('Image.urls')),
    path('feed/', include('Feed.urls')),
]

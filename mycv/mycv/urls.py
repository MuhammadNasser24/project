from django.contrib import admin
from django.urls import path, include  # Import include function to include app URLs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myweb.urls')),  # Include URLs from the myweb app
]

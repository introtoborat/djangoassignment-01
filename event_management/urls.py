from django.contrib import admin
from django.urls import path, include
from core.views import no_permission, home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('activities/', include('activities.urls')),
    path('user/', include('user.urls')),
    path('no-permission/', no_permission, name='no-permission'),
    path('', home, name="home"),
]
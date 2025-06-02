from django.contrib import admin
from django.urls import path
from .api import hello_world_api_view


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/hello/", hello_world_api_view),
]

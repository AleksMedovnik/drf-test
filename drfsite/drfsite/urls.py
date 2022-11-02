from django.contrib import admin
from django.urls import path
from service.views import PostAPIView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/postlist/', PostAPIView.as_view()),
    path('api/v1/postlist/<int:pk>/', PostAPIView.as_view()),
]
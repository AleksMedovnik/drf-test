from django.contrib import admin
from django.urls import path
from service.views import PostAPIList, PostAPIUpdate, PostAPIDestroy

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/postlist/', PostAPIList.as_view()),
    path('api/v1/postlist/<int:pk>/', PostAPIUpdate.as_view()),
    path('api/v1/postdestroy/<int:pk>/', PostAPIDestroy.as_view()),
]

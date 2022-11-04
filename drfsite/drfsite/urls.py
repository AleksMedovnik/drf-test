from django.contrib import admin
from django.urls import path, include
from service.views import *
from rest_framework import routers

router_cat = routers.SimpleRouter()
router_cat.register(r'cats', CatViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/postlist/', PostAPIList.as_view()),
    path('api/v1/postlist/<int:pk>/', PostAPIUpdate.as_view()),
    path('api/v1/postdestroy/<int:pk>/', PostAPIDestroy.as_view()),
    path('api/v1/', include(router_cat.urls)),
]

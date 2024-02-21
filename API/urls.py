from django.urls import path,include
from . import views
from .views import UserViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users',UserViewSet)

urlpatterns = [
    path('', views.index, name="index"),
    # path('<name>/', views.name, name="name"),
    path('',include(router.urls))
]

# or we can use this way
# urlpatterns += router.urls


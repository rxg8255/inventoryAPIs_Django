from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'inventory', views.StockView, basename='inventory')


urlpatterns = router.urls

# urlpatterns = [
#     path('', include(router.urls))
# ]
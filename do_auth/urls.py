from django.urls import path
from .views import FirmViewSet,LoginView

from rest_framework.routers import DefaultRouter

app_name = 'jz'
urlpatterns = [
    path('login', LoginView.as_view(), name='login'),
]
router = DefaultRouter()
router.register(r'firm', FirmViewSet, basename='firm')
urlpatterns = urlpatterns+router.urls


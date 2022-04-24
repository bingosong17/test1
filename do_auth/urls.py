from django.urls import path
from .views import FirmViewSet, LoginView, UploadView

from rest_framework.routers import DefaultRouter

app_name = 'jz'
urlpatterns = [
    path('login', LoginView.as_view(), name='login'),
    path('upload', UploadView.as_view(), name='upload'),
]
router = DefaultRouter()
router.register(r'firm', FirmViewSet, basename='firm')
urlpatterns = urlpatterns + router.urls

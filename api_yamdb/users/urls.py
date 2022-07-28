from django.urls import include, path
from rest_framework.routers import DefaultRouter
from users.views import AuthTokenViewSet, ConfirmationViewSet, UserViewSet

router = DefaultRouter()
router.register(r'auth/signup', ConfirmationViewSet, basename='confirmation')
router.register(r'auth/token', AuthTokenViewSet, basename='auth_token')
router.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls)),
]

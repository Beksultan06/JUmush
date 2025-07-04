from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


router = DefaultRouter()
router.register(r'regions', RegionViewSet)
router.register(r'subregions', SubRegionViewSet)
router.register(r'professions', ProfessionViewSet)

urlpatterns = [
    path('auth/register/', RegisterView.as_view()),
    path('auth/verify-email/', VerifyEmailView.as_view()),
    path('user/role/', SetRoleView.as_view()),
    path('roles/', RoleViewSet.as_view({'get': 'list'}), name='roles-list'),
    path('user/profession/', SetProfessionView.as_view()),
    path('user/verify/', UploadDocumentsView.as_view()),
    path('api/auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('verify-passport/', PassportPhotoUploadView.as_view(), name='verify-passport'),
    path('', include(router.urls)),
]
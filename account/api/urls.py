from django.urls import path
from account.api.views import registration_view, LoginAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

app_name = "account"


urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/veruify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/login/', LoginAPIView.as_view(), name='login_api'),
    path('api/register/', registration_view , name = 'register_api')
] 
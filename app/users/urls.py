from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from users.views import CreateUserView,getUserView,DeleteUserView,UpdateUserView
app_name = 'user'

urlpatterns = [
    path('get/',getUserView.as_view(),name='get'),
    path('create/',CreateUserView.as_view(),name='create'),
    path('update/',UpdateUserView.as_view(),name='update'),
    path('delete/',DeleteUserView.as_view(),name='delete'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
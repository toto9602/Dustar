from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from account import views
urlpatterns = [
    # path('token/obtain/', views.TokenObtainView.as_view(), name='token_create'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
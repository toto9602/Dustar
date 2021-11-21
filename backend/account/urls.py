from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from account import views
urlpatterns = [
    # path('token/obtain/', views.TokenObtainView.as_view(), name='token_create'),
    path('signup/', views.SignUpView.as_view(), name='signup'),

    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('login/', views.LoginView.as_view(), name="token_obtain"),

]
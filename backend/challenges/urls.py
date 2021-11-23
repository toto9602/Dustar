from django.urls import path
from challenges import views

urlpatterns = [
    path('', views.ChallengeList.as_view(), name='main'),
    path('<int:challenge_pk>', views.ChallengeDetail.as_view(), name='challenge_detail'),
]
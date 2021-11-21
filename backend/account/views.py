from rest_framework import permissions, status, serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserCreateSerializer, UserLoginSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .models import User
from rest_framework import exceptions
from django.db import IntegrityError
from django.shortcuts import get_object_or_404

# https://eunjin3786.tistory.com/268
class SignUpView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = UserCreateSerializer
    def post(self, request):

        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        # try:
        #     user = User.objects.create_user(username=request.data['id'], password=request.data['password'])
        # except IntegrityError as e:
        #     raise exceptions.NotAcceptable("이미 존재하는 아이디 입니다.")

        # profile = Profile(
        #     user=user,
        #     nickname=request.data['nickname'],
        #     dust_type=request.data['dust_type'],
        # )
        # user.save()
        # profile.save()

        # serializer = ProfileSerializer(profile)
        # return Response(serializer.data, status=status.HTTP_201_CREATED)


class LoginView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = UserLoginSerializer

    def get_tokens_for_user(self, user):
        refresh = RefreshToken.for_user(user)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

    def post(self, request):
        print(request.data)
        user = authenticate(username=request.data['username'], password=request.data['password'])
        if user is not None:
            token = self.get_tokens_for_user(user)
            serializer = UserLoginSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)




# class SignUpView(APIView):

#     permission_classes = [permissions.AllowAny]
#     serializer_class = UserCreateSerializer
#     def post(self, request, format=None):

#         serializer = UserCreateSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class LogInView(APIView):
#     permission_classes = [permissions.AllowAny]
#     serializer_class = UserLoginSerializer

#     def get_tokens_for_user(self, user):
#         refresh = RefreshToken.for_user(user)

#         return {
#             'refresh': str(refresh),
#             'access': str(refresh.access_token),
#         }

#     def post(self, request):

#         user = authenticate(username=request.data['id'], password=request.data['password'])
#         if user is not None:
#             token = self.get_tokens_for_user(user)
#             serializer = serializers.

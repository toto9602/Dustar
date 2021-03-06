from rest_framework import serializers
# from rest_framework_jwt.settings import api_settings
from .models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import BaseUserManager

class UserCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'nickname', 'dust_type')

    extra_kwargs = {
        'password': {"write_only" : True}
    }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        validated_data['email'] = BaseUserManager.normalize_email(validated_data['email'])
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)

        instance.save()
        return instance




class UserLoginSerializer(serializers.ModelSerializer):
    
    token = serializers.SerializerMethodField(method_name='get_tokens_for_user')
    dust_type = serializers.SerializerMethodField()
    nickname = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('email', 'password', 'nickname', 'token', 'dust_type')


    def get_tokens_for_user(self, user):
        refresh = RefreshToken.for_user(user)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

    def get_nickname(self, obj):
        return obj.nickname

    def get_dust_type(self, obj):
        return obj.dust_type
    



# class ProfileSerializer(serializers.ModelSerializer):

#     token = serializers.SerializerMethodField(method_name='get_tokens_for_user')
#     user_id = serializers.SerializerMethodField()

#     class Meta:
#         model = Profile
#         fields = ('token', 'user_id', 'nickname', 'dust_type', 'email')

#     def get_tokens_for_user(self, user):
#         refresh = RefreshToken.for_user(user)

#         return {
#             'refresh': str(refresh),
#             'access': str(refresh.access_token),
#         }

#     def get_user_id(self, obj):
#         return obj.user.id



# class UserCreateSerializer(serializers.ModelSerializer):
#     token = serializers.SerializerMethodField(method_name='get_tokens_for_user')
#     extra_kwargs = {
#         'password': {"write_only" : True}
#     }
#     class Meta:
#         model = User
#         fields = ('token', 'username', 'email', 'id', 'password', 'dust_type', 'nickname')

#     def get_tokens_for_user(self, user):
#         refresh = RefreshToken.for_user(user)

#         return {
#             'refresh': str(refresh),
#             'access': str(refresh.access_token),
#         }

#     def create(self, validated_data):
#         password = validated_data.pop('password', None)
#         instance = self.Meta.model(**validated_data)
#         if password is not None:
#             instance.set_password(password)
#         instance.save()
#         return instance
    

# class UserLoginSerializer()
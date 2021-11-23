from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                        PermissionsMixin
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models.fields import BooleanField
from django.db.models.fields.related import OneToOneField
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserManager(BaseUserManager): 
# 유저 생성 helper function 제공. user 생성할 때의 행위를 지정
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('email 필수 입력!')
        user = self.model(email=self.normalize_email(email), **extra_fields) 
        #self.model => UserManager가 속해 있는 모델에 접근
        #normalize_email로 도메인 부분 lowercase => 중복 방지!
        user.set_password(password)
        # 암호화 위해서 set_password 사용함
        user.save(using=self.db)
        # 데이터베이스 여러 개 둘 때 사용. 굳이 안 써도 된다. 

        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self.db)

        return user


class User(AbstractBaseUser, PermissionsMixin):

    AMBITIOUS_DUST = 'AD'
    POPPING_DUST = 'PD'
    TINY_DUST = 'TD'
    EXCITING_DUST = 'ED'

    DUST_CHOICES = [
        (AMBITIOUS_DUST, '야망있는 먼지'),
        (POPPING_DUST, '통통튀는 먼지'),
        (TINY_DUST, '조구만 먼지'),
        (EXCITING_DUST, '신나는 먼지'),
    ]
    email = models.EmailField(unique=True)
    # 한 이메일로 계정 한 개만 생성 가능하게?
    nickname = models.CharField(max_length=20, blank=True, null=True)
    dust_type = models.CharField(max_length=10, choices=DUST_CHOICES, blank=True, null=True)
    big_star = models.PositiveIntegerField(default=0, blank=True, null=True)
    small_star = models.PositiveIntegerField(default=0, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(max_length=30, auto_now_add=True)

    objects = UserManager()
    # 헬퍼 클래스 지정하기
    USERNAME_FIELD = 'email' #email을 username field로 사용
    REQUIRED_FIELDS = [] #required_fields를 비워서 username을 required_fields에서 제외
    #django는 기본적으로 username을 사용. 이메일을 username으로 사용하기!
    class Meta:
        db_table: 'User'

    def __str__(self):
        if self.nickname is None: #생성된 superuser는 nickname을 갖지 않아, admin에서 에러 방지하는 임시 코드
            return '슈퍼유저먼지'
        return self.nickname


# class User(AbstractUser):

#     AMBITIOUS_DUST = 'AD'
#     POPPING_DUST = 'PD'
#     TINY_DUST = 'TD'
#     EXCITING_DUST = 'ED'

#     DUST_CHOICES = [
#         (AMBITIOUS_DUST, '야망있는 먼지'),
#         (POPPING_DUST, '통통튀는 먼지'),
#         (TINY_DUST, '조구만 먼지'),
#         (EXCITING_DUST, '신나는 먼지'),
#     ]
#     username = None
#     email = models.EmailField(unique=True)
#     nickname = models.CharField(max_length=20, blank=True, null=True)
#     dust_type = models.CharField(max_length=10, choices=DUST_CHOICES, blank=True, null=True)
#     big_star = models.PositiveIntegerField(default=0, blank=True, null=True)
#     small_star = models.PositiveIntegerField(default=0, blank=True, null=True)

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []

#     class Meta:
#         db_table: 'User'

#     def __str__(self):
#         if self.nickname is None:
#             return '슈퍼유저'
#         return self.nickname


# class UserManager(BaseUserManager): 
# # 유저 생성 helper function 제공. user 생성할 때의 행위를 지정
#     def create_user(self, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError('email 필수 입력!')
#         user = self.model(email=self.normalize_email(email), **extra_fields) 
#         #self.model => UserManager가 속해 있는 모델에 접근
#         #normalize_email로 도메인 부분 lowercase => 중복 방지!
#         user.set_password(password)
#         # 암호화 위해서 set_password 사용함
#         user.save(using=self.db)
#         # 데이터베이스 여러 개 둘 때 사용. 굳이 안 써도 된다. 

#         return user

#     def create_superuser(self, email, password):
#         user = self.create_user(email, password)
#         user.is_staff = True
#         user.is_superuser = True
#         user.save(using=self.db)

#         return user


# class User(AbstractBaseUser, PermissionsMixin):
#     id = models.BigAutoField(primary_key=True)

#     AMBITIOUS_DUST = 'AD'
#     POPPING_DUST = 'PD'
#     TINY_DUST = 'TD'
#     EXCITING_DUST = 'ED'

#     DUST_CHOICES = [
#         (AMBITIOUS_DUST, '야망있는 먼지'),
#         (POPPING_DUST, '통통튀는 먼지'),
#         (TINY_DUST, '조구만 먼지'),
#         (EXCITING_DUST, '신나는 먼지'),
#     ]
#     email = models.EmailField(unique=True)
#     # 한 이메일로 계정 한 개만 생성 가능하게?
#     nickname = models.CharField(max_length=20, blank=True, null=True)
#     dust_type = models.CharField(max_length=10, choices=DUST_CHOICES, blank=True, null=True)
#     big_star = models.PositiveIntegerField(default=0, blank=True, null=True)
#     small_star = models.PositiveIntegerField(default=0, blank=True, null=True)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     date_joined = models.DateTimeField(max_length=30, auto_now_add=True)

#     objects = UserManager()
#     # 헬퍼 클래스 지정하기
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []
#     #django는 기본적으로 username을 사용. 이메일을 username으로 사용하기!
#     class Meta:
#         db_table: 'User'

#     def __str__(self):
#         if self.nickname is None:
#             return '슈퍼유저먼지'
#         return self.nickname





# class Profile(models.Model):

#     AMBITIOUS_DUST = 'AD'
#     POPPING_DUST = 'PD'
#     TINY_DUST = 'TD'
#     EXCITING_DUST = 'ED'

#     DUST_CHOICES = [
#         ('ambitious', '야망있는 먼지'),
#         ('popping', '통통튀는 먼지'),
#         ('tiny', '조구만 먼지'),
#         ('exciting', '신나는 먼지'),
#     ]

#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', primary_key=True)
#     email = models.EmailField(max_length=255, unique=True)
#     nickname = models.CharField(max_length=20, blank=True, null=True)
#     dust_type = models.CharField(max_length=10, choices=DUST_CHOICES, blank=True, null=True)
#     big_star = models.PositiveIntegerField(default=0, blank=True, null=True)
#     small_star = models.PositiveIntegerField(default=0, blank=True, null=True)

#     class Meta:
#         db_table: 'Profile'

#     def __str__(self):
#         return self.nickname






# #User 모델의 인스턴스가 저장될 때만 메서드 호출
# #유저가 생성되면 자동으로 프로필 생성 & 저장
# # https://korinkorin.tistory.com/57
# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs): #sender - 모델 클래스 / instance - 모델의 record 데이터 / created - 레코드가 생성되었다면 True
#     if created:
#         Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()




# class UserManager(BaseUserManager):  #이거는 다시 봐야 함
# # 유저 생성 helper function 제공. user 생성할 때의 행위를 지정
#     def create_user(self, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError('email 필수 입력!')
#         user = self.model(email=self.normalize_email(email), **extra_fields) 
#         #self.model => UserManager가 속해 있는 모델에 접근
#         #normalize_email로 도메인 부분 lowercase => 중복 방지!
#         user.set_password(password)
#         # 암호화 위해서 set_password 사용함
#         user.save(using=self.db)
#         # 데이터베이스 여러 개 둘 때 사용. 굳이 안 써도 된다. 

#         return user

#     def create_superuser(self, email, password):
#         user = self.create_user(email, password)
#         user.is_staff = True
#         user.is_superuser = True
#         user.save(using=self.db)

#         return user


# class User(AbstractBaseUser, PermissionsMixin):
#     id = models.BigAutoField(primary_key=True)
#     DUST_CHOICES = [
#         ('ambitious', '야망있는 먼지'),
#         ('popping', '통통튀는 먼지'),
#         ('tiny', '조구만 먼지'),
#         ('exciting', '신나는 먼지'),
#     ]
#     email = models.EmailField(max_length=255, unique=True)
#     # 한 이메일로 계정 한 개만 생성 가능하게?
#     name = models.CharField(max_length=5)
#     nickname = models.CharField(max_length=20)
#     dust_type = models.CharField(max_length=10, choices=DUST_CHOICES)
#     big_star = models.PositiveIntegerField(default=0)
#     small_star = models.PositiveIntegerField(default=0)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)

#     objects = UserManager()
#     # 헬퍼 클래스 지정하기
#     USERNAME_FIELD = 'email'
#     #django는 기본적으로 username을 사용. 이메일을 username으로 사용하기!
#     class Meta:
#         db_table: 'User'

#     def __str__(self):
#         return self.nickname


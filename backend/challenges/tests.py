from django.test import TestCase
from django.contrib.auth import get_user_model
# Create your tests here.

class ModelTests(TestCase):

    def test_create_user_successful(self): 
        #유저 생성 확인
        email = "dustar_user@gmail.com"
        password = 'user_password'
        user = get_user_model().objects.create_user(
            email = email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        # 이메일 normalize 확인
        email = 'dustar_user@GMAIL.COM'
        user = get_user_model().objects.create_user(email, 'test_pass')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        with self.assertRaises(ValueError): #이하에서 실행하는 내용은 ValueError를 일으켜야 함
            get_user_model().objects.create_user(None, 'test_pass')

    def test_create_new_superuser(self):

        user = get_user_model().objects.create_superuser(
            'dustar_user@gmail.com',
            'test_pass'
        )
        
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    
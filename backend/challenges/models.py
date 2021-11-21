from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
#                                         PermissionsMixin
from account.models import User
from django.conf import settings
from django.db.models.fields import BooleanField

class Challenge(models.Model):
    PERIOD_CHOICES = [
        ('OW', '1주'),
        ('TW', '2주'),
        ('THW', '3주'),
        ('FW', '4주'),
    ]
    title = models.CharField(max_length=255)
    max_people = models.PositiveIntegerField(default=0)
    period = models.CharField(max_length=3, choices=PERIOD_CHOICES)
    big_star = models.PositiveIntegerField(default=0)
    small_star = models.PositiveIntegerField(default=0)
    description = models.TextField()
    creator = models.ForeignKey(User, on_delete = models.CASCADE, related_name='challenges')
    is_full = models.BooleanField(default=False)
    participants = models.ManyToManyField(User, related_name='participating')

    class Meta:
        db_table: 'challenges'

    def __str__(self):
        return self.title
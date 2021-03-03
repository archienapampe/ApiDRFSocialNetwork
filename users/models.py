from django.contrib.auth.models import AbstractUser
from activity_log.models import UserMixin


class User(AbstractUser, UserMixin):
    pass

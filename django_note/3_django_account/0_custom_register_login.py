# model for custom register

""" 
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
"""
        # এটি একটি base class যা custom user model তৈরি করতে ব্যবহৃত হয়। আপনি যদি AbstractBaseUser ব্যবহার করেন, তাহলে আপনাকে BaseUserManager ব্যবহার করে user creation এর জন্য create_user() এবং create_superuser() মেথড ডিফাইন করতে হবে।
"""
class CustomManager(BaseUserManager):
    def create_user(self, email, user_name, password, **extra_fields):
        if not email:
            raise ValueError('Email address is required')
        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, user_name, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_verify', True)
        extra_fields.setdefault('user_type', 'developer')

        if extra_fields.get('is_staff') is not True:
            raise ValueError('superuser must be is_staff=true')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('superuser must be is_superuser=true')
        if extra_fields.get('is_active') is not True:
            raise ValueError('superuser must be is_active=true')
        if extra_fields.get('is_verify') is not True:
            raise ValueError('superuser must be is_verify=true')
        
        return self.create_user(email, user_name, password, **extra_fields)
"""
        # এটি একটি base class যা custom user model তৈরি করতে ব্যবহার করা হয়। এটি ডিফল্ট user model এর মতো password hashing এবং authentication এর জন্য প্রয়োজনীয় মেথড প্রদান করে।
"""
class User(AbstractBaseUser, PermissionsMixin):
    USER_TYPE = (
        ('visitor', 'visitor'),
        ('developer', 'developer')
        )

    email = models.EmailField(unique=True)
    user_name = models.CharField(max_length=100, unique=True)
    REQUIRED_FIELDS = ['user_name']
    USERNAME_FIELD = 'email'
    user_type = models.CharField(max_length=100, choices=USER_TYPE, default=USER_TYPE[0])
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_verify = models.BooleanField(default=False)
    
    objects = CustomManager()

    def __str__(self):
        return str(self.email)

"""
# backend.py | gmail or username diye login
"""
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user, get_user_model
from django.db.models import Q
from django.db.models.base import Model

User = get_user_model()
class UsernameOrEmail(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(user_name__iexact=username) | Q(email__iexact=username))

        except User.DoesNotExist:
            User().set_password(password)
            return
        except User.MultipleObjectsReturned:
            user = User.objects.filter(Q(user_name__iexact=username) | Q(email__iexact=username)).order_by('id').first()
        if user.check_password(password) and self.user_can_authenticate(user):
            return user
"""
# setting all
""" 
AUTH_USER_MODEL = 'home.User' # custom register ar jonno
AUTHENTICATION_BACKENDS = ['home.backend.UsernameOrEmail'] # app name, file, 
"""




# messages.debug(request, "%s SQL statements were executed." % count)
# messages.info(request, "Three credits remain in your account.")
# messages.success(request, "Profile details updated.")
# messages.warning(request, "Your account expires in three days.")
# messages.error(request, "Document deleted.")
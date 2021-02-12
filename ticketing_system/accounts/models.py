from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
#from django.conf import settings
from django.utils import timezone

# Create your models here.
class MyAccountManager(BaseUserManager):
    def _create_user(self, email, password, is_staff, is_superuser):
        if not email:
            raise ValueError("User must have email address")
       
        now = timezone.now()
        user = self.model(
            email=self.normalize_email(email),
            is_staff=is_staff,
            is_active=True,
            is_superuser=is_superuser,
            last_login=now,
            date_joined=now,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None):
        return self._create_user(email, password, False, False)

    def create_superuser(self, email, password):
        user = self._create_user(email, password, True, True)
        user.save(using=self._db)
        return user

        
class User(AbstractBaseUser, PermissionsMixin):
    #user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin  = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    first_name = models.CharField(verbose_name="first name", max_length=50)
    last_name = models.CharField(verbose_name="last name", max_length=50)
    phone_number = models.CharField(verbose_name="phone number", max_length=10, blank=True)
    address = models.CharField(verbose_name="address", max_length=150, blank=True)
    city = models.CharField(max_length=50, blank=True)
  


    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = 'username'
    REQUIRED_FIELDS =[]

    objects = MyAccountManager()

    #def __str__(self):
        #return self.email

    #def has_perm(self, perm, obj=None):
        #return self.is_admin

    #def has_module_perms(self, app_label):
        #return True

    def get_absolute_url(self):
        return "/users/%i/" % (self.pk)

    def get_email(self):
        return self.email


class user_type(models.Model):
    is_client = models.BooleanField(default=False)
    is_spuser = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        if self.is_client == True:
            return User.get_email(self.user) + " - is_client"
        else:
            return User.get_email(self.user) + " - is_spuser"
            
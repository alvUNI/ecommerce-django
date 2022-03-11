from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.

class MyAccountManager(BaseUserManager):                                # Creacion de un usuario
    def create_user(self, first_name, last_name, username, email, password=None):
        if not email:
            raise ValueError('el usuario debe tener un email')

        if not username:
            raise ValueError('el usuario debe tener username')

        user = self.model(
            email      = self.normalize_email(email),
            username   = username,
            first_name = first_name,
            last_name  = last_name,
        )

        user.set_password(password)
        user.save(using = self._db)     # Para insertarlo en la base de datos

        return user

    def create_superuser(self, first_name, last_name, email, username, password):
        user = self.create_user(
            email      = self.normalize_email(email),
            username   = username,
            first_name = first_name,
            last_name  = last_name,
            password   = password,
        )

        user.is_admin       = True
        user.is_active      = True
        user.is_staff       = True
        user.is_superadmin  = True
        user.save(using = self._db)

        return user

class Account(AbstractBaseUser):
    first_name   = models.CharField(max_length=50)
    last_name    = models.CharField(max_length=50)
    username     = models.CharField(max_length=50,  unique = True)
    email        = models.CharField(max_length=100, unique = True)
    phone_number = models.CharField(max_length=50,  unique = True)

    #Campos atributos django
    date_joined    = models.DateTimeField(auto_now_add = True) # fecha en la q se esta uniendo el usuario
    last_login     = models.DateTimeField(auto_now_add = True) # ultima ves en la q inicio sesion
    is_admin       = models.BooleanField(default = False)      # para ver si es administrador el usuario
    is_staff       = models.BooleanField(default = False)      # es parte del staff
    is_active      = models.BooleanField(default = False)
    is_superadmin  = models.BooleanField(default = False)

    USERNAME_FIELD = 'email' # indica q para ingresar se usara el email
    REQUIRED_FIELDS= ['username', 'first_name', 'last_name'] # campos obligatorios

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True

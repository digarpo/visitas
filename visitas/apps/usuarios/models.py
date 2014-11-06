from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

from django.conf import settings


class UserManager(BaseUserManager, models.Manager):
    def _create_user(self, username, email, password, is_staff,
                     is_superuser, **extra_fields):
        email = self.normalize_email(email)
        if not email:
            raise ValueError('El email debe ser obligatorio')
        user = self.model(username=username, email=email, is_active=True,
                          is_staff=is_staff, is_superuser=is_superuser, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email, password=None, **extra_fields):
        return self._create_user(username, email, password, False,
                                 False, **extra_fields)

    def create_superuser(self, username, email, password=None, **extra_fields):
        return self._create_user(username, email, password, True,
                                 True, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='users')  # falta hacer algo

    objects = UserManager()

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def get_short_name(self):
        return self.username


USERNAME_FIELD = 'username'
REQUIRED_FIELDS = ['email']


def get_short_name(self):
    return self.username


class UserDepartment(User):
    departament = models.CharField(max_length=100)

    def __unicode__(self):
        return " %s" % (self.user.username)


class UserCentral(User):
    plant = models.CharField(max_length=100)

    def __unicode__(self):
        return "%s" % (self.user.username)


class UserCoordinate(User):
    def __unicode__(self):
        return "%s" % (self.user.username)


class UserCompany(User):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    phone = models.CharField(max_length=7)
    mobile = models.CharField(max_length=7)
    CIF = models.CharField(max_length=100)
    activity = models.CharField(max_length=500)
    revision = models.DateTimeField()
    subcontrate = models.CharField(max_length=100)

    def __unicode__(self):
        return "%s" % (self.user.username)


class UserWorkers(UserCompany):
    nameWorker = models.CharField(max_length=100)
    TA2_date = models.DateTimeField()
    TA2_doc = models.FileField(upload_to='usuarios')
    medical = models.DateTimeField()
    information = models.DateTimeField()
    formation_date = models.DateTimeField()
    EPI_date = models.DateTimeField()
    EPI_doc = models.FileField(upload_to='EPI')
    medical_doc = models.FileField(upload_to='medical')
    information_doc = models.FileField(upload_to='information')
    skill_doc = models.FileField(upload_to='skill')


    def __unicode__(self):
        return "%s" % (self.user.username)


class UserDocs(models.Model):
    user = models.ForeignKey(UserWorkers, unique=True)
    TC2 = models.FileField(upload_to='TC2')
    safe = models.FileField(upload_to='safe')
    ssocial = models.FileField(upload_to='ssocial')
    notETT = models.FileField(upload_to='notETT')
    risk = models.FileField(upload_to='risk')
    protection = models.FileField(upload_to='protection')
    ICCo = models.CharField(max_length=100)
    ICSyva = models.CharField(max_length=100)
    PRL03 = models.CharField(max_length=100)
    PRL04 = models.CharField(max_length=100)


    def __unicode__(self):
        return "%s" % (self.user.username)


class UserAnexoTrobajo(models.Model):
    user = models.ForeignKey(UserCompany, unique=True)

    FA = models.FileField(upload_to='anexosTR')
    FB = models.FileField(upload_to='anexosTR')
    F1 = models.FileField(upload_to='anexosTR')
    F2 = models.FileField(upload_to='anexosTR')
    F3 = models.FileField(upload_to='anexosTR')
    F4 = models.FileField(upload_to='anexosTR')
    F5 = models.FileField(upload_to='anexosTR')
    F6 = models.FileField(upload_to='anexosTR')
    F7 = models.FileField(upload_to='anexosTR')
    F8 = models.FileField(upload_to='anexosTR')
    F9 = models.FileField(upload_to='anexosTR')
    F10 = models.FileField(upload_to='anexosTR')
    F11 = models.FileField(upload_to='anexosTR')
    F12 = models.FileField(upload_to='anexosTR')
    F13 = models.FileField(upload_to='anexosTR')
    F14 = models.FileField(upload_to='anexosTR')
    F15 = models.FileField(upload_to='anexosTR')
    F16 = models.FileField(upload_to='anexosTR')
    F17 = models.FileField(upload_to='anexosTR')
    F18 = models.FileField(upload_to='anexosTR')
    F19 = models.FileField(upload_to='anexosTR')
    F20 = models.FileField(upload_to='anexosTR')
    F21 = models.FileField(upload_to='anexosTR')
    F22 = models.FileField(upload_to='anexosTR')
    F23 = models.FileField(upload_to='anexosTR')
    F24 = models.FileField(upload_to='anexosTR')
    F25 = models.FileField(upload_to='anexosTR')
    F26 = models.FileField(upload_to='anexosTR')
    F27 = models.FileField(upload_to='anexosTR')


    def __unicode__(self):
        return "%s" % (self.user.username)


class UserAnexoParque(models.Model):
    user = models.ForeignKey(UserCompany, unique=True)

    IA = models.FileField(upload_to='anexosParque')
    IB = models.FileField(upload_to='anexosParque')
    I1 = models.FileField(upload_to='anexosParque')
    I2 = models.FileField(upload_to='anexosParque')
    I3 = models.FileField(upload_to='anexosParque')
    I4 = models.FileField(upload_to='anexosParque')
    I5 = models.FileField(upload_to='anexosParque')
    I6 = models.FileField(upload_to='anexosParque')
    I7 = models.FileField(upload_to='anexosParque')
    I8 = models.FileField(upload_to='anexosParque')
    I9 = models.FileField(upload_to='anexosParque')
    I10 = models.FileField(upload_to='anexosParque')
    I11 = models.FileField(upload_to='anexosParque')
    I12 = models.FileField(upload_to='anexosParque')
    I13 = models.FileField(upload_to='anexosParque')
    I14 = models.FileField(upload_to='anexosParque')
    I15 = models.FileField(upload_to='anexosParque')
    I16 = models.FileField(upload_to='anexosParque')
    I17 = models.FileField(upload_to='anexosParque')
    I18 = models.FileField(upload_to='anexosParque')
    I19 = models.FileField(upload_to='anexosParque')
    I20 = models.FileField(upload_to='anexosParque')
    I21 = models.FileField(upload_to='anexosParque')
    I22 = models.FileField(upload_to='anexosParque')
    I23 = models.FileField(upload_to='anexosParque')
    I24 = models.FileField(upload_to='anexosParque')
    I25 = models.FileField(upload_to='anexosParque')
    I26 = models.FileField(upload_to='anexosParque')
    I27 = models.FileField(upload_to='anexosParque')
    I28 = models.FileField(upload_to='anexosParque')
    I29 = models.FileField(upload_to='anexosParque')
    I30 = models.FileField(upload_to='anexosParque')


    def __unicode__(self):
        return "%s" % (self.user.username)
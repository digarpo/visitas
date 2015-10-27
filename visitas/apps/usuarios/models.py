from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

from django.conf import settings


class UserManager(BaseUserManager, models.Manager):
    def _create_user(self, username, email, password, is_staff,
                     is_superuser,is_company,is_worker,is_usuario,is_centralita,is_coordinador, **extra_fields):
        email = self.normalize_email(email)
        if not email:
            raise ValueError('El email debe ser obligatorio')
        user = self.model(username=username, email=email, is_active=True,
                          is_staff=is_staff, is_superuser=is_superuser,is_company=is_company,
                          is_worker = is_worker,is_usuario = is_usuario,is_centralita = is_centralita,
                          is_coordinador = is_coordinador, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email, password=None, **extra_fields):
        return self._create_user(username, email, password, False,
                                 False,False,False,False,False,False, **extra_fields)

    def create_superuser(self, username, email, password=None, **extra_fields):
        return self._create_user(username, email, password, True,
                                 True,False,False,False,False,False, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField()
    first_name = models.CharField(max_length=100,blank=True)
    last_name = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='users',blank=True )

    objects = UserManager()

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    is_company = models.BooleanField(default=False)
    is_worker = models.BooleanField(default=False)
    is_usuario = models.BooleanField(default=False)
    is_centralita = models.BooleanField(default=False)
    is_coordinador = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def get_short_name(self):
        return self.username



class UserDepartment(User):
    departament = models.CharField(max_length=100)


    class Admin:
        pass

    def __unicode__(self):
        return "%s" % (self.username)

class UserCentral(User):
    plant = models.CharField(max_length=100)

    def __unicode__(self):
        return "%s" % (self.username)


class UserCompany(User):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    phone = models.CharField(max_length=7)
    mobile = models.CharField(max_length=7)
    CIF = models.CharField(max_length=100)
    activity = models.CharField(max_length=500,blank=True)
    #revision = models.DateTimeField(blank=True)
    subcontrate = models.CharField(max_length=100)

    class Admin:
        pass

    def __unicode__(self):
        return "%s" % (self.username)


class UserWorkers(UserCompany):
    TA2_date = models.DateTimeField()
    TA2_doc = models.FileField(upload_to='usuarios',blank=True)
    medical = models.DateTimeField()
    information = models.DateTimeField()
    formation_date = models.DateTimeField()
    EPI_date = models.DateTimeField()
    EPI_doc = models.FileField(upload_to='EPI',blank=True)
    medical_doc = models.FileField(upload_to='medical',blank=True)
    information_doc = models.FileField(upload_to='information',blank=True)
    skill_doc = models.FileField(upload_to='skill',blank=True)

    class Admin:
        pass

    def __unicode__(self):
        return "%s" % (self.username)

#class Docs(models.Model):
#    name = models.CharField(max_lenght=500)
#    validate = models.BooleanField()


#class Doc_User(models.Model):
##    doc = models.ForeignKey('Docs')
#    user = models.ForeignKey('User')
#    type_doc = models.Choices(['FA',])
#    read = models.BooleanField()


class UserDocs(models.Model):
    user = models.ForeignKey(UserWorkers, unique=True)
    TC2 = models.FileField(upload_to='TC2',blank=True)
    safe = models.FileField(upload_to='safe',blank=True)
    ssocial = models.FileField(upload_to='ssocial',blank=True)
    notETT = models.FileField(upload_to='notETT',blank=True)
    risk = models.FileField(upload_to='risk',blank=True)
    protection = models.FileField(upload_to='protection',blank=True)
    ICCo = models.CharField(max_length=100)
    ICSyva = models.CharField(max_length=100)
    PRL03 = models.CharField(max_length=100)
    PRL04 = models.CharField(max_length=100)


    def __unicode__(self):
        return "%s" % (self.username)



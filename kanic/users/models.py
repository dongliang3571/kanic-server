from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.db import models
from django.db.models.signals import post_save
from django.utils import timezone


class UserManager(BaseUserManager):
    def create_user(self, email, phone, password=None, is_mechanic=False):
        """
        Creates and saves a User with the given email, phone and password.
        """

        if not email:
            raise ValueError('Users must have an email address')
        if not phone:
            raise ValueError('Users must have an phone number')

        user = self.model(email=self.normalize_email(email), phone=phone)
        user.set_password(password)
        user.is_mechanic = is_mechanic
        user.save(using=self._db)
        return user

    def create_superuser(self, email, phone, password):
        """
        Creates and saves a superuser with the given email, phone and password.
        """
        user = self.create_user(email=email, phone=phone, password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user

    def exclude_admin(self):
        return super(UserManager, self).filter(is_admin=False)

    def all_mechanic(self):
        return self.exclude_admin().filter(is_mechanic=True)

    def all_car_owner(self):
        return self.exclude_admin().filter(is_mechanic=False)


class User(AbstractBaseUser):
    username = models.CharField(max_length=255, unique=True, null=True, blank=True)
    email = models.EmailField(verbose_name='email address', max_length=255,
                              unique=True)
    phone = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    is_mechanic = models.BooleanField(verbose_name="Is Mechanic", default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    date_joined = models.DateTimeField(verbose_name='date joined',
                                       default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone']

    def get_full_name(self):
        # The user is identified by their email address
        return "%s %s" %(self.first_name, self.last_name)

    def get_short_name(self):
        # The user is identified by their email address
        return self.first_name

    def __unicode__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    def get_nested_attributes_for_serializer(self):
        '''This method is for model Request to get nested attribute of mode User'''
        data = {
            'id': self.id,
            'email': self.email,
            'phone': self.phone,
            'first_name': self.first_name,
            'last_name': self.last_name
        }
        return data


class Mechanic(models.Model):
    user = models.OneToOneField(User)
    year_of_experience = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)

    def __unicode__(self):
        return self.user.email

    def get_nested_attributes_for_serializer(self):
        data = {
            'mechanic_id': self.id,
            'user_id': self.user.id,
            'email': self.user.email,
            'phone': self.user.phone,
            'first_name': self.user.first_name,
            'last_name': self.user.last_name,
            'year_of_experience': self.year_of_experience,
            'address': self.address
        }
        return data

def new_user_receiver(sender, instance, created, *args, **kwargs):
    if created and instance.is_mechanic:
        mechanic, is_created = Mechanic.objects.get_or_create(user=instance)
    elif created:
        pass


post_save.connect(new_user_receiver, sender=User)

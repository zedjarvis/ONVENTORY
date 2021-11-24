from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import (AbstractBaseUser,
                                        PermissionsMixin,
                                        BaseUserManager
                                        )
from django.db.models.signals import post_save
from django.dispatch import receiver


# Custom User Manager Model
class CustomAccountManager(BaseUserManager):

    def create_user(self, email, username, password, **other_fields):
        if not email:
            raise ValueError(_('You must provide an email address'))
        if not password:
            raise ValueError(_('User must have a password'))

        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **other_fields)
        user.set_password(password)
        user.save()

        return user

    def create_staffuser(self, email, username, password, **other_fields):
        other_fields.setdefault('is_staff', True)

        if not other_fields.get('is_staff'):
            raise ValueError(
                _('staff member must be assigned to is_staff: True')
                )

        return self.create_user(email, username, password, **other_fields)

    def create_superuser(self, email, username, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if not other_fields.get('is_staff'):
            raise ValueError(_('Superuser must be assigned to is_staff: True'))

        if not other_fields.get('is_superuser'):
            raise ValueError(
                _('Superuser must be assigned to is_superuser: True')
            )

        return self.create_user(email, username, password, **other_fields)


# Custom User Model
class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(_('Email address'), max_length=255, unique=True)
    username = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    date_joined = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_employed = models.BooleanField(default=False)
    has_accepted_terms = models.BooleanField(default=False)

    objects = CustomAccountManager()  # usermanager

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username


# Extending user Profile attributes
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # inventory related objects
    updated_on = models.DateTimeField(auto_now=True)
    phone_no = models.CharField(max_length=50, blank=True, null=True)
    profile_image = models.ImageField(default='default.png',
                                      upload_to='media/',
                                      null=True, blank=True)

    class Meta:
        ordering = ['-updated_on']

    def __str__(self):
        return self.user.username


class Notification(models.Model):
    message = models.TextField()
    viewed = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    viewed_on = models.DateTimeField(auto_now=True)
    time = models.TimeField(auto_now=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='notifications')

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_welcome_message(sender, **kwargs):
    if kwargs.get('created', False):
        Notification.objects.create(user=kwargs.get('instance'),
                                    message="Welocome to your\
                                        Online Inventory \
                                            System...now the job begins...")

        Notification.objects.create(user=kwargs.get('instance'),
                                    message="ONventory is in beta mode. \
                                         Services are not\
                                             charged at the moment.")


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


# Model to store the list of logged in Users
# used to make sure only one instance of a user is
# logged in at a particular time
class LoggedInUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='logged_in_user')
    # session keys are 32 characters long
    session_key = models.CharField(max_length=32, null=True, blank=True)

    def __str__(self):
        return self.user.username

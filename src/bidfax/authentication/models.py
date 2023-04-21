import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser

from bidfax.authentication.managers import UserManager


class User(AbstractUser):
    uid = models.UUIDField(
        db_index=True,
        default=uuid.uuid4,
        unique=True,
        editable=False
    )
    username = None
    email = models.EmailField(max_length=255, help_text='Required. Inform a valid email address.', unique=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Profile(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Имя', help_text='Your First Name.')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия', help_text='Your Second Name.')
    avatar = models.ImageField(verbose_name='Изображение', help_text='Choose a picture.', blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return str(self.user)


# @receiver(post_save, sender=User)
# def create_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(
#             user=instance
#             )
#     instance.profile.save()

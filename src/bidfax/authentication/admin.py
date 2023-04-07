from django.contrib import admin
from django.contrib.auth import get_user_model

from bidfax.authentication.models import Profile

admin.site.register(get_user_model())
admin.site.register(Profile)

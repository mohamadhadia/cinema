from django.contrib import admin

from .models import Profile
from .models import Payment

admin.site.register(Profile)
admin.site.register(Payment)

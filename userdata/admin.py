from django.contrib import admin
from .models import UserProfileData,Comment,Children
# Register your models here.
admin.site.register(UserProfileData)
admin.site.register(Comment)
admin.site.register(Children)

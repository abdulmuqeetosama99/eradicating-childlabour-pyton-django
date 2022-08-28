from django.contrib import admin
from .models import Ngo, NgoMember,Volunteer
# Register your models here.
admin.site.register(Ngo)
admin.site.register(NgoMember)
admin.site.register(Volunteer)

from __future__ import unicode_literals
from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class Volunteer(models.Model):
    username        =  models.CharField(max_length=50,default='user',primary_key=True)
    first_name      = models.CharField(max_length=50,default=None)
    last_name       = models.CharField(max_length=50,default=None)
    email           = models.EmailField(default='example23@gmail.com', max_length=254)
    contact_no      = PhoneNumberField(blank=True, help_text='Contact phone number')
    volunteer_id    = models.IntegerField()
    Adharno         = models.BigIntegerField()
    verified        = models.BooleanField(default=False)

    objects = models.Manager()

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse("volunteer-detail", kwargs={"pk": self.username})




class Ngo(models.Model):
    name            = models.CharField(max_length=100,default='ngo',primary_key=True)
    manager_name    = models.CharField(max_length=100)
    email           = models.EmailField(default='example23@gmail.com', max_length=254)
    contact_no      = PhoneNumberField(blank=True, help_text='Contact phone number')
    address         = models.CharField(max_length=50)
    city            = models.CharField(max_length=30)
    state           = models.CharField(max_length=30)
    document        = models.FileField(upload_to='document/ngo',blank=True)
    verify          = models.BooleanField(default=False)
    objects = models.Manager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("ngo-detail", kwargs={"pk": self.name})

class NgoMember(models.Model):
    username        =  models.CharField(max_length=50,default='user',primary_key=True)
    first_name      = models.CharField(max_length=50,default=None)
    last_name       = models.CharField(max_length=50,default=None)
    email           = models.EmailField(default='example23@gmail.com', max_length=254)
    contact_no      = PhoneNumberField(blank=True, help_text='Contact phone number')
    ngo_name        = models.ForeignKey(Ngo, on_delete=models.CASCADE)
    Adharno         = models.BigIntegerField()
    ngo_id          = models.IntegerField()
    designation     = models.CharField(max_length=100)
    is_manager      = models.BooleanField(default=False)
    ngo_verified   = models.BooleanField(default=False)

    objects = models.Manager()
    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse("ngo-member-detail", kwargs={"pk": self.username})
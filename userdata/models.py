from __future__ import unicode_literals
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class UserProfileData(models.Model):
    username        =  models.CharField(max_length=50,default='user',primary_key=True)
    first_name      = models.CharField(max_length=50,default=None)
    last_name       = models.CharField(max_length=50,default=None)
    profile_pic = models.ImageField(upload_to='image/users',blank=True)
    MALE        = 'male'
    FEMALE      = 'female'
    OTHERS      = 'others'
    gender_type     = [(MALE, 'Male'),(FEMALE , 'Female'),(OTHERS , 'Others'),]
    gender          = models.CharField(max_length=6,choices =  gender_type )
    age             = models.IntegerField(default=None)
    address         = models.CharField(max_length=50)
    city            = models.CharField(max_length=30)
    state           = models.CharField(max_length=30)
    contact_no      = PhoneNumberField(blank=True, help_text='Contact phone number')
    is_volunteer    = models.BooleanField(default=False)
    is_ngo_member    = models.BooleanField(default=False)
    accept          = models.BooleanField(default=False)
    
    def __str__(self):
        return self.username

    
    objects = models.Manager()
    def get_absolute_url(self):
        return reverse("userprofile-detail", kwargs={"pk": self.username})

class Children(models.Model):
    user_name   = models.CharField(max_length=50,default=None)
    full_name   = models.CharField(max_length=50,default=None)
    child_id    = models.IntegerField()
    image = models.ImageField(upload_to='image/child',blank=True)
    MALE        = 'male'
    FEMALE      = 'female'
    OTHERS      = 'others'
    gender_type     = [(MALE, 'Male'),(FEMALE , 'Female'),(OTHERS , 'Others'),]
    gender          = models.CharField(max_length=6,choices =  gender_type )
    age             = models.IntegerField(default=None)
    address         = models.CharField(max_length=50)
    city            = models.CharField(max_length=30)
    state           = models.CharField(max_length=30)
    message         = models.TextField(max_length=400,default=None)
    submit_on       = models.DateTimeField(auto_now_add=True)
    verified        = models.BooleanField(default=False)
    
    objects = models.Manager()

    def save(self,*args,**kwargs):
        self.child_id = Children.objects.count()
        super(Children,self).save(*args,**kwargs)
    
    def get_absolute_url(self):
        return reverse("children-detail", kwargs={"pk": self.pk})



class Comment(models.Model):
    full_name    = models.CharField(max_length=50,default=None)
    email        = models.EmailField(default='abcd123@gmail.com')
    subject      = models.CharField(max_length=50,default=None)
    message      = models.TextField(max_length=400,default=None)
    submit_on = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    def get_absolute_url(self):
        return reverse("comment-detail", kwargs={"pk": self.pk})


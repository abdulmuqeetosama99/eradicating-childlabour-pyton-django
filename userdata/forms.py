from django import forms
from django.contrib.auth.models import User
from .models import UserProfileData,Comment,Children
class ProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfileData
        fields = ('username','first_name','last_name','profile_pic','gender','age','address','city','state','contact_no','accept')


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('full_name','email','subject','message')

class ChildrenForm(forms.ModelForm):

    class Meta:
        model = Children
        fields = ('user_name','full_name','gender','image','age','address','city','state','message')
        

class ChildImageForm(forms.ModelForm):
    class Meta:
        model = Children
        fields = ('image',)
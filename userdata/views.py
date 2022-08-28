from django.shortcuts import render,HttpResponseRedirect,redirect
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.mixins import  LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django import forms
from .forms import  ProfileForm, ChildrenForm, ChildImageForm
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from .models import (
    UserProfileData,
    Comment,
    Children,
    )
from userlog.models import NgoMember,Volunteer

from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
    FormView
)

def UserProfileOrderList(request):
    context = {
        'userprofiledatas' : UserProfileData.objects.all()
    }
    return render(request,'userdata/userprofile_list.html',context)


class UserProfileListView(LoginRequiredMixin,ListView):
    model = UserProfileData
    context_object_name = 'userprofiledatas'
    template_name = "userdata/UserProfile_list.html"
    

class UserProfileDetailView(LoginRequiredMixin,DetailView):
    model = UserProfileData



class UserProfileCreateView(LoginRequiredMixin,CreateView):
    model = UserProfileData
    fields = ['username','first_name','last_name','gender','age','address','city','state','contact_no']

    def form_valid(self,form):
        form.instance.username = self.request.user
        return super().form_valid(form)


class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = UserProfileData
    fields = ['username','first_name','last_name','gender','age','address','city','state','contact_no']


    def form_valid(self,form):
        form.instance.username = self.request.user
        return super().form_valid(form)
        


class UserProfileDeleteView(LoginRequiredMixin,DeleteView):
    model = UserProfileData
    success_url = '/userprofile_list'

    def test_func(self):
        userprofiledata = self.get_object()
        if self.request.user == userprofiledata.username:
            return True
        return False


def my_profile(request):
    try:
        u_name = request.user
        userprofiledata = UserProfileData.objects.get(username=u_name)
        response = redirect('/userprofile/'+userprofiledata.username)
        return response
    except ObjectDoesNotExist:
        response = redirect('/userprofile/new')
        return response

# NGO member redirect
def ngo_member(request):
    try:
        u_name = request.user
        ngomember = NgoMember.objects.get(username=u_name)
        response = redirect('/ngo_member/'+ngomember.username)
        return response
    except ObjectDoesNotExist:
        response = redirect('/ngo_member/new')
        return response

# Volunteer redirect
def Volunteer_member(request):
    try:
        u_name = request.user
        volunteer = Volunteer.objects.get(username=u_name)
        response = redirect('/volunteer/'+volunteer.username)
        return response
    except ObjectDoesNotExist:
        response = redirect('/volunteer/new')
        return response



def ChildrenList(request):
    context = {
        'childrens' : Children.objects.all(),
        'userprofiles': UserProfileData.objects.all()
    }
    return render(request,'userdata/children_list.html',context)


class ChildrenListView(LoginRequiredMixin,ListView):
    model = Children
    context_object_name = 'childrens'
    template_name = "userdata/children_list.html"
    

class ChildrenDetailView(LoginRequiredMixin,DetailView):
    model = Children

class ChildrenCreateView(LoginRequiredMixin,CreateView):
    model = Children
    fields = ['user_name','full_name','gender','age','address','city','state','message']

    def form_valid(self,form):
        form.instance.username = self.request.user
        return super().form_valid(form)



class ChildrenUpdateView(LoginRequiredMixin, UpdateView):
    model = Children
    fields = ['full_name','gender','age','address','city','state','message']

    def form_valid(self,form):
        form.instance.username = self.request.user
        return super().form_valid(form)

class ChildrenVerifyUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'userdata/children_verify_form.html'
    model = Children
    fields = ['verified']


    def form_valid(self,form):
        form.instance.username = self.request.user
        return super().form_valid(form)

class ChildrenDeleteView(LoginRequiredMixin,DeleteView):
    model = Children
    success_url = '/children_list'

    def test_func(self):
        Children = self.get_object()
        if self.request.user == Children.username:
            return True
        return False



class ChildImageUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'userdata/childimage_form.html'
    model = Children
    fields = ['image']
    

    def form_valid(self,form):
        form.instance.username = self.request.user
        return super().form_valid(form)

class ProfilePicUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'userdata/userprofile_image.html'
    model = UserProfileData
    fields = ['profile_pic']


    def form_valid(self,form):
        form.instance.username = self.request.user
        return super().form_valid(form)


def CommentList(request):
    context = {
        'comments' : Comment.objects.all()
    }
    return render(request,'userdata/comment_list.html',context)


class CommentListView(LoginRequiredMixin,ListView):
    model = Comment
    context_object_name = 'comments'
    template_name = "userdata/commentlist.html"
    

class CommentDetailView(LoginRequiredMixin,DetailView):
    model = Comment

class CommentCreateView(LoginRequiredMixin,CreateView):
    model = Comment
    fields = ['full_name','email','subject','message']

    def form_valid(self,form):
        form.instance.username = self.request.user
        return super().form_valid(form)
        
class CommentDeleteView(LoginRequiredMixin,DeleteView):
    model = Comment
    success_url = '/comment_list'

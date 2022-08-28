from django.shortcuts import render,HttpResponseRedirect,redirect
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.mixins import  LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django import forms
from .forms import CustomUserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
    FormView
)
from .models import Ngo, NgoMember,Volunteer
# Create your views here.

def register(request):
    
        form = CustomUserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    
        form = CustomUserCreationForm()
        context={
        'form' : form
        }
        return render(request,'registration/register.html',context)



def login_view(request):
    username = request.POST.get('username','')
    m = User.objects.get(username=username)
    password = request.POST.get('password','')
    user =auth.authenticate(username=username,password=password)
    if user is not None and user.is_active:
        auth.login(request,user)
        request.session['member_id'] = m.id
        print("hi request.session['username']")
        return HttpResponseRedirect("/")
    else:
        return HttpResponseRedirect("/accounts/login/")


def logout(request):
    auth.logout(request)
    #del request.session['username']
    return HttpResponseRedirect("/")



# NGO Views
def NgoList(request):
    context = {
        'ngomembers' : NgoMember.objects.all(),
        'ngos' : Ngo.objects.all()
    }
    return render(request,'uselog/ngo_list.html',context)


class NgoListView(LoginRequiredMixin,ListView):
    model = Ngo
    context_object_name = 'ngos'
    template_name = "uselog/ngo_list.html"
    

class NgoDetailView(LoginRequiredMixin,DetailView):
    model = Ngo

class NgoCreateView(LoginRequiredMixin,CreateView):
    model = Ngo
    fields = ['name','manager_name','email','contact_no', 'address','city', 'state']

    def form_valid(self,form):
        form.instance.username = self.request.user
        return super().form_valid(form)



class NgoUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'userlog/ngo_update_form.html'
    model = Ngo
    fields = ['name','manager_name','email','contact_no', 'address','city', 'state']

    def form_valid(self,form):
        form.instance.username = self.request.user
        return super().form_valid(form)


class NgoDeleteView(LoginRequiredMixin,DeleteView):
    model = Ngo
    success_url = '/ngo_list'

    def test_func(self):
        Ngo = self.get_object()
        if self.request.user == Ngo.username:
            return True
        return False



class NgoDocUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'userlog/ngodocument.html'
    model = Ngo
    fields = ['document']

    def form_valid(self,form):
        form.instance.username = self.request.user
        return super().form_valid(form)


class NgoVerifyUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'userlog/ngo_verify.html'
    model = Ngo
    fields = ['verify']

    def form_valid(self,form):
        form.instance.username = self.request.user
        return super().form_valid(form)
# Ngo member Views
def NgoMemberList(request):
    context = {
        'ngomembers' : NgoMember.objects.all(),
        'ngos': Ngo.objects.all()
    }
    return render(request,'userlog/ngomember_list.html',context)


class NgoMemberListView(LoginRequiredMixin,ListView):
    model = NgoMember
    context_object_name = 'ngomembers'
    template_name = "userlog/ngomember_list.html"
    

class NgoMemberDetailView(LoginRequiredMixin,DetailView):
    model = NgoMember

class NgoMemberCreateView(LoginRequiredMixin,CreateView):
    model = NgoMember
    fields = ['username','first_name' , 'last_name' ,'email','ngo_name','contact_no' ,'Adharno','ngo_id', 'designation']

    def form_valid(self,form):
        form.instance.username = self.request.user
        return super().form_valid(form)



class NgoMemberUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'userlog/ngomember_update_form.html'
    model = NgoMember
    fields = ['first_name' , 'last_name' ,'email','ngo_name', 'contact_no' ,'Adharno','ngo_id', 'designation']

    def form_valid(self,form):
        form.instance.username = self.request.user
        return super().form_valid(form)

class NgoMemberManagerUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'userlog/ngomember_manager.html'
    model = NgoMember
    fields = ['is_manager']

    def form_valid(self,form):
        form.instance.username = self.request.user
        return super().form_valid(form)

class NgoMemberVerifyUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'userlog/ngomember_verify.html'
    model = NgoMember
    fields = ['ngo_verified']

    def form_valid(self,form):
        form.instance.username = self.request.user
        return super().form_valid(form)

class NgoMemberDeleteView(LoginRequiredMixin,DeleteView):
    model = NgoMember
    success_url = '/ngomember_list'

    def test_func(self):
        NgoMember = self.get_object()
        if self.request.user == NgoMember.username:
            return True
        return False

def VolunteerList(request):
    context = {
        'volunteers' : Volunteer.objects.all()
    }
    return render(request,'userlog/volunteer_list.html',context)


class VolunteerListView(LoginRequiredMixin,ListView):
    model = Volunteer
    context_object_name = 'volunteers'
    template_name = "userlog/volunteer_list.html"
    

class VolunteerDetailView(LoginRequiredMixin,DetailView):
    model = Volunteer

class VolunteerCreateView(LoginRequiredMixin,CreateView):
    model = Volunteer
    fields = ['username','first_name' , 'last_name' ,'email', 'contact_no' ,'Adharno', 'volunteer_id']

    def form_valid(self,form):
        form.instance.username = self.request.user
        return super().form_valid(form)



class VolunteerUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'userlog/volunteer_update_form.html'
    model = Volunteer
    fields = ['first_name' , 'last_name' ,'email', 'contact_no' ,'Adharno', 'volunteer_id']

    def form_valid(self,form):
        form.instance.username = self.request.user
        return super().form_valid(form)

class VolunteerVerifyUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'userlog/volunteer_verify.html'
    model = Volunteer
    fields = ['verified']

    def form_valid(self,form):
        form.instance.username = self.request.user
        return super().form_valid(form)


class VolunteerDeleteView(LoginRequiredMixin,DeleteView):
    model = Volunteer
    success_url = '/volunteer_list'

    def test_func(self):
        Volunteer = self.get_object()
        if self.request.user == Volunteer.username:
            return True
        return False

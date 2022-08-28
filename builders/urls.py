"""nation_builder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from django.views.generic.base import TemplateView
from userlog.views import register,login_view,logout
from userdata.views import ( 
    my_profile, ngo_member,Volunteer_member,
    UserProfileListView,CommentListView,ChildrenListView,
    UserProfileDetailView,CommentDetailView,ChildrenDetailView,
    UserProfileCreateView,CommentCreateView,ChildrenCreateView,
    UserProfileUpdateView,ChildrenUpdateView,ChildImageUpdateView,ProfilePicUpdateView,
    UserProfileDeleteView,CommentDeleteView,ChildrenDeleteView,
)
from userlog.views import ( 
    NgoListView,NgoDetailView,NgoCreateView,NgoUpdateView,NgoDeleteView,NgoDocUpdateView,NgoVerifyUpdateView,
    NgoMemberListView,NgoMemberDetailView,NgoMemberCreateView,NgoMemberUpdateView,NgoMemberDeleteView,
    NgoMemberVerifyUpdateView, NgoMemberManagerUpdateView,
    VolunteerListView,VolunteerDetailView,VolunteerCreateView,VolunteerUpdateView,VolunteerDeleteView,VolunteerVerifyUpdateView   
    )
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('django.contrib.auth.urls')),
    path('accounts/login/', login_view),
    path('register/', register,name='register'),
    path('logout/', logout,name='logout'),
    path('', TemplateView.as_view(template_name='index.html'),name='home'),
    path('about/', TemplateView.as_view(template_name='about.html'),name='about'),
    path('contact/', TemplateView.as_view(template_name='contact.html'),name='contact'),
# rediecting
    path('my_profile/', my_profile,name='my_profile'),
    path('my_member/', ngo_member,name='my_member'),
    path('my_volunteer/',Volunteer_member,name='my_volunteer'),
# userdata UserProfileData
    path('userprofile/new', UserProfileCreateView.as_view(),name='userprofile-create'),
    path('userprofile_list', UserProfileListView.as_view(),name='userprofile-list'),
    path('userprofile/<str:pk>/', UserProfileDetailView.as_view(),name='userprofile-detail'),
    path('userprofile/<str:pk>/update', UserProfileUpdateView.as_view(),name='userprofile-update'),
    path('userprofile/<str:pk>/delete', UserProfileDeleteView.as_view(),name='userprofile-delete'),
    path('userprofile/<str:pk>/image',ProfilePicUpdateView.as_view(),name='userprofile-image'),
# userdata Children
    path('children/new', ChildrenCreateView.as_view(),name='children-create'),
    path('children_list', ChildrenListView.as_view(),name='children-list'),
    path('children/<int:pk>/', ChildrenDetailView.as_view(),name='children-detail'),
    path('children/<int:pk>/update', ChildrenUpdateView.as_view(),name='children-update'),
    path('children/<int:pk>/delete', ChildrenDeleteView.as_view(),name='children-delete'),
    path('children/<int:pk>/image',ChildImageUpdateView.as_view(),name='children-image'),

# userdata Comment
    path('comment/new', CommentCreateView.as_view(),name='comment-create'),
    path('comment_list', CommentListView.as_view(),name='comment-list'),
    path('comment/<int:pk>/', CommentDetailView.as_view(),name='comment-detail'),
    path('comment/<int:pk>/delete', CommentDeleteView.as_view(),name='comment-delete'),

# userlog NGO
    path('ngo/new', NgoCreateView.as_view(),name='ngo-create'),
    path('ngo_list', NgoListView.as_view(),name='ngo-list'),
    path('ngo/<str:pk>/', NgoDetailView.as_view(),name='ngo-detail'),
    path('ngo/<str:pk>/update', NgoUpdateView.as_view(),name='ngo-update'),
    path('ngo/<str:pk>/delete', NgoDeleteView.as_view(),name='ngo-delete'),
    path('ngo/<str:pk>/document',NgoDocUpdateView.as_view(),name='ngo-doc'),
    path('ngo/<str:pk>/verify',NgoVerifyUpdateView.as_view(),name='ngo-verify'),
# userlog NGO Members
    path('ngo_member/new', NgoMemberCreateView.as_view(),name='ngo-member-create'),
    path('ngo_member_list', NgoMemberListView.as_view(),name='ngo-member-list'),
    path('ngo_member/<str:pk>/', NgoMemberDetailView.as_view(),name='ngo-member-detail'),
    path('ngo_member/<str:pk>/update', NgoMemberUpdateView.as_view(),name='ngo-member-update'),
    path('ngo_member/<str:pk>/delete', NgoMemberDeleteView.as_view(),name='ngo-member-delete'),
    path('ngo_member/<str:pk>/verify',NgoMemberVerifyUpdateView.as_view(),name='ngo-member-verify'),
    path('ngo_member/<str:pk>/manager',NgoMemberManagerUpdateView.as_view(),name='ngo-member-verify-manager'),
# userlog Volunteer
    path('volunteer/new', VolunteerCreateView.as_view(),name='volunteer-create'),
    path('volunteer_list', VolunteerListView.as_view(),name='volunteer-list'),
    path('volunteer/<str:pk>/', VolunteerDetailView.as_view(),name='volunteer-detail'),
    path('volunteer/<str:pk>/update', VolunteerUpdateView.as_view(),name='volunteer-update'),
    path('volunteer/<str:pk>/delete', VolunteerDeleteView.as_view(),name='volunteer-delete'),
    path('volunteer/<str:pk>/verify',VolunteerVerifyUpdateView.as_view(),name='volunteer-verify')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

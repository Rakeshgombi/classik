from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="Home"),
    path('search/', views.search, name="Search"),
    path('createclass/', views.createClass, name="createclass"),
    path('joinclass/', views.joinClass, name="joinclass"),
    path('people/<int:slug>/', views.people, name="People"),
    path('deleteclass/<str:slug>/', views.deleteclass, name="deleteclass"),
    path('classroom/<int:slug>/', views.classRoom, name="Classroom"),
    path('editAnnouncement/<int:slug>/', views.editAnnouncement, name="editAnnouncement"),
    path('deleteAnnouncement/<str:slug>/', views.deleteAnnouncement, name="deleteAnnouncement"),
    path('editclass/<int:slug>/', views.editclass, name="editclass"),
    path('otp/', views.sendOtp, name="sendOtp"),
    path('signup/', views.handleSignUp, name="signup"),
    path('login/', views.handleLogIn, name="login"),
    path('logout/', views.handleLogout, name="logout"),
]
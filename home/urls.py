from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="Home"),
    path('createclass/', views.createClass, name="createclass"),
    path('search/', views.search, name="To-do"),
    path('joinclass/', views.joinClass, name="joinclass"),
    path('people/<int:slug>/', views.people, name="joinclass"),
    path('editclass/<int:slug>/', views.editclass, name="joinclass"),
    path('deleteclass/<str:slug>/', views.deleteclass, name="joinclass"),
    path('classroom/<int:slug>/', views.classRoom, name="Classroom"),
    path('otp/', views.sendOtp, name="sendOtp"),
    path('signup/', views.handleSignUp, name="signup"),
    path('login/', views.handleLogIn, name="login"),
    path('logout/', views.handleLogout, name="logout"),
]
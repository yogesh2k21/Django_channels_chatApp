from django.urls import path
from . import views

urlpatterns=[
    path('',views.chat,name='index'),
    path('signup/',views.signup_user,name='signup'),
    path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout'),
]